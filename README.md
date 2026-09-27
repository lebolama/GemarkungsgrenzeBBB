# Grenzsteine der Gemarkung Tauberbischofsheim – Website-Projekt

Arbeitsrepositorium für die Überarbeitung von **https://beierstettel.de/Grenze/**,
der Website von Hendrik (GitHub: `lebolama`) über die historischen Grenzsteine
rund um die Gemarkung Tauberbischofsheim.

> **Wer hier neu einsteigt (Mensch oder Claude):** zuerst diese Datei lesen,
> dann `CLAUDE.md` (verbindliche Arbeitsregeln), dann `docs/PROTOKOLL.md`
> (was zuletzt passiert ist und was als Nächstes ansteht).

## Projektziel

1. **Website überarbeiten:** Texte neu schreiben (keine KI-typische Sprache,
   kein „Digitale Edition“), Layout verbessern, Hilfetexte ergänzen, damit
   Besucher ohne Vorwissen verstehen, was sie auf jeder Seite tun können.
2. **Einreichung beim Landespreis für Heimatforschung Baden-Württemberg**,
   Kategorie **„Heimatforschung digital“**, mit allen geforderten Unterlagen.
   Siehe `docs/LANDESPREIS.md`. **Die Frist für die Runde 2027 endet am
   31. Oktober 2026.**

## Worum es inhaltlich geht

Die Grenze der Gemarkung Tauberbischofsheim (ca. 30,4 km) war über Jahrhunderte
mit Steinen markiert. Hendrik hat die historischen Grenzbeschreibungen
(1569/1580, 1608, 1683, 1700, 1749, Großrinderfelder Grenzbegehung 1784, 1872,
Grenzberichtigungen 1887–93) Stein für Stein ausgewertet und 2021 im Gelände
nachgesucht, fotografiert und per GPS eingemessen.

Datenstand im Repo (`data.json`, 394 Datensätze):

| Kennzahl | Wert |
|---|---|
| Datensätze (Steinpositionen) | 394 |
| 2021 gefunden | 143 |
| davon am ursprünglichen Standort | 126 |
| versetzt / Standort unklar | 19 |
| 2021 nicht gefunden | 248 |
| Dreimärker | 14 |

Nachbargemarkungen: Impfingen (84), Dittigheim (73), Dienstadt (67),
Königheim (50), Großrinderfeld (44), Hochhausen (33), Dittwar (17),
Grünsfeld (12), Grünsfeldhausen; dazu Dreimärker zwischen je zwei Nachbarn.

Pro Stein und Quelle sind erfasst: laufende Nummer, Jahreszahl, Größe, Farbe,
Zeichen (Wappen/Wappenschild, Mainzer Rad, „b“ für Bischofsheim, Kreuz oben),
Rückseite, Abstand zum Vorgänger in Ruten (fränkische Werkrute 3,65 m bzw.
neue badische Rute 3,00 m) und Metern, Freitext. Dazu 2021: Nummer, GPS, Fotos.
Das Feld `_derived` enthält daraus berechnete Werte (Präsenz je Jahr,
Symbolzählungen, Status).

## Wo die Dateien liegen

| Ort | Inhalt | Bemerkung |
|---|---|---|
| `https://beierstettel.de/Grenze/` | Live-Website | Maßgeblicher aktueller Stand |
| `C:\Users\User\Documents\My Web Sites\beierstettel\httpdocs\Grenze` | Lokale Kopie der Website (Expression Web) | Auf Hendriks PC |
| `C:\Users\User\Documents\_Taubertal\_EIGENES\Web\Grenzstein-Rekonstruktion` | Ursprünglicher Codex-Arbeitsordner | Auf Hendriks PC, Vorgeschichte |
| `C:\claude-Lab` | Zugangsdaten/Infos zu beierstettel.de (aus den Projekten Archive-App, Studienberatung-Chatbot) | **Nie ins Repo übernehmen** |
| dieses Repo `lebolama/GemarkungsgrenzeBBB` | Doku, Arbeitsstände, Backups der Textfassungen | |

**Achtung:** Der Code in diesem Repo (`reconstruction.html`, `rekonstruktion.html`,
`stein.html`, `suche.html`, `data.json`) ist ein **früher Zwischenstand**.
Die Live-Site hat deutlich mehr Seiten (u. a. `standorte.html`, `karteXL.html`,
`reconstruction_xl.html`, Recherche, Experten-Recherche). Vor jeder Arbeit
an Seiten muss der aktuelle Stand von der Live-Site bzw. aus dem lokalen
Ordner ins Repo gezogen werden (Ordner `site/`, siehe `docs/DEPLOYMENT.md`).

## Struktur dieses Repos

```
README.md              Überblick (diese Datei)
CLAUDE.md              Verbindliche Regeln für jeden Claude, der hier arbeitet
docs/AUFTRAG.md        Hendriks Originalauftrag vom 27.09.2026, vollständig
docs/STILREGELN.md     Sprach- und Textregeln für die Website
docs/DEPLOYMENT.md     Backup-, Upload- und Dokumentationsverfahren
docs/LANDESPREIS.md    Alles zum Landespreis für Heimatforschung
docs/VORSCHLAEGE.md    Verbesserungsliste für die Website (Schritt 2)
docs/PROTOKOLL.md      Laufendes Arbeitsprotokoll
docs/landespreis/      Originalunterlagen des Landespreises (PDF)
site/                  Spiegel des Live-Stands (byte-genau)
backups/               datierte Sicherungen (Dateien lokal, im Repo nur Manifeste)
```

## Fahrplan

- [x] Schritt 1: Projektdokumentation anlegen (dieses Repo)
- [x] Schritt 1b: Aktuellen Live-Stand der Website ins Repo holen (`site/`), Erst-Backup (27.09.2026)
- [x] Schritt 2: Website Seite für Seite sichten, Vorschlagsliste (`docs/VORSCHLAEGE.md`) (27.09.2026)
- [ ] Schritt 2b: Freigabe der Vorschlagsliste durch Hendrik
- [ ] Schritt 3: Texte und Layout überarbeiten (ohne die drei geschützten Seiten)
- [ ] Schritt 4: Upload mit Backup und Protokoll
- [ ] Schritt 5: Bewerbungsunterlagen Landespreis erstellen und einreichen (Frist 31.10.2026)
