"""Erzeugt aus Hendriks Transkriptionen (PDF) Leseseiten für die Website:
entwurf/transkription-1683.html und entwurf/transkription-1872.html.

Zeilenumbrüche bleiben wie in der Abschrift, Seitenmarken („-Seite 12-“, „[Seitenwechsel]“)
werden zu Zwischenüberschriften bzw. Trennlinien, Anmerkungen in [eckigen Klammern] und
unsichere Lesungen (?) werden hervorgehoben.

Aufruf:  python werkzeuge/transkription_seiten.py
"""
import html
import pathlib
import re

import fitz

QUELLE = pathlib.Path(r"F:\User\Dokumente2\Tauberfranken\_Büscheme\Büschemer Gemarkungsumgehungsbücher\PDF")
ZIEL = pathlib.Path(__file__).resolve().parent.parent / "entwurf"

PROTOKOLLE = {
    "1683": {
        "datei": "Büschemer Gemarkungsumgehung 1683 - Transkript.pdf",
        "titel": "Gemarkungsumgehungsbuch 1683",
        "signatur": "Stadtarchiv Tauberbischofsheim, Abt. B, Nr. 6",
        "umfang": "47 Seiten im Original, 108 Steine",
    },
    "1872": {
        "datei": "Büschemer Gemarkungsumgehung 1872 - Transkript (Version 13.9.21).pdf",
        "titel": "Grenzbeschreibung der Gemarkung Tauberbischofsheim 1872",
        "signatur": "Stadtarchiv Tauberbischofsheim, Abt. B, Nr. 8a",
        "umfang": "239 beschriebene Seiten im Original, mit den Grenzberichtigungen 1887–1893",
    },
}


def zeile(t: str) -> str:
    t = html.escape(t)
    t = re.sub(r"(\[[^\]]*\])", r'<span class="anm">\1</span>', t)
    t = re.sub(r"\(\?+\)", lambda m: f'<span class="unsicher">{m.group(0)}</span>', t)
    return t


def umwandeln(text: str) -> tuple[str, list]:
    teile, absatz, seiten = [], [], []

    def absatz_ende():
        if absatz:
            teile.append("<p>" + "<br>".join(absatz) + "</p>")
            absatz.clear()

    for roh in text.splitlines():
        s = roh.strip()
        m = re.match(r"^-\s*Seite\s+(\d+)\s*-$", s)
        if m:
            absatz_ende()
            n = m.group(1)
            seiten.append(n)
            teile.append(f'<h3 class="seite" id="seite-{n}">Seite {n}</h3>')
            continue
        if re.match(r"^\[(Seitenwechsel|n[äa]chste seite)\]$", s, re.I):
            absatz_ende()
            teile.append('<hr class="seitenwechsel" aria-label="Seitenwechsel">')
            continue
        if not s:
            absatz_ende()
            continue
        absatz.append(zeile(s))
    absatz_ende()
    return "\n".join(teile), seiten


def seite(jahr: str, p: dict) -> str:
    d = fitz.open(QUELLE / p["datei"])
    text = "\n".join(s.get_text() for s in d)
    koerper, seiten = umwandeln(text)
    sprung = ""
    if seiten:
        sprung = ('<details class="hilfe"><summary>Zu einer Seite springen</summary><p class="seitenliste">'
                  + " ".join(f'<a href="#seite-{n}">{n}</a>' for n in seiten) + "</p></details>")
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Transkription {jahr} – Grenzsteine Tauberbischofsheim</title>
<meta name="description" content="Vollständige Transkription: {html.escape(p['titel'])}, {html.escape(p['signatur'])}.">
<link rel="stylesheet" href="assets/grenze.css">
<script src="assets/menue.js" defer></script>
<style>
.abschrift-text p{{font-family:Georgia,serif;line-height:1.65;margin:0 0 1rem;overflow-wrap:anywhere}}
.abschrift-text .anm{{color:var(--grau);font-style:italic}}
.abschrift-text .unsicher{{color:#9a5a00}}
.abschrift-text h3.seite{{font-size:.95rem;color:var(--grau);border-top:1px solid var(--linie);padding-top:.6rem;margin:1.6rem 0 .8rem}}
.abschrift-text hr.seitenwechsel{{border:0;border-top:1px dashed var(--linie);margin:1.2rem 0}}
.seitenliste a{{display:inline-block;min-width:2.2rem;margin:.1rem 0}}
</style>
</head>
<body>
<!-- KOPF -->
<!-- /KOPF -->

<main>
<div class="text">
<p class="klein"><a href="protokolle.html#regal">← Zurück zu den Protokollen</a></p>
<h1>Transkription: {html.escape(p['titel'])}</h1>
<p class="einleitung">Vollständige Abschrift von Hendrik Beierstettel.
{html.escape(p['signatur'])}; {html.escape(p['umfang'])}.</p>
<div class="kasten">
<p><strong>So ist die Abschrift zu lesen.</strong> Zeilenumbrüche entsprechen dem Original.
Schreibweisen sind unverändert übernommen. <span style="color:#9a5a00">(?)</span> kennzeichnet
eine unsichere Lesung, <em>[eckige Klammern]</em> Anmerkungen des Transkribenten.
„Distat“ gibt den Abstand zum vorigen Stein an. Mit Strg+F (am Handy: „Auf Seite suchen“)
lässt sich nach Steinen, Namen oder Jahreszahlen suchen.</p>
</div>
{sprung}
<div class="abschrift-text">
{koerper}
</div>
<p class="klein"><a href="protokolle.html#regal">← Zurück zu den Protokollen</a></p>
</div>
</main>

<!-- FUSS -->
<!-- /FUSS -->
</body>
</html>
"""


def main():
    for jahr, p in PROTOKOLLE.items():
        ziel = ZIEL / f"transkription-{jahr}.html"
        ziel.write_text(seite(jahr, p), encoding="utf-8", newline="\n")
        print(ziel.name, round(ziel.stat().st_size / 1024), "KB")


if __name__ == "__main__":
    main()
