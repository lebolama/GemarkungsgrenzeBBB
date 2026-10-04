"""Datenkorrektur vom 04.10.2026, Teil 2: drei Meterwerte 1872 (Entscheidung Hendrik).

- Stein 69  (Dittwar Nr. 17):        190,0 → 190,8   (Abschrift S. 85: 63 Ruthen 6 Fuß oder 190 Meter 80)
- Stein 316 (Großrinderfeld Nr. 7):  152,2 → 154,2   (Abschrift S. 34: 51 Ruthen 4 Fuß oder 154 Meter 20)
- Stein 365 (Grünsfeld Nr. 5):        65,0 →  65,1   (Original: 21 Ruthen 7 Fuß, Meterwert durchgestrichen)

69 und 316 sind GPS-Anker; ihre Meterwerte ändern keine berechneten Standorte. Bei 365 wird die Kette
364 → 365 → 366 → 367 neu gerechnet (Verfahren wie in datenkorrektur_20261004.py; vorher wird geprüft,
dass die Rechnung mit den alten Werten die gespeicherten Einträge reproduziert).

Aufruf:  python werkzeuge/datenkorrektur_20261004b.py [--schreiben]
"""
import json
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from geo_linie import lade, xy  # noqa: E402

ENTWURF = pathlib.Path(__file__).resolve().parent.parent / "entwurf"
SCHREIBEN = "--schreiben" in sys.argv
daten = json.loads((ENTWURF / "data.json").read_text(encoding="utf-8"))
pos = json.loads((ENTWURF / "standorte-positionen.json").read_text(encoding="utf-8"))
linie = lade(str(ENTWURF / "Gemarkungsgrenze Tauberbischofsheim.geojson"))[0]
by = {r["ID"]: r for r in daten}
J = "1872"
SPALTE = f"{J} — Meter zum vorherigen"
P = pos["years"][J]


def gps(i):
    g = by[i].get("_gps_parsed") or {}
    return (g["lat"], g["lon"])


def kette(links, rechts, ids):
    """Neu berechnete Einträge für die Steine `ids` zwischen den Ankern links und rechts."""
    ds = [float(by[i][SPALTE]) for i in ids + [rechts]]
    S = sum(ds)
    sl, sr = linie.projiziere(*gps(links))[1], linie.projiziere(*gps(rechts))[1]
    rest = (sl - sr) - S
    out, cum = {}, 0.0
    for i, d in zip(ids, ds):
        cum += d
        if cum <= S - cum:
            la, lo = linie.punkt(sl - cum)
            d_a = cum
        else:
            la, lo = linie.punkt(sr + (S - cum))
            d_a = S - cum
        out[i] = (la, lo, d_a, rest)
    return out


def pruefe(neu, vergleiche_alt):
    for i, (la, lo, d_a, rest) in neu.items():
        e = P[str(i)]
        ab = math.hypot(*[a - b for a, b in zip(xy(la, lo), xy(e["lat"], e["lon"]))])
        assert ab < 0.05 and abs(d_a - e["anchorDistance"]) < 0.05 and abs(rest - e["closureResidual"]) < 0.05, \
            f"Kette reproduziert Stein {i} nicht: {ab:.2f} m, {d_a} vs {e['anchorDistance']}, {rest} vs {e['closureResidual']}"


# 1. Probe mit den alten Werten
alt = kette(364, 367, [365, 366])
pruefe(alt, True)
print("Probe bestanden: Kette 364–367 mit den alten Werten reproduziert die gespeicherten Einträge.")

# 2. Meterwerte ändern
for i, wert in ((69, 190.8), (316, 154.2), (365, 65.1)):
    print(f"Stein {i}: {by[i][SPALTE]} → {wert}")
    by[i][SPALTE] = wert

# 3. Kette 365/366 neu
neu = kette(364, 367, [365, 366])
for i, (la, lo, d_a, rest) in neu.items():
    for e in [P[str(i)]] + [pos["years"][y][str(i)] for y in pos["years"] if y != J and str(i) in pos["years"][y]
                            and pos["years"][y][str(i)].get("sourceYear") == J]:
        old = (e["lat"], e["lon"])
        e.update(lat=la, lon=lo, anchorDistance=d_a, closureResidual=rest, counterpartDifference=abs(rest))
        print(f"  Stein {i} ({'1872' if e is P[str(i)] else 'übernommen'}): Verschiebung "
              f"{math.hypot(*[a - b for a, b in zip(xy(*old), xy(la, lo))]):.2f} m, Rest {rest:+.2f} m")

if SCHREIBEN:
    (ENTWURF / "data.json").write_text(json.dumps(daten, indent=2, ensure_ascii=False), encoding="utf-8", newline="")
    (ENTWURF / "standorte-positionen.json").write_text(json.dumps(pos, indent=2, ensure_ascii=False) + "\n",
                                                        encoding="utf-8", newline="")
    print("geschrieben: data.json, standorte-positionen.json")
else:
    print("Probelauf – nichts geschrieben.")
