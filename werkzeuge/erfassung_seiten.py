"""Erzeugt für Protokolle ohne vollständige Fließtext-Abschrift je eine Seite
„Die Steine im Grenzgang …“: alle Einträge Stein für Stein aus data.json (= Hendriks Excel-Erfassung),
dazu die Randbemerkungen aus den PDF-Kommentaren in „Büschemer Gemarkungsumgehungen.pdf“.

Ausgabe: entwurf/erfassung-1569.html, -1608.html, -1700.html, -1749.html

Aufruf:  python werkzeuge/erfassung_seiten.py
"""
import html
import json
import pathlib
import re

import fitz

REPO = pathlib.Path(__file__).resolve().parent.parent
ENTWURF = REPO / "entwurf"
SAMMEL = pathlib.Path(r"F:\User\Dokumente2\Tauberfranken\_Büscheme\Büschemer Gemarkungsumgehungsbücher\PDF\Büschemer Gemarkungsumgehungen.pdf")

# Kommentare, die keine Steinbeschreibung sind (Einleitungen, Wechsel der Begleiter, Nachträge);
# (PDF-Seite in der Sammeldatei, Anfang des Kommentars, Überschrift auf der Website)
RAND = {
    "1569": [(2, "??, f??? ?? uff Montag", "Der Anfang des Protokolls von 1569")],
    "1580": [(41, "wegen großen Rinderfeldt", "Wechsel der Begleiter an der Grenze zu Großrinderfeld (Abschrift 1580)")],
    "1608": [(50, "Ano 1608", "Der Anfang des Protokolls von 1608"),
             (68, "18.) Ein rother Stein", "Anmerkung beim Dreimärker Bischofsheim – Großrinderfeld – Impfingen")],
}

# Ausführlicher Wortlaut aus den PDF-Kommentaren ersetzt die Kurzfassung aus der Tabelle
# (Entscheidung Hendrik 28.09.2026). Seitenbereiche in der Sammeldatei; nur Nummern, deren
# Zuordnung geprüft ist (1608: Nummerierung der Kommentare weicht ab, daher nur Nr. 1).
WORTLAUT = {
    "1569": {"bereiche": [(1, 20), (21, 48)], "nur": None},
    "1608": {"bereiche": [(49, 77)], "nur": {1}},
}

SEITEN = {
    "1569": {"prefix": "1569 (1580)", "titel": "1569 (wiederholt 1580)",
             "quelle": "Gemarkungsumgehungsbuch 1569, Stadtarchiv Tauberbischofsheim, Abt. B, Nr. 3; Abschrift 1580, Abt. B, Nr. 4",
             "rand": ["1569", "1580"]},
    "1608": {"prefix": "1608", "titel": "1608",
             "quelle": "Gemarkungsumgehungsbuch 1608, Stadtarchiv Tauberbischofsheim, Abt. B, Nr. 5", "rand": ["1608"]},
    "1700": {"prefix": "1700", "titel": "1700",
             "quelle": "Gemarkungsumgehungsbuch 1700, Stadtarchiv Tauberbischofsheim, Abt. B, Nr. 7", "rand": []},
    "1749": {"prefix": "1749", "titel": "1749",
             "quelle": "Gemarkungsumgehungsbuch 1749, Stadtarchiv Tauberbischofsheim, Abt. B, Nr. 8", "rand": []},
}


def leer(v):
    return v is None or str(v).strip() in ("", "nan")


def e(v):
    return html.escape(str(v).strip())


def randbemerkungen(schluessel):
    if not SAMMEL.exists():
        return []
    d = fitz.open(SAMMEL)
    gefunden = []
    for jahr in schluessel:
        for seite, anfang, ueberschrift in RAND.get(jahr, []):
            for a in d[seite - 1].annots() or []:
                t = (a.info.get("content") or "").strip()
                if t.startswith(anfang[:12]):
                    gefunden.append((ueberschrift, t.replace("\r", "\n")))
                    break
            else:
                print("  WARNUNG: Randbemerkung nicht gefunden:", jahr, seite, anfang)
    return gefunden


def rand_html(text):
    zeilen = [html.escape(z.strip()) for z in text.split("\n") if z.strip()]
    t = "<br>".join(zeilen)
    t = re.sub(r"(\[[^\]]*\])", r'<span class="anm">\1</span>', t)
    t = re.sub(r"\?{2,}|\(\?\)", lambda m: f'<span class="unsicher">{m.group(0)}</span>', t)
    return t


def wortlaut(jahr):
    cfg = WORTLAUT.get(jahr)
    if not cfg or not SAMMEL.exists():
        return {}
    d = fitz.open(SAMMEL)
    out = {}
    for a, b in cfg["bereiche"]:
        for i in range(a - 1, b):
            for x in d[i].annots() or []:
                t = (x.info.get("content") or "").strip().replace(chr(13), chr(10))
                t = re.sub(r"^wegen großen Rinderfeldt\s*" + chr(10), "", t)  # Randvermerk vor Stein 70 (1580)
                m = re.match(r"^\s*(\d+)\s*(?:\.\)|\.|:|\s)(?:\s*&\s*(\d+)\s*\.\))?", t)
                if not m:
                    continue
                for n in (m.group(1), m.group(2)):
                    if n and (cfg["nur"] is None or int(n) in cfg["nur"]):
                        out[int(n)] = t
    return out


def nr_schluessel(v):
    try:
        return int(float(str(v).strip()))
    except ValueError:
        return None


def merkmale(r, p):
    teile = []
    feld = lambda n: r.get(f"{p} — {n}")
    if not leer(feld("Jahr")): teile.append(f"Jahreszahl {e(feld('Jahr'))}")
    g = feld("groß/klein") if not leer(feld("groß/klein")) else feld("groß/ klein")
    if not leer(g): teile.append(e(g))
    if not leer(feld("Farbe")): teile.append(e(feld("Farbe")))
    w = feld("Wappen") if feld("Wappen") is not None else feld("Wappenschild")
    if not leer(w): teile.append("Wappen" if str(w).strip().lower() == "x" else f"Wappen: {e(w)}")
    if not leer(feld("Rad")): teile.append("Mainzer Rad" if str(feld("Rad")).strip().lower() == "x" else f"Rad: {e(feld('Rad'))}")
    if not leer(feld("b")):
        b = str(feld("b")).strip()
        teile.append(f"{b} „b“" if b.isdigit() else f"b: {e(b)}")
    if not leer(feld("Kreuz oben")): teile.append("Kreuz oben")
    if not leer(feld("Rückseite")): teile.append(f"Rückseite: {e(feld('Rückseite'))}")
    return " · ".join(teile) or "–"


def abstand(r, p):
    rk = next((k for k in r if k.startswith(p + " — Ruthen")), None)
    if rk and not leer(r[rk]) and str(r[rk]).strip() != "?":
        return f"{e(r[rk])} Ruten"
    return "–"


def seite(jahr, cfg, daten):
    p = cfg["prefix"]
    wl = wortlaut(jahr)
    zeilen = []
    for r in daten:
        if not any(k.startswith(p + " — ") and not leer(v) for k, v in r.items()):
            continue
        nr = r.get(f"{p} — Nr.")
        text = r.get(f"{p} — sonstiges")
        voll = wl.get(nr_schluessel(nr)) if not leer(nr) else None
        zeilen.append(
            f'<tr><td class="nr">{e(nr) if not leer(nr) else "–"}</td>'
            f'<td><a href="stein.html?id={r["ID"]}">{r["ID"]}</a><br><span class="klein">{e(r["Grenze"])}</span></td>'
            f"<td>{merkmale(r, p)}</td><td class=\"nr\">{abstand(r, p)}</td>"
            f'<td class="lage">{rand_html(voll) if voll else (e(text) if not leer(text) else "")}</td></tr>')
    rand = randbemerkungen(cfg["rand"])
    rand_block = ""
    if rand:
        rand_block = "<h2>Aus dem Protokoll: Randbemerkungen</h2>\n" + "\n".join(
            f'<section class="rand"><h3>{html.escape(u)}</h3><p>{rand_html(t)}</p></section>' for u, t in rand)
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Die Steine im Grenzgang {cfg['titel']} – Grenzsteine Tauberbischofsheim</title>
<meta name="description" content="Alle Grenzsteine im Tauberbischofsheimer Grenzgang {cfg['titel']}, Stein für Stein aus dem Protokoll erfasst.">
<link rel="stylesheet" href="assets/grenze.css">
<script src="assets/menue.js" defer></script>
<style>
td.nr{{white-space:nowrap}}
td.lage{{font-style:italic}}
.rand{{background:var(--weiss);border:1px solid var(--linie);border-radius:6px;padding:.8rem 1rem;margin:1rem 0}}
.rand h3{{margin-top:0;font-size:1rem;color:var(--rot)}}
.rand p{{font-style:italic;line-height:1.65;margin:0;overflow-wrap:anywhere}}
.rand .anm{{color:var(--grau);font-style:normal}}
.rand .unsicher{{color:#9a5a00}}
</style>
</head>
<body>
<!-- KOPF -->
<!-- /KOPF -->

<main>
<div class="text">
<p class="klein"><a href="protokolle.html#regal">← Zurück zu den Protokollen</a></p>
<h1>Die Steine im Grenzgang {cfg['titel']}</h1>
<p class="einleitung">Alle Grenzsteine, die das Protokoll nennt, Stein für Stein aus dem Original
erfasst: Nummer, Zeichen, Abstand zum vorigen Stein und die Lagebeschreibung. Quelle:
{html.escape(cfg['quelle'])}.</p>
<div class="kasten">
<p><strong>Zur Form dieser Abschrift.</strong> Für dieses Buch sind die Einträge Stein für Stein in
einer Tabelle erfasst. Nicht übernommen sind Passagen, die für die Steine und ihre Abstände keine
Bedeutung haben – vor allem die Namen der Männer, die auf den einzelnen Grenzabschnitten dabei
waren, und der Wechsel der Begleiter zwischen den Nachbarorten. Wie ein solches Protokoll im
Ganzen berichtet, zeigen die vollständigen Abschriften von
<a href="transkription-1683.html">1683</a> und <a href="transkription-1872.html">1872</a>.
Die Lagebeschreibungen folgen der Schreibweise des Originals; einzelne Einträge sind knapp
zusammengefasst.</p>
</div>
{rand_block}
<h2>Die Steine</h2>
<p class="klein">„Stein“ ist die laufende Nummer dieser Website und führt zum Steckbrief; „Nr.“ ist
die Nummer im Protokoll. Der Abstand ist in fränkischen Werkruten (3,65 m) angegeben.</p>
</div>
<div class="tabelle-rahmen">
<table>
<thead><tr><th scope="col">Nr.</th><th scope="col">Stein</th><th scope="col">Zeichen und Aussehen</th>
<th scope="col">Abstand</th><th scope="col">Lage und Bemerkungen</th></tr></thead>
<tbody>
{chr(10).join(zeilen)}
</tbody>
</table>
</div>
<div class="text"><p class="klein"><a href="protokolle.html#regal">← Zurück zu den Protokollen</a></p></div>
</main>

<!-- FUSS -->
<!-- /FUSS -->
</body>
</html>
""", len(zeilen), len(rand)


def main():
    daten = json.loads((ENTWURF / "data.json").read_text(encoding="utf-8"))
    for jahr, cfg in SEITEN.items():
        text, n, nr = seite(jahr, cfg, daten)
        ziel = ENTWURF / f"erfassung-{jahr}.html"
        ziel.write_text(text, encoding="utf-8", newline="\n")
        print(f"{ziel.name}: {n} Steine, {nr} Randbemerkungen, {round(ziel.stat().st_size / 1024)} KB")


if __name__ == "__main__":
    main()
