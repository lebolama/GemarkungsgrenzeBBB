"""Setzt Kopf- und Fußzeile in alle Seiten von entwurf/, die die Marken
<!-- KOPF --> ... <!-- /KOPF --> und <!-- FUSS --> ... <!-- /FUSS --> enthalten.

Die drei geschützten Seiten (standorte.html, karteXL.html,
reconstruction_xl.html) enthalten diese Marken nicht und werden nie berührt.

Aufruf:  python werkzeuge/rahmen.py
"""
import pathlib
import re

ENTWURF = pathlib.Path(__file__).resolve().parent.parent / "entwurf"
GESCHUETZT = {"standorte.html", "karteXL.html", "reconstruction_xl.html"}

MENUE = [
    ("index.html", "Start"),
    ("standorte.html", "Karte"),
    ("reconstruction_xl.html", "Verschwundene Steine"),
    ("recherche.html", "Steine suchen"),
    ("grenzgaenge.html", "Die Grenzgänge"),
    ("chronik.html", "Geschichte"),
    ("quellen.html", "Quellen und Methode"),
    ("begriffe.html", "Begriffe"),
    ("projekt.html", "Über das Projekt"),
]

FUSS_LINKS = [
    ("karteXL.html", "Amtliche Grenzpunkte"),
    ("artikel.html", "Artikel"),
    ("download.html", "Daten"),
    ("impressum.html", "Impressum"),
    ("datenschutz.html", "Datenschutz"),
]


def kopf(datei: str) -> str:
    punkte = []
    for ziel, text in MENUE:
        aktuell = ' aria-current="page"' if ziel == datei else ""
        punkte.append(f'      <li><a href="{ziel}"{aktuell}>{text}</a></li>')
    return (
        '<!-- KOPF -->\n'
        '<header class="kopf">\n'
        '  <div class="kopf-innen">\n'
        '    <a class="marke" href="index.html">Grenzsteine Tauberbischofsheim</a>\n'
        '    <button class="menue-knopf" type="button" aria-expanded="false" aria-controls="hauptmenue">Menü</button>\n'
        '    <nav id="hauptmenue" aria-label="Hauptmenü">\n'
        '    <ul>\n' + "\n".join(punkte) + '\n    </ul>\n'
        '    </nav>\n'
        '  </div>\n'
        '</header>\n'
        '<!-- /KOPF -->'
    )


def fuss(datei: str) -> str:
    links = "\n".join(f'      <li><a href="{z}">{t}</a></li>' for z, t in FUSS_LINKS)
    return (
        '<!-- FUSS -->\n'
        '<footer class="fuss">\n'
        '  <div class="fuss-innen">\n'
        '    <span>© Hendrik Beierstettel, Tauberbischofsheim</span>\n'
        '    <ul>\n' + links + '\n    </ul>\n'
        '  </div>\n'
        '</footer>\n'
        '<!-- /FUSS -->'
    )


def main() -> None:
    for pfad in sorted(ENTWURF.glob("*.html")):
        if pfad.name in GESCHUETZT:
            continue
        text = pfad.read_text(encoding="utf-8")
        if "<!-- KOPF -->" not in text:
            continue
        neu = re.sub(r"<!-- KOPF -->.*?<!-- /KOPF -->", lambda m: kopf(pfad.name), text, flags=re.S)
        neu = re.sub(r"<!-- FUSS -->.*?<!-- /FUSS -->", lambda m: fuss(pfad.name), neu, flags=re.S)
        if neu != text:
            pfad.write_text(neu, encoding="utf-8", newline="\n")
            print("Rahmen gesetzt:", pfad.name)


if __name__ == "__main__":
    main()
