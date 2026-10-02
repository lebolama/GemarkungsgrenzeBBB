"""Baut die eingefrorene Abgabeversion (Stichtagsfassung) der Website aus entwurf/.

Unterschiede zur laufenden Fassung (Entscheidung Hendrik, 02.10.2026):
  - Die Seite reconstruction_xl.html („Verschwundene Steine“) entfällt; alles, was sie zeigt,
    steht auch auf standorte.html. Alle Verweise darauf werden entfernt.
  - Die Weiterleitungsseiten für alte Adressen entfallen (die Stichtagsfassung hat keine alten Adressen).
Die geschützten Seiten standorte.html und karteXL.html werden unverändert kopiert.

Ausgabe: stichtag/<NAME>/   (NAME z. B. version-20261005; Ordner steht in .gitignore)

Aufruf:  python werkzeuge/stichtag.py version-20261005
Danach:  PYTHONIOENCODING=utf-8 python werkzeuge/ftp.py stichtag version-20261005
"""
import pathlib
import re
import shutil
import sys
from urllib.parse import unquote, urldefrag

REPO = pathlib.Path(__file__).resolve().parent.parent
QUELLE = REPO / "entwurf"
ENTFALLEN = {"reconstruction_xl.html"}
TEXT = {".html", ".js", ".css", ".json", ".geojson", ".csv", ".txt"}


def lesen(p):
    return p.read_text(encoding="utf-8", newline="")


def schreiben(p, t):
    p.write_text(t, encoding="utf-8", newline="")


def ersetzen(t, muster, neu, name, flags=0, pflicht=True):
    t2, n = re.subn(muster, neu, t, flags=flags)
    if pflicht and n == 0:
        sys.exit(f"FEHLER: Muster nicht gefunden in {name}: {muster[:60]}")
    return t2


def bauen(name):
    ziel = REPO / "stichtag" / name
    if ziel.exists():
        shutil.rmtree(ziel)
    shutil.copytree(QUELLE, ziel)

    # Weiterleitungsseiten entfallen, außer sie werden noch von einer Seite verlinkt (z. B. von der
    # geschützten karteXL.html, die nicht angefasst wird).
    weiterleitungen = {p.name for p in ziel.glob("*.html") if "Diese Seite gibt es nicht mehr" in lesen(p)}
    verlinkt = set()
    for p in ziel.glob("*.html"):
        if p.name not in weiterleitungen and p.name not in ENTFALLEN:
            verlinkt |= set(re.findall(r'href="([^"#?/:]+\.html)', lesen(p)))
    for p in sorted(ziel.glob("*.html")):
        if p.name in ENTFALLEN or (p.name in weiterleitungen and p.name not in verlinkt):
            p.unlink()

    for p in sorted(ziel.glob("*.html")):
        if p.name in ("standorte.html", "karteXL.html"):
            continue
        t = lesen(p)
        t = re.sub(r'[ \t]*<li><a href="reconstruction_xl\.html">Verschwundene Steine</a></li>\r?\n', "", t)
        if p.name == "index.html":
            t = ersetzen(t, r'[ \t]*<a class="einstieg" href="reconstruction_xl\.html">.*?</a>\r?\n', "",
                         p.name, re.S)
            t = ersetzen(t, r"alten Flurkarten und Flurnamen\. Funktioniert",
                         "alten Flurkarten und Flurnamen, dazu die berechneten Standorte der verschwundenen\n"
                         "    Steine mit einer Angabe, wie sicher sie sind. Funktioniert", p.name)
        if p.name == "berechnung.html":
            t = ersetzen(t, r'erscheinen auf der\s+<a href="reconstruction_xl\.html">Karte der verschwundenen Steine</a>'
                            r' und auf der\s+<a href="standorte\.html">Karte der Grenzsteine</a>, jeweils mit allen Angaben aus den\s+Quellen\.',
                         'erscheinen auf der\n  <a href="standorte.html">Karte der Grenzsteine</a>, mit allen Angaben aus den\n  Quellen.',
                         p.name)
        if p.name == "datenschutz.html":
            t = ersetzen(t, r"„Karte“, „Verschwundene Steine“, „Amtliche Grenzpunkte“",
                         "„Karte“, „Amtliche Grenzpunkte“", p.name)
        schreiben(p, t)

    css = ziel / "assets" / "grenze.css"
    schreiben(css, ersetzen(lesen(css), r"karteXL\.html\s+und reconstruction_xl\.html \(die haben",
                            "karteXL.html (die haben", css.name))
    return ziel


def pruefen(ziel):
    fehler = []
    for p in ziel.rglob("*"):
        if p.is_file() and p.suffix.lower() in TEXT:
            t = lesen(p)
            if re.search(r"reconstruction|rekonstruktion\.html", t, re.I):
                fehler.append(f"Verweis auf entfernte Seite: {p.relative_to(ziel)}")
    ids = {}
    seiten = sorted(ziel.glob("*.html"))
    for p in seiten:
        ids[p.name] = set(re.findall(r'\bid="([^"]+)"', lesen(p)))
    for p in seiten:
        for attr, url in re.findall(r'\b(href|src)="([^"#][^"]*|#[^"]*)"', lesen(p)):
            if re.match(r"(https?:|mailto:|data:|javascript:|//)", url) or "+" in url or "{" in url:
                continue
            pfad, frag = urldefrag(url)
            if not pfad:
                if frag and frag not in ids[p.name]:
                    fehler.append(f"{p.name}: toter Anker #{frag}")
                continue
            pfad = unquote(pfad.split("?")[0])
            f = (p.parent / pfad)
            if not f.exists():
                fehler.append(f"{p.name}: toter Link {url}")
            elif frag and f.suffix == ".html" and f.name in ids and frag not in ids[f.name]:
                fehler.append(f"{p.name}: toter Anker {url}")
    return fehler


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    ziel = bauen(sys.argv[1])
    dateien = [p for p in ziel.rglob("*") if p.is_file()]
    print(f"{ziel.relative_to(REPO)}: {len(dateien)} Dateien, "
          f"{round(sum(p.stat().st_size for p in dateien) / 1e6)} MB, "
          f"{len(list(ziel.glob('*.html')))} HTML-Seiten")
    fehler = pruefen(ziel)
    for f in fehler:
        print("  ", f)
    print("Prüfung:", "OK, keine Verweise auf die entfernte Seite, keine toten Links" if not fehler
          else f"{len(fehler)} Auffälligkeit(en)")
