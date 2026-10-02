"""Erzeugt aus docs/bewerbung/dokumentation.md (bzw. kriterienkatalog.md) ein druckfertiges HTML
und daraus mit Microsoft Edge (headless) ein PDF.

Aufruf:  python werkzeuge/dokumentation_pdf.py dokumentation
         python werkzeuge/dokumentation_pdf.py kriterienkatalog
"""
import base64
import html
import pathlib
import re
import subprocess
import sys
import time

REPO = pathlib.Path(__file__).resolve().parent.parent
BEW = REPO / "docs" / "bewerbung"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Platzhalter „[Abb. …]“ → Abbildungsdateien und Bildunterschriften
ABB = {
    "Abb. 1": [("01-start.jpg", "Abb. 1: Die Startseite")],
    "Abb. 2": [("02-protokolle.jpg", "Abb. 2: Die Seite „Die Protokolle“ – der „1308er“ in drei Jahrhunderten, Original und Abschrift")],
    "Abb. 3": [("03-berechnung.jpg", "Abb. 3: „So wird gerechnet“ – das Rechenbeispiel Stein 367 bis 370")],
    "Abb. 4": [("04-standorte.jpg", "Abb. 4: Karte der Grenzsteine, hier mit der Ebene „Grenzgang 1872“: grün eingemessene Steine, orange und rot berechnete Standorte verschwundener Steine mit Sicherheitsklasse"),
               ("05-steckbrief.jpg", "Abb. 5: Steckbrief eines Steins (Stein 94, Eckstein von 1474)"),
               ("06-suche.jpg", "Abb. 6: Die Suche, hier: Steine an der Grenze zu Impfingen mit Mainzer Rad im Jahr 1608")],
}

CSS = """
@page { size: A4; margin: 20mm 20mm 20mm 22mm; }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 10.5pt; line-height: 1.45; color: #1f1b16; }
h1 { font-size: 22pt; color: #6b0000; margin: 0 0 4mm; line-height: 1.15; }
h2 { font-size: 14pt; color: #6b0000; margin: 7mm 0 2mm; break-after: avoid; }
h3 { font-size: 11.5pt; margin: 5mm 0 1.5mm; break-after: avoid; }
p { margin: 0 0 2.5mm; text-align: justify; hyphens: auto; }
p.kopf { text-align: left; }
ul, ol { margin: 0 0 3mm 5mm; padding-left: 4mm; }
li { margin-bottom: 1mm; }
table { border-collapse: collapse; width: 100%; margin: 2mm 0 4mm; font-size: 9.5pt; }
tr { break-inside: avoid; }
th, td { border: 0.3mm solid #cfc6b6; padding: 1.2mm 2mm; text-align: left; vertical-align: top; }
th { background: #f0e7d6; }
hr { border: 0; border-top: 0.3mm solid #cfc6b6; margin: 5mm 0; }
figure { margin: 3mm 0 5mm; break-inside: avoid; }
figure img { width: 100%; border: 0.3mm solid #cfc6b6; }
figcaption { font-size: 8.5pt; color: #5c554c; margin-top: 1mm; }
.titel { height: 245mm; display: flex; flex-direction: column; justify-content: center; break-after: page; }
.titel h1 { font-size: 28pt; }
.titel .unter { font-size: 15pt; color: #3a332c; margin-bottom: 12mm; }
.titel .meta { font-size: 11pt; line-height: 1.6; }
.titel img { width: 70mm; margin-bottom: 10mm; border-radius: 2mm; }
.offen { background: #ffe9a8; }
a { color: #6b0000; text-decoration: none; }
"""


def inline(t: str) -> str:
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"(https?://[^\s<)]+)", r'<a href="\1">\1</a>', t)
    t = t.replace("✏️", '<span class="offen">✏️</span>')
    return t


def bild(datei: str) -> str:
    daten = (BEW / "abbildungen" / datei).read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(daten).decode()


def umwandeln(md: str, titelblatt: bool) -> str:
    zeilen = md.splitlines()
    out, i = [], 0
    if titelblatt:
        # Titel, Untertitel und Kopfblock bis zur ersten Trennlinie bilden das Titelblatt
        kopf = []
        while i < len(zeilen) and zeilen[i].strip() != "---":
            kopf.append(zeilen[i]); i += 1
        i += 1
        titel = next(z[2:] for z in kopf if z.startswith("# "))
        unter = next((z[3:] for z in kopf if z.startswith("## ")), "")
        rest, block = [], []
        for z in kopf + [""]:
            if z.strip() and not z.startswith("#"):
                block.append(z.strip())
            elif block:
                rest.append(" ".join(block)); block = []
        out.append('<section class="titel">')
        out.append(f'<img src="{bild_titel()}" alt="">')
        out.append(f"<h1>{inline(titel)}</h1><div class='unter'>{inline(unter)}</div>")
        out.append("<div class='meta'>" + "<br>".join(inline(z) for z in rest) + "</div></section>")
    liste = None
    while i < len(zeilen):
        z = zeilen[i].rstrip()
        s = z.strip()
        if not s:
            if liste: out.append(f"</{liste}>"); liste = None
            i += 1; continue
        m = re.match(r"✏️ \[(Abb\. \d+)", s)
        if m:
            for datei, unterschrift in ABB[m.group(1)]:
                out.append(f'<figure><img src="{bild(datei)}" alt=""><figcaption>{inline(unterschrift)}</figcaption></figure>')
            i += 1; continue
        if s.startswith("|"):
            tab = []
            while i < len(zeilen) and zeilen[i].strip().startswith("|"):
                tab.append([c.strip() for c in zeilen[i].strip().strip("|").split("|")]); i += 1
            kopf, koerper = tab[0], [r for r in tab[1:] if not re.match(r"^:?-+:?$", r[0])]
            out.append("<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in kopf) + "</tr></thead><tbody>")
            def zelle(c):
                m = re.match(r"^\{rs=(\d+)\}\s*(.*)$", c)
                return f'<td rowspan="{m.group(1)}">{inline(m.group(2))}</td>' if m else f"<td>{inline(c)}</td>"
            out += ["<tr>" + "".join(zelle(c) for c in r if c != "~") + "</tr>" for r in koerper]
            out.append("</tbody></table>"); continue
        if s == "[Unterschrift]":
            out.append('<div style="height:22mm"></div>'); i += 1; continue
        if s == "---":
            out.append("<hr>"); i += 1; continue
        h = re.match(r"^(#{1,3}) (.*)", s)
        if h:
            n = len(h.group(1)); out.append(f"<h{n}>{inline(h.group(2))}</h{n}>"); i += 1; continue
        lm = re.match(r"^(\d+\.|-) (.*)", s)
        if lm:
            art = "ol" if lm.group(1)[0].isdigit() else "ul"
            if liste != art:
                if liste: out.append(f"</{liste}>")
                out.append(f"<{art}>"); liste = art
            text = lm.group(2); i += 1
            while i < len(zeilen) and zeilen[i].startswith("  ") and zeilen[i].strip():
                text += " " + zeilen[i].strip(); i += 1
            out.append(f"<li>{inline(text)}</li>"); continue
        if liste: out.append(f"</{liste}>"); liste = None
        absatz = [s]; hart = [zeilen[i].endswith("  ")]; i += 1
        while i < len(zeilen) and zeilen[i].strip() and not re.match(r"^(#|\||-|\d+\.|✏️ \[|---|\[Unterschrift)", zeilen[i].strip()):
            absatz.append(zeilen[i].strip()); hart.append(zeilen[i].endswith("  ")); i += 1
        if any(hart):
            teile = ""
            for a, h in zip(absatz, hart):
                teile += inline(a) + ("<br>" if h else " ")
            out.append('<p class="kopf">' + teile.rstrip("<br> ") + "</p>"); continue
        if len(absatz) > 1 and (all(a.startswith("**") for a in absatz) or all(len(a) < 60 for a in absatz)):
            out.append("<p>" + "<br>".join(inline(a) for a in absatz) + "</p>")
        else:
            out.append(f"<p>{inline(' '.join(absatz))}</p>")
    if liste: out.append(f"</{liste}>")
    return "\n".join(out)


def bild_titel() -> str:
    p = REPO / "entwurf" / "bilder" / "grenzstein-mainzer-rad.jpg"
    return "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode()


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "dokumentation"
    md = (BEW / f"{name}.md").read_text(encoding="utf-8")
    titelblatt = name == "dokumentation"
    körper = umwandeln(md, titelblatt)
    seite = f"<!DOCTYPE html><html lang='de'><head><meta charset='utf-8'><title>{name}</title><style>{CSS}</style></head><body>{körper}</body></html>"
    html_datei = BEW / f"{name}.html"
    html_datei.write_text(seite, encoding="utf-8")
    ziele = {"dokumentation": "Dokumentation_Grenzsteine_Tauberbischofsheim.pdf",
             "kriterienkatalog": "Kriterienkatalog_Grenzsteine_Tauberbischofsheim.pdf"}
    pdf = BEW / ziele[name]
    # Alte PDF entfernen: Läuft noch ein Edge mit demselben Profil, beendet sich der neue Aufruf
    # sonst stillschweigend, und die veraltete Datei bliebe unbemerkt liegen.
    pdf.unlink(missing_ok=True)
    for _ in range(3):
        subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        f"--user-data-dir={BEW / '.edge-profil'}", f"--print-to-pdf={pdf}",
                        html_datei.as_uri()], check=True, capture_output=True, timeout=120)
        for _ in range(30):
            if pdf.exists() and pdf.stat().st_size > 0:
                break
            time.sleep(1)
        if pdf.exists():
            break
    if not pdf.exists():
        sys.exit(f"FEHLER: {pdf.name} wurde nicht erzeugt")
    print(pdf.name, round(pdf.stat().st_size / 1e6, 2), "MB")


if __name__ == "__main__":
    main()
