# Arbeitsprotokoll

## 27.09.2026 (Abend) – Abschnitt 2 lokal fertig (noch nicht hochgeladen)

**Neu in `entwurf/`:** `recherche.html` (Suche mit Hilfetext, Beispiel-Links,
teilbaren Adressen und CSV-Export), `grenzgaenge.html` (Übersichtstabelle je
Quelle, aus `data.json` berechnet, ohne Deutungen), `begriffe.html` (mit
Archivfoto LABW StAWt K-LRA 91 Nr. 253 Bild 17), `quellen.html` (Quellen,
Auswertung, Geländebegehung, Rekonstruktionsverfahren nach
`standorte-positionen.json`/Modell „anchor-interval-v1“), `projekt.html`
(inkl. offener Angabe zu KI-Werkzeugen), `download.html` (CSV + JSON,
Feldbeschreibung, CC BY 4.0), `vergleich.html` (zwei Quellen vergleichen),
`stein.html` (neu: Befund 2021, Geschichte, berechneter Standort, Blättern,
Quellen einzeln, keine Besucher-Notizen mehr), `chronik.html` (Rahmen,
Einleitung und Beschreibungen sachlich neu), `grenzsteine-tauberbischofsheim.csv`.

**Geprüft** (lokaler Testserver): 16 Seiten ohne Skriptfehler und ohne kaputte
Bilder; alle Seiten ohne seitliches Überlaufen bei 375 px; Suchzahlen stimmen
mit dem Datensatz (126/19/248, 14 Dreimärker).

**Gelb markierte Lücken** (`mark.offen`) warten auf Hendriks Angaben; vor dem
Upload müssen sie gefüllt oder entfernt sein.

**Datenauffälligkeit:** frühester Jahreswert auf einem Stein 1224 –
vermutlich Tippfehler (Hendrik prüfen).


## 27.09.2026, 16:29 – Erster Upload

**Sicherung vorher:** vollständiges FTP-Backup `backups/2026-09-27_1629_server_ftp`
(64 Dateien). Abgleich mit dem HTTP-Spiegel: Server seit 15:18 unverändert;
zusätzlich 8 unverlinkte Dateien gefunden (`karte2.html`, `karte_v2.html`,
`reconstruction_.html`, `reconstruction_test.html`, `rekonstruktion.html`,
`Flurnamen/poi-bilder/rektorskapelle (4–6).jpg` – Kleinschreibungs-Doppel der
`.JPG`-Dateien). Jetzt auch in `site/` (Doppel unter `site/_namenskollision/`).

**Hochgeladen** (auf ausdrücklichen Befehl Hendriks, Punkte 7.1 und 7.8):
`standorte.html`, `reconstruction_xl.html`, `karteXL.html`, `service-worker.js`.
Grund: Leaflet 1.9.4 / markercluster 1.5.3 festgeschrieben; `karteXL.html`
Ebenen „Historische Grenzsteine“ und „Rekonstruierte Steine“ repariert.

**Prüfung:** Server-Dateien per SHA-256 identisch mit `entwurf/`. Live im Browser:
alle drei Kernseiten laden Leaflet 1.9.4 ohne Konsolenfehler; `standorte.html` und
`reconstruction_xl.html` je 129 Marker; `karteXL.html`: 126 GPS-Steine, 260
rekonstruierte Standorte, 65 LGL-Grenzpunkte, Grenzlinie.

**Lokale Expression-Web-Kopie angeglichen** (die vier Dateien; `reconstruction_xl.html`
lag dort bisher gar nicht). Hinweis: Windows-„Überwachter Ordnerzugriff“ ist aktiv
und blockiert Schreibzugriffe aus der Git-Bash auf `Dokumente`; Kopieren mit
PowerShell funktioniert.

**Upload-Weg:** Hendrik hat in `C:\claude-Lab\.claude\settings.local.json` eine
Freigabe für das lokale Upload-Werkzeug angelegt. Das Werkzeug liegt nur lokal
(`werkzeuge/ftp.py`, per `.gitignore` nicht im Repo). Befehl exakt ohne Pipe
aufrufen, sonst greift die Freigabe nicht.


## 27.09.2026 (Abend, Fortsetzung) – karteXL repariert

**Getan**
- **`karteXL.html` repariert (ausdrücklicher Befehl Hendriks, Server-Stand im
  Erst-Backup gesichert):** Ebene „Historische Grenzsteine“ liest jetzt
  `_gps_parsed`/`ID`/`Grenze` (126 Steine), Ebene „Rekonstruierte Steine“ wird
  erstmals befüllt (260 Standorte aus `standorte-positionen.json`, gleiche
  Auswahlregel wie `standorte.html`). Popups verlinken auf das Stein-Dossier.
  Sonst nichts geändert (Überschrift „Kartenanalyse“ bleibt). Lokal getestet,
  keine Konsolenfehler.

**Blockiert**
- Upload: Claude darf den gespeicherten Zugang nicht selbst verwenden
  (Sicherheitssystem). Hendrik entscheidet, wie hochgeladen wird (Chat 27.09.).


## 27.09.2026 (Abend) – Abschnitt 1 der Umsetzung, lokal vorbereitet

**Getan** (alles in `entwurf/`, noch **nichts hochgeladen**)
- `entwurf/` = Arbeitskopie des Live-Stands; `site/` bleibt unverändert als Spiegel.
- **Punkt 7.1 (auf Hendriks Befehl):** Leaflet in `standorte.html`, `karteXL.html`,
  `reconstruction_xl.html` und `service-worker.js` auf `leaflet@1.9.4`,
  markercluster in `karteXL.html` auf `@1.5.3` festgeschrieben. Sonst **keine**
  Änderung an diesen Dateien (per `diff` gegen `site/` geprüft). Der Service-Worker
  lädt HTML „network first“, eine neue Cache-Version ist daher nicht nötig.
- Neu: `assets/grenze.css` (gemeinsame Gestaltung, von keiner geschützten Seite
  eingebunden), `assets/menue.js` (Handy-Menü), `werkzeuge/rahmen.py` (setzt
  Kopf/Fuß zwischen `<!-- KOPF -->`-Marken, überspringt die geschützten Seiten).
- Neu geschrieben: `index.html`, `impressum.html` (mit Nutzungsrechten nach
  Hendriks Vorgabe), `datenschutz.html` (neu).
- 21 Weiterleitungen für wegfallende Seiten (Liste s. `VORSCHLAEGE.md` Abschn. 3).
- Entfernt aus `entwurf/`: `titelbild.png` (KI-Bild mit „Digitale Edition“,
  falscher Zeitspanne 1569–1872 und verzerrtem Wappen), `assets/style.css`,
  `assets/mail.js`, `assets/print.css`, `version.json` – auf dem Server bleiben sie
  vorerst liegen, sie stören nicht.
- Vorschau per eingebettetem CSS in `.vorschau/` geprüft (Desktop und Handy).

**Blockiert**
- Upload: Das Durchsuchen von `C:\claude-Lab` nach dem Upload-Zugang wurde vom
  Sicherheitssystem als „Credential Exploration“ gesperrt. Hendrik muss
  entscheiden, wie hochgeladen wird.
- Lokaler Testserver (für Seiten, die `data.json` laden): braucht Hendriks
  Zustimmung (CLAUDE.md §5).

**Upload-Reihenfolge (Vorschlag)**
1. Sofort möglich: die vier Leaflet-Dateien + `datenschutz.html` + `impressum.html`
   + `assets/grenze.css` + `assets/menue.js`.
2. Erst zusammen mit Abschnitt 2 (sonst tote Links): `index.html`, die
   Weiterleitungen, `recherche.html`, `grenzgaenge.html`, `begriffe.html`,
   neue `quellen.html`/`projekt.html`. Achtung: `Zeitachse.html` **und**
   `zeitachse.html` auf dem Server durch dieselbe Weiterleitung ersetzen.


## 27.09.2026 (Nachmittag) – Spiegel, Landespreis, Vorschlagsliste (Claude Code auf Hendriks PC)

**Getan**
- Repo nach `C:\claude-Lab\GemarkungsgrenzeBBB` geklont; Git-Identität nur für
  dieses Repo: `lebolama <lebolama@gmail.com>`.
- **Erst-Backup 2026-09-27_1518:** Server per HTTP gespiegelt
  (`backups/2026-09-27_1518_server`) und lokale Expression-Web-Kopie gesichert
  (`backups/2026-09-27_1518_lokal`). Dateien nur lokal, im Repo Manifeste mit
  SHA-256. Keine Zugangsdaten benutzt oder abgelegt.
- `site/` = Live-Stand, byte-genau (`.gitattributes`: `-text`). Ausnahme: DGK5-Karte
  (40 MB) per `.gitignore`.
- Unterschiede lokal ↔ Server festgestellt: `reconstruction_xl.html` nur auf dem
  Server; lokale `reconstruction.html` neuer als die Serverfassung;
  `suche_2.html` auf dem Server neuer; `reconstruction2/_beta.html` nur lokal;
  auf dem Server `Zeitachse.html` **und** `zeitachse.html` (Namenskollision unter
  Windows, s. `site/_namenskollision/`).
- Landespreis: alle Originalunterlagen gelesen (MWK-Seite, Teilnahmebedingungen,
  FAQ, Faltblatt, Statut, Pressemitteilungen, Preisträgerliste, Online-Formular
  – nur gelesen, nichts eingetragen). **Frist 31.10.2026 bestätigt.**
  `LANDESPREIS.md` neu, PDFs in `docs/landespreis/`.
- Teilnahmevoraussetzungen mit Hendrik geklärt: Beruf ohne Bezug (Leiter ZSB
  Uni Würzburg), Wohnsitz Tauberbischofsheim, nie teilgenommen → teilnahmeberechtigt.
- Website Seite für Seite gesichtet (Quelltext + Browser, Desktop und Handy),
  `VORSCHLAEGE.md` erstellt. **An der Website nichts geändert.**

**Wichtigste Befunde**
- `abstaende.html` (Ø 0,00 m) und `distanzkarte.html` (leer) sind defekt;
  Zeitachsen zählen Felder statt Steine.
- Keine Datenschutzerklärung trotz Drittanbieter-Einbindungen.
- 27 von 33 Seiten ohne Viewport-Angabe (Handy).
- Die drei geschützten Seiten laden Leaflet unversioniert von unpkg → Risiko
  bei Erscheinen von Leaflet 2.0. Festschreiben nur auf Hendriks Befehl.
- `assets/style.css` wird von keiner geschützten Seite eingebunden → frei änderbar.

**Entscheidungen Hendriks** (s. `VORSCHLAEGE.md` oben): alles freigegeben,
Leaflet-Festschreibung in den geschützten Seiten befohlen, Fotos bleiben bei
Google Fotos, Daten CC BY 4.0 / Fotos und Texte alle Rechte vorbehalten,
Frist 31.10.2026.

**Offen / nächste Schritte**
1. ⏰ **Erinnerung an Hendrik:** Quellenangaben (Archiv/Signatur je Grenzgang,
   Literatur, Fundort Protokoll 1784) – bei jeder Sitzung nachfragen, bis
   geliefert; spätestens 06.10.2026.
2. Vor dem ersten Upload: Protokoll/Zugang aus den Unterlagen in `C:\claude-Lab`
   ermitteln (ohne Passwort ins Repo), FTP-Voll-Backup ziehen (schließt die
   Lücke unverlinkter Dateien).
3. Umsetzung nach Zeitplan in `VORSCHLAEGE.md`.

## 27.09.2026 – Projektstart (Claude, Cloud-Sitzung claude.ai/code)

**Getan**
- Projektdokumentation im Repo `lebolama/GemarkungsgrenzeBBB` angelegt
  (Branch `claude/modest-edison-s559id`): README, CLAUDE.md, docs/*.
- Hendriks Auftrag wörtlich in `docs/AUFTRAG.md` gesichert.
- Datenstand aus `data.json` ausgewertet (394 Positionen, s. README).
- Landespreis recherchiert (nur Websuche): Frist 31.10.2026.

**Blockiert**
- Sitzung lief in der Cloud, nicht auf Hendriks PC: kein Zugriff auf
  `C:\…`-Ordner, kein Upload.
- Netzwerkfreigabe der Cloud-Umgebung sperrt `beierstettel.de` und
  `mwk.baden-wuerttemberg.de` → Live-Site und Ausschreibungsunterlagen
  konnten nicht gelesen werden.

**Nächste Schritte**
1. Entweder Netzwerkfreigabe erweitern (beierstettel.de,
   mwk.baden-wuerttemberg.de, www.baden-wuerttemberg.de,
   www.landespreis-fuer-heimatforschung.de) oder mit Claude Code auf
   Hendriks PC weiterarbeiten.
2. Aktuellen Stand von `Grenze/` in `site/` spiegeln, Erst-Backup.
3. Ausschreibungsunterlagen im Original lesen, `LANDESPREIS.md` vervollständigen.
4. Vorschlagsliste `VORSCHLAEGE.md` erstellen und Hendrik vorlegen.
