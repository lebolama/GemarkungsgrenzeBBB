"""Datenkorrektur vom 04.10.2026 (Entscheidungen Hendrik):

1. Stein 388 (Dittigheim, Begehung 156) wurde nach 1872 versetzt: Zustand „versetzt“, der berechnete
   Standort je Grenzgang wird aus dem näheren Anker (387 bzw. 389) berechnet.
2. Stein 66 (Dittwar) ist nicht die Begehungsnummer 126, sondern 125 (Zuordnung vermutlich):
   neue GPS-Position und Fotos; Stein 67 wird für 1872 aus dem neuen Anker 66 berechnet.

Das Verfahren entspricht dem Modell „anchor-interval-v1“ in standorte-positionen.json (an 4
vorhandenen Einträgen auf 0,0 m genau nachgerechnet): Anker auf die Grenzlinie projizieren,
vom vorherigen Anker um die Protokollstrecke zurück, vom folgenden Anker nach vorn (Linienrichtung
entgegen der Steinfolge).

Aufruf:  python werkzeuge/datenkorrektur_20261004.py            (Probelauf, schreibt nichts)
         python werkzeuge/datenkorrektur_20261004.py --schreiben
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

LINKS = "Distanzkette vom vorherigen GPS-Anker; auf den zugehörigen historischen Grenzast ausgerichtet"
RECHTS = "Distanzkette vom folgenden GPS-Anker; auf den zugehörigen historischen Grenzast ausgerichtet"


def meter(r, jahr):
    v = r.get(f"{jahr} — Meter zum vorherigen")
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def gps(i):
    g = by[i].get("_gps_parsed") or {}
    return (g["lat"], g["lon"]) if g.get("lat") else None


def berechne(jahr, links, mitte, rechts, abstaende):
    """abstaende: Strecken links→…→mitte→…→rechts im Jahr; mitte ist der berechnete Stein."""
    s_l = linie.projiziere(*gps(links))[1]
    s_r = linie.projiziere(*gps(rechts))[1]
    vorn, hinten = abstaende  # links→mitte, mitte→rechts
    summe = vorn + hinten
    lin = s_l - s_r  # Linienrichtung ist der Steinfolge entgegengesetzt
    rest = lin - summe
    if vorn <= hinten:
        la, lo = linie.punkt(s_l - vorn)
        d, text = vorn, LINKS
    else:
        la, lo = linie.punkt(s_r + hinten)
        d, text = hinten, RECHTS
    gut = abs(rest) <= 20 or abs(rest) / max(lin, 1) < 0.05
    return {"id": mitte, "lat": la, "lon": lo, "certainty": "B" if gut else "C", "method": text,
            "leftAnchor": links, "rightAnchor": rechts, "anchorDistance": d,
            "counterpartDifference": abs(rest), "closureResidual": rest,
            "closureQuality": "good" if gut else "conflict", "direction": -1,
            "sourceYear": jahr, "transferred": False}


# ---- 1. Stein 388 -------------------------------------------------------------------------
direkt = {}
for jahr in ("1608", "1683", "1700", "1749", "1872"):
    d1, d2 = meter(by[388], jahr), meter(by[389], jahr)
    if d1 is not None and d2 is not None:
        direkt[jahr] = berechne(jahr, 387, 388, 389, (d1, d2))
print("Stein 388, direkt berechnet:")
for j, e in direkt.items():
    print(f"  {j}: {e['certainty']} Rest {e['closureResidual']:+.1f} m, Abstand {e['anchorDistance']} m vom "
          f"{'vorherigen' if e['method'] == LINKS else 'folgenden'} Anker, {xy(e['lat'], e['lon'])[0]:.0f}/"
          f"{xy(e['lat'], e['lon'])[1]:.0f}")
quelle = min(direkt, key=lambda j: abs(direkt[j]["closureResidual"]))
print("  Quelljahr für Jahre ohne Abstandsangabe:", quelle)
for jahr in ("1569", "1608", "1683", "1700", "1749", "1872"):
    if jahr in direkt:
        neu = direkt[jahr]
    else:
        q = direkt[quelle]
        neu = dict(q, method=f"Standort desselben Steins aus Grenzgang {quelle}", sourceYear=quelle, transferred=True)
    pos["years"][jahr]["388"] = neu

# ---- 2. Stein 66 / 67 -----------------------------------------------------------------------
GPS_NEU = "N 49.60130474 E 9.62515680"
LAT, LON = 49.60130474, 9.6251568
r66 = by[66]
r66["2021 — Nr."] = "125 (vermutlich)"
r66["2021 — Fotos"] = "https://photos.app.goo.gl/EowEgbEoeHsVKfQ27"
r66["2021 — GPS"] = GPS_NEU
r66["_gps_parsed"] = {"lat": LAT, "lon": LON}
s = r66["_derived"]["survey2021"]
s.update({"number_raw": "125 (vermutlich)", "number_certainty": "vermutlich",
          "photos_url": r66["2021 — Fotos"], "gps_raw": GPS_NEU, "gps_normalized": f"{LAT}, {LON}",
          "gps": {"lat": LAT, "lon": LON}})
abstand = linie.projiziere(LAT, LON)[0]
for jahr in ("1872", "1887"):
    e = pos["years"][jahr]["66"]
    e["lat"], e["lon"], e["snapDistance"] = LAT, LON, abstand
print(f"Stein 66: neue Position, Abstand zur Grenzlinie {abstand:.1f} m")
d67, d68 = meter(by[67], "1872"), meter(by[68], "1872")
e67 = berechne("1872", 66, 67, 68, (d67, d68))
print(f"Stein 67 (1872): {e67['certainty']} Rest {e67['closureResidual']:+.1f} m, {e67['anchorDistance']} m, "
      f"Abstand zu 65 entlang der Linie: {abs(linie.projiziere(*gps(65))[1] - linie.projiziere(e67['lat'], e67['lon'])[1]):.1f} m "
      f"(bisher aus 1700: 328,5 m)")
pos["years"]["1872"]["67"] = e67

# ---- Zustand 388 ----------------------------------------------------------------------------
st = by[388]["_derived"]["status"]
st["standing_original"], st["moved_or_unknown_location"] = False, True
by[388]["_derived"]["survey2021"]["gps_status"] = "unknown_or_moved"

if SCHREIBEN:
    (ENTWURF / "data.json").write_text(json.dumps(daten, indent=2, ensure_ascii=False), encoding="utf-8", newline="")
    (ENTWURF / "standorte-positionen.json").write_text(json.dumps(pos, indent=2, ensure_ascii=False) + "\n",
                                                        encoding="utf-8", newline="")
    print("geschrieben: data.json, standorte-positionen.json")
else:
    print("Probelauf – nichts geschrieben.")
