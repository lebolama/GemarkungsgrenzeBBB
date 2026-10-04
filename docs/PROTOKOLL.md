# Arbeitsprotokoll

## 04.10.2026, 15:20 – Formular gegengelesen; Genauigkeitsstatistik neu gerechnet

**Beim Gegenlesen aufgefallen:** Die Statistik „118 Paare, 35 unter 5 m, 11 unter 1 m, Median 12 m,
Ausreißer über 100 m“ (berechnung.html, quellen.html, Dokumentation, Kriterienkatalog) beruhte auf
den Daten vor den Korrekturen von heute. Methode nachgebaut (aufeinanderfolgende IDs, beide
unversetzt mit GPS, beide im Grenzgang des Jahres vorhanden, Meterangabe vorhanden; Paar × Jahr;
Haversine) und auf dem Stand vom 02.10. exakt reproduziert (118 / 35 / 11 / Median 12,1 m / 13,7 %).
**Neu: 109 Paare, 36 unter 5 m, 11 unter 1 m, Median 8,7 m (12,3 %), größte Abweichung 98,5 m.**
(Minus 9 Paare: 388 ist nicht mehr „unversetzt“; 65→66 weicht jetzt nur noch 4,9 m ab.)
Texte angepasst („109“, „36“, „rund 9 Meter“, „fast 100 Meter“); Beispielzeile 65→66 in der Tabelle
durch 376→377 (1872: 72 R 7 F = 218,1 m, GPS 119,6 m, 98,5 m) ersetzt.
Neuer größter Ausreißer 376→377 (Dittigheim): 378 liegt 177 m hinter 377 (Protokoll 157 m), das
Protokoll 1749 nennt 376→378 direkt mit 335,8 m (GPS-Weg ≈ 297 m) – nicht weiter untersucht.

**Formular (`formular.md`):** Stand 04.10.; Feld „weitere Verfasser“ leer, mit Hinweis auf die im
Kriterienkatalog offengelegte Ersterfassung 2018/19 und KI-Nutzung; Hinweis: Kriterienkatalog vor dem
Hochladen ausdrucken, unterschreiben, einscannen (Datum im Dokument: 5. Oktober 2026).

Sicherung `backups/2026-10-04_1506_server_ftp`; hochgeladen und geprüft: berechnung.html,
quellen.html (live, identisch); Abgabeversion `version-20261005` neu gebaut und hochgeladen, alle
78 Dateien identisch; beide PDFs neu (12 und 3 Seiten); lokaler Ordner und `site/` angeglichen.


## 04.10.2026, 15:00 – Meterwerte korrigiert, Abgabeversion neu hochgeladen

**Korrekturen (Freigabe Hendrik; Seite 34 im Original: „51 Ruten 4 Fuß“):** Meterwerte 1872
Stein 69: 190,0 → 190,8; Stein 316: 152,2 → 154,2; Stein 365: 65,0 → 65,1 (`data.json`, CSV).
69 und 316 sind GPS-Anker, ihre Werte ändern keine berechneten Standorte; bei 365 wurde die Kette
364–367 neu gerechnet (Verschiebung 0,09 m; auch die aus 1872 übernommenen Einträge in 1569–1749).
Skript `werkzeuge/datenkorrektur_20261004b.py` (Probe: reproduziert die gespeicherten Werte auf
≤ 0,05 m). Steckbrief 74: Anmerkung „Im Original widersprechen sich Ruten und Meter …“ (nicht bei
73, auf Wunsch Hendriks). Sicherung `backups/2026-10-04_1449_server_ftp`; hochgeladen und geprüft
(4/4 identisch): data.json, standorte-positionen.json, CSV, stein.html; lokaler Ordner und `site/`
angeglichen.

**Abgabeversion `version-20261005` neu gebaut und hochgeladen** (Stand: alle Datenkorrekturen
dieses Tages; 78 Dateien, alle per SHA-256 gegen den Server geprüft, 0 Abweichungen; kein Verweis
auf `reconstruction*`, keine toten Links; `reconstruction_xl.html` dort 404). Abbildungen 1 (Startseite,
jetzt „124“) und 4 (Karte) neu aufgenommen; beide PDFs neu (Dokumentation 12 Seiten,
Kriterienkatalog 3 Seiten).

**Prüfliste vor der Abgabe damit erledigt**, bis auf: Formular gegen die endgültigen PDFs lesen;
nach dem letzten Upload nichts mehr hochladen und mit leerem Cache prüfen.


## 04.10.2026, 15:30 – Prüfliste: Meterwerte 1872 und Browser-Cache ausgewertet

**72/73 und 74 (Königheim):** Hendrik hat im Original bestätigt: Nr. 4 „Distat 8 Ruthen oder 24 Meter“
und Nr. 5 „16 Ruthen 2 Fuß oder 28 Meter 60 Centimeter“ stehen so da. Die Tabelle gibt das Original
wieder, keine Änderung. Das Original widerspricht sich bei Nr. 5 selbst (16 Ruten 2 Fuß = 48,6 m); der
GPS-Abstand 116→115 (34,5 m) spricht für die Meterangabe.

**Meterwerte 1872 (Abschrift S. 2–112 gegen `data.json`):** Alle Meterwerte der Tabelle außer sechs
kommen so in der Abschrift vor. Die früher gemeldeten „15 Abweichungen“ entstanden, weil die
Spalte „Ruthen“ der Tabelle nur ganze Ruten enthält (Fuß/Zoll fehlen) – die Meterangabe ist die des
Originals. Die sechs Ausnahmen:
- ID 57/196 (88,5) und ID 2 (100,65): stimmen mit der Abschrift überein (Suchmuster zu streng).
- ID 380 (176,1): stimmt (Original schreibt „oben“ statt „oder“).
- **ID 69 (Dittwar Nr. 17): Tabelle 190,0, Abschrift S. 85 „63 Ruthen 6 Fuß oder 190 Meter 80 Centimeter“
  → 190,8.**
- **ID 316 (Großrinderfeld Nr. 7): Tabelle 152,2, Abschrift S. 34 „51 Ruthen 4 Fuß oder 154 Meter 20
  Centimeter“ → vermutlich Zahlendreher, 154,2.**
- ID 365 (Grünsfeld Nr. 5): Tabelle 65,0; Original „21 Ruthen 7 Fuß oder (44 [durchgestrichen])“,
  also 65,1 m aus Ruten/Fuß.
Korrekturen noch nicht ausgeführt (Freigabe Hendrik).

**Browser-Cache:** Server sendet `Last-Modified` und `ETag`, aber kein `Cache-Control`/`Expires`;
Browser cachen heuristisch. Für die eingefrorene Abgabeversion unkritisch (Dateien ändern sich nach
dem Upload nicht); nach dem letzten Upload nicht mehr hochladen und mit leerem Cache prüfen.
`.htaccess` nicht angefasst.


## 04.10.2026, 14:40 – Datenkorrektur: Stein 388 versetzt, Stein 66 = Begehung 125

Entscheidungen Hendrik: 388 nach 1872 versetzt; Zuordnung ID 66 → Begehungsnummer 125 (vermutlich);
Nebenbefund (nicht im Datensatz stehende Erfassungsblätter) bleibt unkommentiert, weil die Website nur
Gemarkungsgrenzsteine zeigt (die übrigen sind Waldgrenzsteine u. a.).

**Umgesetzt mit `werkzeuge/datenkorrektur_20261004.py` (+ `geo_linie.py`):**
- Verfahren „anchor-interval-v1“ nachgebaut und an vier vorhandenen B-Einträgen auf 0,0 m genau
  bestätigt (Anker auf Grenzlinie projizieren; vom vorherigen Anker − Protokollstrecke, vom folgenden
  Anker + Protokollstrecke). Klasse B bei Schlussfehler ≤ 20 m oder < 5 % (Schwelle aus den
  Bestandsdaten abgeleitet, 109 C / 97 B).
- **Stein 388:** Zustand „versetzt“ (`standing_original` false); Standort je Grenzgang berechnet
  (1608/1683/1749/1872: B, Schlussfehler +0,2 / −7,1 / +14,8 / −2,7 m; 1569 und 1700 aus 1608
  übernommen). Steckbrief: Anmerkung, neue Zeile „Standort laut Protokoll“ (nur bei versetzten Steinen).
- **Stein 66:** neue Begehungsnummer 125 (vermutlich), GPS N 49.60130474 E 9.62515680 (0,9 m neben
  der Grenzlinie), Fotolink; **Stein 67** für 1872 neu aus Anker 66 berechnet (B, 343 m ab Stein 65,
  bisher 329 m aus 1700). Anmerkung im Steckbrief 66 (126er = Zusatzstein ohne Protokollbezug).
- Zahlen: **124** statt 125 Steine am ursprünglichen Platz, 20 statt 19 versetzt (index, grenzgaenge,
  quellen, chronik, Dokumentation + PDF neu, 12 Seiten).
- Lokal getestet: Steckbriefe 66/67/387/388/195, geschützte `standorte.html` lädt ohne Fehler, weiter
  329 Marker (Ebene 1872); geschützte Seiten selbst unverändert, nur die gemeinsam genutzten
  Datendateien geändert (ausdrückliche Anweisung).
- Sicherung `backups/2026-10-04_1424_server_ftp` (190 Dateien) vor dem Upload; hochgeladen und
  geprüft (8/8 identisch): data.json, standorte-positionen.json, CSV, stein.html, grenzgaenge.html,
  quellen.html, index.html, chronik.html; lokaler Ordner und `site/` angeglichen.

**Zu Stein 72/73:** Hendrik fand die Stelle im Original nicht. Antwort: Die Seitenmarke „Seite 89“
stammt aus seiner eigenen Transkription (Marke „-Seite 89-“, Sprungmarke #seite-89 auf
transkription-1872.html); Eintrag „4.)“ im Abschnitt Königheim („1.) Dreimärker Dittwar, Königheim und
Bischofsheim im Wiesenbach“ beginnt auf Seite 88). Gegenlesen steht aus.

**Noch offen:** Abgabeversion `version-20261005` neu bauen/hochladen (Stand vor dieser Korrektur),
15 Meterwerte 1872, Browser-Cache, Formular gegen endgültige PDFs lesen.


## 04.10.2026, 14:05 – Prüfliste: Stein 195 angepasst; Befunde zu 387–389, 65/66, 72/73

**Umgesetzt (Freigabe Hendrik):** Stein 195: „(evtl.)“ bei der Begehungsnummer 63 gestrichen
(`data.json`: `2021 — Nr.`, `number_raw`, `number_certainty` = sicher; CSV) und Anmerkung im
Steckbrief (`stein.html`, Weg 194→195 über die Steine 64–66 ≈ 120 m, Luftlinie 84 m, Protokolle
124–131 m). Lokal getestet (375 px), hochgeladen: data.json, grenzsteine-tauberbischofsheim.csv,
stein.html – 3/3 identisch; lokaler Ordner und `site/` angeglichen. **Die Abgabeversion
`version-20261005` ist damit nicht mehr auf dem Stand von `entwurf/`** – vor der Abgabe neu bauen
und hochladen (`stichtag.py`, `ftp.py stichtag`), sobald alle Datenentscheidungen gefallen sind.

**Zwischenfall Sicherung:** `ftp.py sichern` brach nach ~175 Dateien mit Verbindungsabbruch ab
(Server beendet lange Sitzungen, seit die Abgabeversion mitgesichert wird). Weil der Befehl mit
`| tail` verkettet war, lief der Upload trotzdem; die drei Dateien waren vorher gesichert
(`backups/2026-10-04_1356_server_ftp`, unvollständig). `ftp.py` verbindet jetzt bei Abbruch neu und
wiederholt; vollständige Sicherung danach: `backups/2026-10-04_1359_server_ftp` (190 Dateien).
**Künftig `sichern` nie mit Pipe verketten.**

**Befunde (nichts geändert):**
- **387→388→389:** Hendrik: alle drei Originalsteine, 388 vermutlich nach 1872 versetzt (geringfügig
  durch Wegasphaltierung?). Summe 387→389 stimmt (404 vs. 401 m); 388 steht ~63 m zu weit.
  Vorschlag: 388 als „versetzt“ führen (nur 388 selbst wird dann berechnet, 387/389 bleiben Anker).
- **65→66:** Entlang der Feldsteine ab 127: 126 bei 67,6 m, **125 bei 173,1 m** (Protokoll Nr. 14:
  168 m), 124 bei 219 m, Lücke bis 123 bei 421,7 m (Nr. 15 bei 338,7 m: **verschwunden**), 122 bei
  509,5 m (Nr. 16: 518,7 m), 119 bei 686,4 m (Nr. 17: 708,7 m). Damit ist Nr. 14 = Feldnr. **125**
  (hochformatiger, hellgrauer Stein mit Rad/B, „DW“ – passt zu „weißer Stein, viereckig, DW“ 1887),
  Feldnr. 126 (niedriger, rotbrauner Stein mit Rad, „69“, „DW“) ist ein Zusatzstein. Umbuchung
  ID 66 → Feldnr. 125 würde Anker und berechnete Positionen (66, 67) ändern – nur mit Freigabe.
- **72→73:** Hendrik: Feldnr. 117 viereckig, rot, Zahl „56 1/2“ (Erfassung sagt „GK 36 1/2“) –
  passt zu Nr. 3 („rother viereckiger Stein“); der Abstand 8 Ruten = 24 m (Nr. 3→4) bleibt gegen
  GPS 70,4 m unerklärt. Original (Seite 89 der Abschrift 1872) gegenlesen.


## 04.10.2026 – Prüfliste: auffällige Steinpaare ausgewertet (Entscheidungen Hendriks stehen aus)

Grundlage: `data.json`, Transkription 1872 und Hendriks Erfassung 2017–21
(`…\_gisTBB\Grenzsteine\Erfassung aller Grenzsteine …pdf`, 238 Blätter, „Interne Nummer“ = Feldnummer).

- **194→195 (Hochhausen):** Zwischen Feldnr. 67 (ID 194) und 63 (ID 195) stehen drei weitere Steine
  (Feldnr. 66, 65, 64; Inschrift „GHH 7/6/5“, ohne Jahr), die nicht in `data.json` sind. Weg über
  sie: 25,0 + 51,4 + 29,7 + 14,3 = 120,4 m (Protokolle 124–131 m; Luftlinie 84,0 m). Kein
  Datenfehler, die Grenze knickt. Vorschlag: Anmerkung im Steckbrief 195.
- **387→388→389 (Dittigheim):** Protokoll 166,5 / 237,9 m (1872), GPS 229,7 / 171,7 m; Summe
  stimmt (404 vs. 401 m). 387 und 389 passen, Feldnr. 156 (ID 388) liegt ~63 m zu weit.
- **65→66 (Dittwar):** Protokoll 56 Ruten = 168 m, GPS 67,6 m. Feldnr. 125 liegt 173,1 m von 127
  (ID 65) entfernt und passt zum Protokoll; Feldnr. 126 (ID 66, „unsicher“) ist vermutlich ein
  anderer (Zwischen-)Stein. Betrifft Anker der Berechnung, daher nur mit Freigabe ändern.
- **72→73 (Königheim):** Protokoll Nr. 3→4 = 8 Ruten = 24 m, GPS 70,4 m. Feldnr. 117 trägt
  „GK 36½“ (nachträglich eingeschoben), 116 „G37K“; 116→115 passt (34,5 vs. 28,6 m), 117 sitzt
  ca. dort, wo Nr. 2 stehen müsste. Dreimärker 118 wurde 1887 versetzt.
- **Nebenbefund:** 108 der 238 Erfassungsblätter (96 ohne Jahreszahl, 12 mit) sind nicht im
  Datensatz (vermutlich jüngere Steine, nicht in den Protokollen).


## 02.10.2026, 13:50 – Entscheidungen Hendrik: laufende Seite, Kapitel 8, Abbildung 4

1. **Laufende Website:** `reconstruction_xl.html` bleibt dort unverändert (kein Entfernen). Die
   Dokumentation nennt weiter Stichtagslink und „laufende Fassung“.
2. **Dokumentation Kap. 8:** „… das zeigen zwei Funde bei zehn gesuchten Steinen.“
3. **Abbildung 4 neu:** Karte der Grenzsteine mit eingeschalteter Ebene „Grenzgang 1872“ (grün A,
   orange B, rot C = berechnete Standorte). Aufgenommen mit Edge headless aus einer Scratchpad-Kopie
   der Abgabeversion, in der ein Skript die Ebene automatisch einschaltet (Seite im Repo und auf dem
   Server unberührt, kein Upload). Bildunterschrift angepasst. Dokumentation weiter 12 Seiten.

Offen für morgen: Prüfliste vor der Abgabe (ungerade Steinpaare, 15 Meterwerte 1872), Formular
gegen die endgültigen PDFs lesen, Abgabeversion bei Änderungen an `entwurf/` neu bauen (05.10.).


## 02.10.2026, 13:10 – Kriterienkatalog überarbeitet

Wünsche Hendrik umgesetzt: Kopfblock jetzt linksbündig (der Blocksatz zog die Zeile „Form“
auseinander), „(Stichtagsfassung: …)“ in eigener Zeile; Verfasser mit vollständiger Adresse und
eigene Zeile E-Mail; Kategorie „Heimatforschung digital (Einreichung 2026)“; Hilfsmittel für
Ersterfassung, systematische Begehungen und Einmessung als eine verbundene Zelle (Geräte, Apps,
Karten, Werkzeuge); Hilfsmittel „Suche im Gelände“ neu; vier Zeilen Platz für die handschriftliche
Unterschrift. Zusätzlich angeglichen: „zehn verschollene Steine gesucht, zwei wiedergefunden“.
`werkzeuge/dokumentation_pdf.py` kann jetzt harte Zeilenumbrüche (zwei Leerzeichen am Zeilenende),
verbundene Tabellenzellen (`{rs=N}`, `~`) und `[Unterschrift]`. PDF: 3 Seiten.


## 02.10.2026, 12:30 – Abgabeversion `version-20261005` online, Dokumentation überarbeitet

**Abgabeversion (Stichtagsfassung):** https://beierstettel.de/Grenze/version-20261005/ – Kopie der
aktuellen Website ohne die Seite `reconstruction_xl.html` („Verschwundene Steine“; alles darauf
steht auch auf `standorte.html`). Gebaut mit dem neuen `werkzeuge/stichtag.py` aus `entwurf/`:
Menüpunkt, Startseitenkarte und alle Verweise entfernt (berechnung.html, datenschutz.html, CSS-
Kommentar), Startseitenkarte „Karte der Grenzsteine“ nennt jetzt die berechneten Standorte.
Weiterleitungsseiten für alte Adressen entfallen bis auf `karte.html` und `suche.html`, weil die
geschützte `karteXL.html` darauf verlinkt. Ergebnis: 23 Seiten, 78 Dateien, 60 MB; kein Verweis auf
`reconstruction*` in HTML/JS/CSS/JSON, keine toten Links oder Anker. `standorte.html` und
`karteXL.html` byte-identisch kopiert. Hochgeladen mit neuem `ftp.py stichtag NAME` (nur in das neue
Unterverzeichnis; Sicherung vorher: `backups/2026-10-02_1219_server_ftp`); alle 78 Dateien per
SHA-256 gegen den Server geprüft, 0 Abweichungen. `version-20261005/reconstruction_xl.html` → 404,
laufende `reconstruction_xl.html` → 200 (unverändert). Ordner `stichtag/` steht in `.gitignore`
(reproduzierbar mit `stichtag.py`, Stand `entwurf/` zum Zeitpunkt des Commits).

**Dokumentation (jetzt 12 Seiten, vorher 13):** Untertitel „… Rekonstruktion der ehemaligen
Standorte verschwundener Grenzsteine aus historischen Grenzgangprotokollen“ (auch im Formular);
Titelblatt mit Adresse Mörikeweg 6 und Datum 5. Oktober 2026; Link zur Stichtagsfassung; Kennzahl
„2 Steine von 10 gesuchten (erste Stichprobe zur Validierung der Methodik)“; „Die Bewährung“ um
Hendriks Absatz zur Erfolgsquote 20 % ergänzt; Zeile „Verschwundene Steine“ und Abb. 4 gestrichen,
Abbildungen neu nummeriert (jetzt 1–6), Karten-Zeile nennt die berechneten Standorte;
Wikipedia-Eintrag mit URL. Abbildungen 1, 3, 5, 6 neu aus der Abgabeversion aufgenommen (Menü ohne
„Verschwundene Steine“). **Kriterienkatalog:** Stichtagslink, Datum 5. Oktober 2026, „23 Seiten,
394 Steckbriefe, 2 interaktive Karten“. **Formular:** Seitenzahl 12, Stichtagslink eingetragen.

**Offen / Hinweise:** Die laufende Website (`/Grenze/`) hat `reconstruction_xl.html` und den Menüpunkt
weiter; die Dokumentation nennt sie als „laufende Fassung“ – Entscheidung Hendrik. Stand
`entwurf/` ändert sich noch? Dann vor dem 05.10. `stichtag.py` und `ftp.py stichtag` erneut laufen
lassen und die Abbildungen prüfen. Prüfliste vor Abgabe (ungerade Steinpaare, 15 Meterwerte 1872)
steht noch aus. Dokumentation Kap. 8 „das haben zwei Funde bestätigt“ ist bei 2 von 10 vorsichtiger
zu formulieren (Vorschlag an Hendrik).


## 28.09.2026, 23:05 – Projektseite: Lumi, Kobe und die Ziegenböcke

Wunsch Hendrik. `projekt.html`: Lumi (Hündin, 2010–2024) bei der ersten Umgehung 2017 mit Namen
und kurzer Geschichte (blieb vor Grenzsteinen stehen, bis sie gelobt wurde; hat wohl keinen
unbekannten Stein neu entdeckt). Bei der Suche mit der berechneten Karte: heute Hund Kobe, auf
manchen Strecken die Ziegenböcke Freddy und Siggi. Klärung: „um 2005 mit meinem Hund“ meint
Scooby (bis 2010) und bleibt.

Hochgeladen (Sicherung `backups/2026-09-28_2303_server_ftp`): projekt.html – identisch; lokaler
Ordner und `site/` angeglichen.


## 28.09.2026, 22:57 – Kriterienkatalog-PDF nachträglich erzeugt, PDF-Werkzeug abgesichert

Hendrik bemerkte, dass die Kriterienkatalog-PDF noch der Stand von 17:00 war. Ursache: Beim
direkten Nacheinander zweier Aufrufe dockt der zweite Edge an die noch laufende Instanz mit
demselben Profil an und beendet sich ohne Ausgabe; das Skript meldete die Größe der alten Datei.
`werkzeuge/dokumentation_pdf.py` löscht jetzt die alte PDF vorher, wartet auf die neue, versucht
es bis zu dreimal und bricht sonst mit Fehler ab. Beide PDFs neu erzeugt und inhaltlich geprüft
(Kriterienkatalog 3 Seiten mit Ersterfassung, ohne „ohne KI“; Dokumentation 13 Seiten, GPS-Satz
„2 Meter genau oder besser“).


## 28.09.2026, 23:00 – GPS-Formulierung eindeutig, „ohne KI“ gestrichen

Wunsch Hendrik: GPS jetzt „in der Regel auf 2 Meter genau oder besser“ (`dokumentation.md`,
`quellen.html`). Kriterienkatalog, Zeile „Zuordnung der Steine“: Hilfsmittel „ohne KI“ durch „–“
ersetzt. Beide PDFs neu. Hochgeladen (Sicherung `backups/2026-09-28_2252_server_ftp`):
quellen.html – identisch; lokaler Ordner und `site/` angeglichen.


## 28.09.2026, 22:52 – GPS-Genauigkeit: „mindestens“ statt „höchstens“

Korrektur Hendrik: Der Garmin GPSMAP 65s misst im Wald „auf mindestens 2 Meter genau“. Geändert in
`dokumentation.md` (PDF neu) und `quellen.html`. Hochgeladen (Sicherung
`backups/2026-09-28_2250_server_ftp`): quellen.html – identisch; lokaler Ordner und `site/`
angeglichen.


## 28.09.2026, 22:45 – Ersterfassung 2018/19 und Kulturlandschaftspreis 2019 offengelegt

Hinweis Hendrik: Seine Söhne Jonne und Matti und ihr Freund Phil Engert (damals 7, 10, 11 Jahre)
erhielten 2019 den Sonderpreis Kleindenkmale des Kulturlandschaftspreises (Schwäbischer
Heimatbund) für die gemeinsame Ersterfassung der Steine (Spätherbst 2018 bis Mai 2019) und die
Freilegung des Grünsfelder Wegs; Hendrik hatte sie vorgeschlagen. Quelle: „Erfassung aller
Grenzsteine der Gemarkung Tauberbischofsheim (Beierstettel, 2017-21).pdf“. Die Ersterfassung
blieb lückenhaft; die drei vollständigen Umgehungen (27.12.2017, 5.4.2019, 14.5.2021) und alle
späteren systematischen Begehungen hat Hendrik allein gemacht (mit Hund Lumi). Alle Fotos der
Website sind von ihm.

Teilnahme: unschädlich. FAQ 2027: ausgeschlossen ist nur, wer schon einen Landespreis für
Heimatforschung erhalten hat.

Geändert: `dokumentation.md` Kap. 4 (Vorgeschichte, Namen, Preis, Daten der Umgehungen),
`kriterienkatalog.md` (Eigenleistung „bis auf eine Ausnahme allein“, eigene Zeile Ersterfassung,
Hinweis auf den Preis der Kinder), beide PDFs neu (13 und 3 Seiten). `projekt.html`: neuer
Absatz zur Vorgeschichte, online ohne Namen („meine beiden Söhne und ein Freund“).

Hochgeladen (Sicherung `backups/2026-09-28_2242_server_ftp`): projekt.html – identisch; lokaler
Ordner und `site/` angeglichen.

Offen: `projekt.html` sagt „Angefangen hat es um 2005 mit … meinem Hund“; im Vorschlagsschreiben
2019 steht, Lumi kam „vor 9 Jahren“ (≈ 2010). Mit Hendrik klären.


## 28.09.2026, 21:58 – Voller Wortlaut statt Kurzfassung in den gekürzten Abschriften

Entscheidung Hendrik: Wo die PDF-Kommentare den ausführlichen Text eines Steins enthalten, ersetzt
dieser die Kurzfassung aus der Excel-Spalte „sonstiges“. `werkzeuge/erfassung_seiten.py` liest dazu
die nummerierten Kommentare aus „Büschemer Gemarkungsumgehungen.pdf“ (1569: S. 1–20, Abschrift 1580:
S. 21–48; „8.) & 9.)“ gilt für beide Nummern; Randvermerk „wegen großen Rinderfeldt“ vor Stein 70
abgetrennt). Ergebnis: 40 Steine auf `erfassung-1569.html` im vollen Wortlaut. 1608 nur Nr. 1, weil
die Kommentarnummer „18.)“ zu einem anderen Stein gehört als Nr. 18 der Tabelle. 1700 und 1749:
keine Kommentare, unverändert.

Hochgeladen (Sicherung `backups/2026-09-28_2157_server_ftp`): erfassung-1569, erfassung-1608 –
2/2 identisch; lokaler Ordner und `site/` angeglichen.


## 28.09.2026, 21:47 – Gekürzte Abschriften 1569/1580, 1608, 1700, 1749

Vollständige Transkriptionen der übrigen Bücher liegen auf einer externen Festplatte (Hendrik sucht).
Bis dahin (Hendriks Vorgabe): neue Seiten `erfassung-1569.html` (auch für die Abschrift 1580),
`erfassung-1608.html`, `erfassung-1700.html`, `erfassung-1749.html`, erzeugt mit
`werkzeuge/erfassung_seiten.py` aus `data.json` (= Excel „Grenzsteine BBB (alle Grenzgänge).xlsx“):
je Stein Nr., Zeichen, Abstand, Lage/Bemerkung; oben ein Hinweis, dass Randpassagen (Namen der
Begleiter usw.) fehlen, mit Verweis auf die vollständigen Abschriften 1683/1872. Randbemerkungen aus
den PDF-Kommentaren der Sammeldatei ergänzt: Anfang 1569, Begleiterwechsel „wegen großen
Rinderfeldt“ (1580), Anfang 1608, Nachtrag zu Nr. 18 (1608). Linktext auf protokolle.html:
„Abschrift (gekürzt)“. 1724: noch keine Abschrift.

Hinweis an Hendrik: Die PDF-Kommentare enthalten für 1569 Nr. 1–22 und 1580 Nr. 59–76 deutlich
ausführlichere Wortlaut-Abschriften als die Excel-Spalte „sonstiges“ (dort teils zusammengefasst).

Hochgeladen (Sicherung `backups/2026-09-28_2147_server_ftp`): 4 Erfassungsseiten, protokolle – 5/5
identisch; lokaler Ordner und `site/` angeglichen.


## 28.09.2026, 20:14 – Messweise 1872 auf „So wird gerechnet“

Zitat aus dem Vorbericht 1872 („auf den Boden so wie derselbe beschaffen ist …“) als Beleg für
längere Protokollstrecken am Hang eingebaut, **ausdrücklich nur für 1872** (Hinweis Hendrik: für
frühere Grenzgänge nicht überliefert); verlinkt auf transkription-1872.html.
Hochgeladen (Sicherung `backups/2026-09-28_2014_server_ftp`): berechnung – identisch.


## 28.09.2026, 20:09 – Transkriptionen auf der Website, zehnter Upload

**Bestandsaufnahme der Transkriptionen** (Quellordner F:\…\Büschemer Gemarkungsumgehungsbücher\PDF):

| Protokoll | Vollständige Abschrift | PDF-Kommentare in „Büschemer Gemarkungsumgehungen.pdf“ |
|---|---|---|
| 1569 | – | 6 von 20 Seiten, 23 Kommentare, 4 600 Zeichen |
| 1580 (Abschrift) | – | 4 von 28 Seiten, 18 Kommentare, 2 700 Zeichen |
| 1608 | – (docx nur Überschrift) | 3 von 29 Seiten, 618 Zeichen |
| 1683 | **ja** (Transkript pdf/odt/rtf, 108 Steine) | 39 von 47 Seiten |
| 1700 | – | keine |
| 1724 | – | keine |
| 1749 | – | keine |
| 1872 + 1887–93 | **ja** (Transkript pdf/rtf, 239 Seitenmarken) | 226 von 246 Seiten |

Für 1569, 1580, 1608, 1700, 1724 und 1749 gibt es außerdem nur die Steinbeschreibungen in den
Excel-Tabellen (ohne Zwischentexte). Hendrik sucht die fehlenden Transkriptionen.

**Neu:** `werkzeuge/transkription_seiten.py` erzeugt `transkription-1683.html` und
`transkription-1872.html` (Zeilenumbrüche wie im Original, Seitenmarken als Sprungziele,
Anmerkungen [ ] und unsichere Lesungen (?) hervorgehoben). Auf `protokolle.html` sind Einband und
Textlink „Transkription“ für 1683 und 1872 verlinkt. `grenze.css`: Silbentrennung in
Überschriften (langes „Gemarkungsumgehungsbuch“ lief auf dem Handy über).

**Fund für „So wird gerechnet“:** Vorbericht 1872, Punkt 3: Die Messlatten wurden „auf den Boden
so wie derselbe beschaffen ist“ gelegt, nur über Dämme und Gräben waagrecht gemessen – Beleg aus
der Quelle, warum Protokollabstände am Hang länger sind als GPS-Strecken. Noch einzubauen.

Hochgeladen (Sicherung `backups/2026-09-28_2009_server_ftp`): grenze.css, transkription-1683,
transkription-1872, protokolle – 4/4 identisch; lokaler Ordner und `site/` angeglichen.


## 28.09.2026, abends – Bewerbungsunterlagen, Abschnitte 1 und 2 (Entwurf)

- `docs/bewerbung/formular.md`: alle Felder des Online-Formulars (langer Titel, Ausbildung
  Diplom-Psychologe JMU 2002). Telefon und Geburtsdatum bewusst nicht im Repo.
- `docs/bewerbung/kriterienkatalog.md` (+ PDF, 3 Seiten): Intention, Eigenleistungstabelle,
  Bewertungskriterien. Zeile „Inhalte und Texte“ auf Hendriks Wunsch gestrichen; stattdessen der
  zutreffende Satz „Alle Inhalte stammen von mir; geprüft und verantwortet“. Keine ausdrückliche
  Behauptung, alle Texte seien allein formuliert.
- `docs/bewerbung/dokumentation.md` (+ PDF, 13 Seiten, 1,5 MB): 10 Kapitel mit 7 Screenshots und
  vollständigem Quellen- und Literaturverzeichnis.
- Werkzeug `werkzeuge/dokumentation_pdf.py`: Markdown → HTML → PDF mit Edge headless
  (Erlaubnis Hendriks 28.09.2026, in CLAUDE.md eingetragen). Screenshots unter
  `docs/bewerbung/abbildungen/`.
- Offen: Datum und Link der Stichtagsfassung (✏️), Seitenzahl im Formular (13),
  Abschnitt 3 (eingefrorene Stichtagsfassung), Prüfliste vor Abgabe (LANDESPREIS.md).


## 28.09.2026, 15:57 – Leuchtenberg-Indiz bestätigt, neunter Upload

- Hendrik bestätigt das Leuchtenberg-Indiz, mit Einschränkung: Wappen konnten nachgearbeitet
  werden (Beispiel: Fürstenhaus Leiningen ließ 1803–1806 auf Waldgrenzsteinen im ehemals
  kurmainzischen Forst „FL“ über „CM“ hauen). In protokolle.html und Anmerkung zu Stein 369
  ergänzt.
- Abschrift 1608 auf der Protokollseite beginnt jetzt „Von dannen nechst …“ (Hendrik bestätigt).
  Hinweis: Im Datensatz (`data.json`, 1608 — sonstiges, Stein 369) steht weiterhin „von diesem
  nechst“ – nicht geändert, da von den geschützten Seiten gelesen.

Hochgeladen (Sicherung `backups/2026-09-28_1557_server_ftp`): protokolle, stein – 2/2 identisch.


## 28.09.2026, 15:50 – Ich-Form, Seite „Die Protokolle“, achter Upload

- **Erzählperspektive (Entscheidung Hendrik):** „Über das Projekt“ in Ich-Form, unterschrieben;
  Sachseiten unpersönlich (grenzgaenge, quellen, chronik, download). Name bleibt nur als
  Urheberangabe (Fotos, Impressum, Zitierweise, Fuß).
- Projektseite neu: Abschnitt „Die Arbeit an den Protokollen“ (Kurrentschrift selbst erlernt,
  > 2 Wochen je 3–4 h pro Protokoll, anfangs bis 1 h pro Stein; alles von Hand transkribiert,
  Transkribus nur in seltenen Zweifelsfällen, kaum hilfreich).
- **Neu: `protokolle.html`** – Aufwand in Zahlen (9 Grenzbeschreibungen, 497 fotografierte
  Protokollseiten + 400 Seiten Landschiederbücher, 62 Seiten Abschrift 1872, 394 Positionen);
  „Ein Stein durch drei Jahrhunderte“: der „1308er“ (Stein 369) 1608 / 1683 / 1872 als Original
  (Ausschnitte aus Hendriks PDF „Besondere Grenzsteine“) neben Hendriks Abschrift (1683 und 1872
  aus den Transkripten, 1608 aus der Tabelle „Gemarkungsumgehungen 1580-1749.xlsx“); Bücherregal
  mit 8 Titelseiten und Signaturen. Im Menü, auf Start, in Quellen, Projekt und Stein 369 verlinkt.
- **Neues Indiz zum „1308er“:** 1608/1683 „leuchtenbergisch Wappen“ auf der Grünsfelder Seite;
  Grünsfeld kam erst 1502/03 an Leuchtenberg (Wikipedia „Grünsfeld“), 1308 Rieneck → spricht für
  1508. Auf protokolle.html und in der Anmerkung zu Stein 369 – **von Hendrik bestätigen lassen.**
- Genehmigungen der Archive zur Veröffentlichung der Abbildungen liegen laut Hendrik vor.
- Prüfliste: wiedergefundene Steine erledigt (laut Hendrik von Codex bereits im Datensatz).

Hochgeladen (Sicherung `backups/2026-09-28_1550_server_ftp`): 11 Bilder, protokolle und alle
14 übrigen Rahmenseiten – 26/26 identisch; lokaler Ordner und `site/` angeglichen.


## 28.09.2026, 15:19 – Nachträge Hendrik, siebter Upload

- `projekt.html`: „sowie bei Textentwürfen für die Website“ gestrichen (Wunsch Hendriks; Claude hat
  auf das Risiko bei der Eigenleistungserklärung hingewiesen, s. Chat).
- Begehungen 2017–2021 präzisiert: drei vollständige Umgehungen + zahlreiche Teilbegehungen,
  Steine behutsam gereinigt; Begehungen laufen weiter (projekt, quellen).
- Historische Grenzgänge: abschnittsweise, Feldschieder beider Nachbarorte, bei Streit neutrale
  Feldschieder einer dritten Gemeinde (begriffe).
- **Zwei Steine mit der Karte wiedergefunden** (± ca. 2,5 m vorhergesagt): Fahrentalgraben
  (Steilhang) und Wald bei den ehem. Dienstadter Weinbergen; beide umgestürzt knapp unter der
  Oberfläche, wieder aufgerichtet. Allgemein eingearbeitet (projekt, berechnung „Bewährt im
  Gelände“). **Stein-IDs, GPS, Fotos fehlen noch** → Datensatz noch nicht aktualisiert.
- Ausreißer > 100 m als möglicher Hinweis auf unbekannte Grenzänderung (berechnung).
- **Meterwerte 1872/1887–93 geklärt:** Hendriks Sorge (2,97 m) unbegründet. Die Meter enthalten
  Ruten + Fuß + Zoll (1 Rute = 10 Fuß = 3,00 m; 1 Fuß = 10 Zoll). 181 von 196 Meterwerten 1872
  stimmen exakt mit „Distat … Ruthen … Fuß … Zoll“ der Transkription überein; die Rutenspalte
  enthält nur ganze Ruten. **Datensatz nicht geändert.** Texte (quellen, begriffe, download,
  berechnung) entsprechend präzisiert; Beispiel zitiert „Distat 17 Ruthen 8 Fuß oder 53 Meter 40
  Centimeter“.
- Neuer Quellbestand freigegeben: `F:\User\Dokumente2\Tauberfranken\_Büscheme\Büschemer
  Gemarkungsumgehungsbücher` (3,2 GB; Fotos aller Seiten, PDFs, Transkriptionen 1608/1683/1872,
  Protokoll 1724, Landschieder-Tagebücher 1860–1919). Transkribus-XML dort ohne Textzeilen.

Hochgeladen (Sicherung `backups/2026-09-28_1519_server_ftp`): projekt, quellen, begriffe, download,
berechnung – 5/5 identisch; lokaler Ordner und `site/` angeglichen.


## 28.09.2026, 14:50 – Erklärseite „So wird gerechnet“, sechster Upload

**Neu: `berechnung.html`** (Wunsch f, von Hendrik freigegeben): Idee, sieben Schritte (nach
Hendriks Mail an Dr. Himmelsbach), Rechenbeispiel Grenzgang 1872, Stein 367 → 368 → 369 („1308er“)
→ 370 mit SVG-Skizze (Summe Protokoll 226,7 m, entlang der Grenzlinie gemessen 234,2 m,
Unterschied 7,5 m = 3 %), Genauigkeitsprüfung, Sicherheitsklassen, Grenzen der Methode,
Aufruf zum Mitsuchen. Im Menü („So wird gerechnet“), auf der Startseite, in Quellen und Begriffe
verlinkt. Skizze auf dem Handy seitlich wischbar (Schrift sonst 6 px).

**Genauigkeitsprüfung (neu ausgewertet, 118 direkt benachbarte Paare unversetzter Steine):**
Median der Abweichung Protokoll ↔ GPS 12,1 m (13,7 %); 35 Paare ≤ 5 m, 11 ≤ 1 m; Ausreißer bis
>100 m, teils in allen Jahrgängen gleich (z. B. 194→195, 387→389). Die frühere Formulierung
„stimmen erstaunlich gut überein“ in `quellen.html` wurde durch diese Zahlen ersetzt.

**Hochgeladen** (Sicherung `backups/2026-09-28_1450_server_ftp`): berechnung und die 13 übrigen
Rahmenseiten (neuer Menüpunkt) – 14/14 identisch. Lokaler Ordner und `site/` angeglichen.

**Rückfragen an Hendrik:**
1. Meterwerte 1872/1887–93: z. B. 18 Ruten = 53,4 m, 25 Ruten = 75,6 m – nicht genau × 3,00 m.
   Stehen die Meter so im Protokoll (dann „laut Protokoll“) oder wurden sie umgerechnet?
   Texte in Begriffe/Quellen/Daten sprechen derzeit von „umgerechnet mit 3,00 m“.
2. Auffällige Paare prüfen: 194→195 (alle Jahrgänge ca. 124–128 m laut Protokoll, GPS 84 m),
   387→388→389, 65→66 (1872), 72→73 – Zuordnung, Versetzung oder Zwischensteine?


## 28.09.2026, 14:42 – Artikelbilder, Stein 369 im Datensatz korrigiert, fünfter Upload

**Artikelseite:** alle 19 Abbildungen der sieben Artikel übernommen, mit den Quellenangaben
aus den Artikeln (Staatsarchive Wertheim und Würzburg, Archiv Tauberfränkische Heimatfreunde,
OpenStreetMap, Fotos H. Beierstettel). Freigabe Hendriks: Archivkarten mit Quellenangabe,
Heimatfreunde-Material als Mitglied, alle übrigen Fotos von ihm. Hufeisen-Foto (Art. 07):
Gesicht des Kindes (Hendriks Sohn) verpixelt.

**Stein 369 („1308er“) – auf ausdrücklichen Befehl Hendriks, Backup vorher:**
- `data.json`: 2021-Felder und `_gps_parsed` geleert, `_derived.survey2021`/`status` wie bei
  nicht gefundenen Steinen, `presence_by_year.2021 = false`. Die Begehungsdaten des Ersatzsteins
  (Nr. 187.2, GPS, Fotos) stehen im neuen Feld `_befund_2021_anderer_stein`. Diff geprüft: nur
  Stein 369 geändert.
- `standorte-positionen.json`: 6 Einträge für 369 von Klasse A auf B („Standort aus dem GPS-Punkt
  eines anderen Steins im Umkreis von ca. 2 m übernommen“).
- Neue Kennzahlen: 142 gefunden (vorher 143), 125 am ursprünglichen Platz (126), 19 versetzt,
  249 ohne Fund (248). Angepasst in index, chronik, grenzgaenge, projekt, quellen; CSV neu.
- Test lokal: standorte.html 128 Marker (vorher 129), reconstruction_xl.html 128, karteXL.html
  125 GPS + 261 rekonstruiert; keine Konsolenfehler. Hinweis: Browser mit altem Cache zeigen
  bis zum Ablauf die alte data.json (keine Cache-Steuerung auf dem Server).

**Hochgeladen** (Sicherung `backups/2026-09-28_1442_server_ftp`): 15 Artikelbilder, artikel,
data.json, standorte-positionen.json, CSV, index, chronik, grenzgaenge, projekt, quellen, stein –
25/25 identisch. Lokaler Ordner und `site/` angeglichen.

**Als Nächstes:** Erklärseite „So werden verschwundene Steine berechnet“ (von Hendrik freigegeben).


## 28.09.2026, 14:27 – Artikelseite, Begriffe vervollständigt, vierter Upload

**Antworten Hendriks eingearbeitet:**
- Henkerslehen: westliche Grenze = Gemarkungsgrenze zu Großrinderfeld; ein 1490er-Stein dort
  wurde bei manchen Begehungen als Gemarkungsgrenzstein anerkannt.
- Archivfoto = Stein 94 bestätigt.
- Kreuz oben (Deutung nicht überliefert; vermutlich von Findlingen übernommen, später durch
  Richtungslinien ersetzt), rot = Buntsandstein, weiß = Kalkstein, Zahl in der b-Spalte =
  Anzahl der „b“, „GB“/„G.B.“ = Gemeinde Bischofsheim (19. Jh.), Gründe für drei „b“,
  Werkrute = Nürnberger Rute 3,647676 m (Wikipedia „Rute (Einheit)“, im Gelände bestätigt).
- Stein 369: Der „1308er“ ist verschwunden; der Befund im Datensatz betrifft einen anderen
  Stein im Umkreis von ca. 2 m, vermutlich Waldgrenzstein. → Anmerkung im Dossier.
  **`data.json` nicht geändert** (von den geschützten Seiten genutzt) – Entscheidung Hendriks offen.
- Weiteres Protokoll 1724 (StA Würzburg, Gebr. A Wü IV G 196 III) in die Quellen aufgenommen.

**Neu: `artikel.html`** – die sieben FN-Artikel (27.08.–04.11.2024) in Hendriks
Manuskriptfassung, mit Titel und Erscheinungsdatum der Zeitung. Nur Fotos mit Vermerk
„H. Beierstettel“ übernommen (Galgen Mudau, Spitalsteine, Hoheitssäulen); Archivkarten und
Fotos Dritter weggelassen. Verlinkt von Start, Projekt, Quellen, Stein 94/369 und im Fuß
aller Seiten (`werkzeuge/rahmen.py`).

**Hochgeladen** (Sicherung vorher `backups/2026-09-28_1427_server_ftp`): 4 Bilder, artikel,
begriffe, quellen, stein, projekt, index und die übrigen Rahmenseiten – 17 Dateien, alle per
SHA-256 identisch. Lokaler Ordner per PowerShell angeglichen, `site/` aktualisiert.

**Offen:**
1. Hendrik: Fotos ohne Bildvermerk in den Artikeln (Judenstein, Stein 1493, Bruchstück 1508,
   Gründle, Bruchstück 1490, Rosenstein, Hufeisen) – eigene Fotos? Dann aufnehmen.
2. Hendrik: Stein 369 in `data.json` korrigieren (Befehl nötig, geschützte Seiten lesen die Datei)?
3. Neue Erklärseite zur Rekonstruktion mit durchgerechnetem Beispiel (Hendriks Wunsch f).
4. Bewerbungsunterlagen Landespreis.


## 28.09.2026, 12:34 – Hendriks Angaben eingearbeitet, dritter Upload

**Neue Quellen von Hendrik:** `Quellenverzeichnis Gemarkungsgrenze TBB.txt` (im Repo),
Mailwechsel mit Dr. Gerrit Himmelsbach (Spessart-Projekt), 24.–26.02.2026 (PDF nur lokal,
per `.gitignore` ausgeschlossen – Kontaktdaten Dritter), FN-Artikelserie 2024, Folgen 02–04
(`C:\Users\User\Documents\_Taubertal\FN-Grenzsteine-Serie`, Leserecht erteilt).

**Eingearbeitet:**
- `quellen.html` neu: alle Signaturen (Stadtarchiv TBB Abt. B Nr. 3–8a, GLA 229 Nr. 35161 a),
  zwölf weitere Archivalien, Kartengrundlagen mit Lizenzlinks (DGK5 über Geoportal BW,
  Historische Gemarkungsübersicht Baden 1:10000 als Open GeoData), Grenzlinie in QGIS aus
  der DGK5 nachgezeichnet, Messverfahren (Garmin GPSMAP 65s + Pixel 4/8 + Sony DSC-HX60V,
  Abgleich, DGK5-Kontrolle), Begehungen **2017–2021** (nicht nur 2021), Validierung an
  Steinpaaren, bekannte Grenzen der Berechnung (Berichtigung 1887 Hänglein–Bösehof,
  A 81/Industriegebiet 1980er), Literatur (Simmerding 1997/99, Pahl 1955, FN-Serie 2024).
- `projekt.html`: Entstehung (seit ca. 2005, Hundespaziergänge, TK25, Kleindenkmale),
  Forschungsfrage, Eigenleistung genauer (Zuordnung ohne KI), Ausblick, Veröffentlichungen.
- `begriffe.html`: Landschieder/Feldschieder, Eckstein, Dreimärker (dreieckig), drei „b“,
  Jahreszahlen und Lesefehler (1224 statt 1724, „1308“?), Ziffernschrift 15. Jh.,
  Bildunterschrift Archivfoto = **Stein 94** (Eckstein 1474; Protokolle 1569 und 1608: 2 „b“).
- `stein.html`: Anmerkungen zu Stein 94, 369 („1308“), 370 („1224“); „Befund 2021“ →
  „Befund im Gelände“.
- `index.html`: Bildunterschrift Titelfoto = Stein 58 (1508, Heidenkessel, Grenze Dittwar).
- 2021 → 2017–2021 in index, grenzgaenge, chronik, recherche, vergleich, download.

**Hochgeladen** (Sicherung vorher `backups/2026-09-28_1234_server_ftp`): quellen, projekt,
begriffe, grenzgaenge, recherche, vergleich, download, chronik, stein, index. Alle 10 per
SHA-256 identisch; live geprüft. Lokaler Ordner per PowerShell angeglichen, `site/` aktualisiert.

**Offen / Rückfragen an Hendrik:**
1. Frage 5 (Kreuz oben, rot/weiß, „GB“/„G.B.“ in der b-Spalte, Beleg Werkrute 3,65 m) –
   Hendrik hat die Frage nicht verstanden; im Chat neu erklärt.
2. **Widerspruch Stein 369 („1308“):** Datensatz: gefunden, am ursprünglichen Platz
   (Nr. 187.2); FN-Artikel 02: „seit ein paar Jahrzehnten spurlos verschwunden“.
3. Stein 94 = Archivfoto bestätigen lassen.
4. Erscheinungsdaten der FN-Artikel für das Literaturverzeichnis.


## 27.09.2026, 17:32 – Zweiter Upload: Abschnitt 1 und 2 online (auf Hendriks Wunsch vor Eingang der Restangaben)

**Sicherung vorher:** `backups/2026-09-27_1732_server_ftp` (64 Dateien).

**Vorbereitung:** Alle gelb markierten Lücken entfernt, damit nichts Halbfertiges
sichtbar ist. Dabei vorläufig **weggelassen** und morgen nachzutragen:
Archiv/Signatur je Quelle (Tabelle zeigt „wird ergänzt“), Literaturabschnitt,
Herkunft/Lizenz DGK5 und Gemarkungskarte 1932, genaue LGL-Datensatzbezeichnung,
GPS-Modell/Genauigkeit/Zeitraum, Abschnitte „Wie es anfing“ und „Wie es weitergeht“
(projekt.html). **Vorsichtiger formuliert**, bis Hendrik bestätigt: Kreuz auf der
Oberseite (nur „wird vermerkt“), Farbe (nur „hängt vom Gestein ab“), Bedeutung
von drei „b“ und „GB“ (weggelassen). Datenstand: Februar 2026 (Datensatz),
August 2026 (berechnete Standorte).

**Hochgeladen (44 Dateien):** `assets/grenze.css`, `assets/menue.js`,
`bilder/grenzstein-mainzer-rad.jpg`, `bilder/grenzstein-brehmbachtal-landesarchiv.jpg`,
`grenzsteine-tauberbischofsheim.csv`; Seiten `index`, `recherche`, `grenzgaenge`,
`begriffe`, `quellen`, `projekt`, `download`, `vergleich`, `stein`, `chronik`,
`impressum`, `datenschutz`; 26 Weiterleitungen (die 21 wegfallenden Seiten plus die
unverlinkten `karte2`, `karte_v2`, `reconstruction_`, `reconstruction_test`,
`rekonstruktion`) und `Zeitachse.html` (Großschreibung, per `--als`).
Nicht angefasst: die drei Kernseiten, `data.json`, GeoJSON, Flurnamen. Alte
Dateien `titelbild.png`, `assets/style.css`, `assets/print.css`, `assets/mail.js`,
`version.json` liegen noch auf dem Server, werden aber nicht mehr verwendet.

**Prüfung:** 44/44 Dateien per SHA-256 identisch. Live im Browser: alle Seiten
laden, keine kaputten Bilder, „Digitale Edition“ nirgends mehr; Weiterleitungen
führen zum richtigen Ziel.

**Lokale Expression-Web-Kopie** per PowerShell angeglichen (43 Dateien);
`site/` aktualisiert.


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

**Antworten Hendriks (27.09., abends):** Zuordnung nur bei eindeutigem Abgleich von
Eintragungen und Entfernungen als „sicher“ (in `quellen.html` eingearbeitet); GPS:
Garmin-Handgerät, Details folgen. ⏰ **Morgen (28.09.) früh liefert Hendrik:** Quellenangaben
(Archiv/Signatur, Literatur, Protokoll 1784) und die GPS-Details. Noch offen: Fragen 4–8
(Karten-Lizenzen, Begriffe b/GB/Kreuz/Farbe/Werkrute, Projektanfang und -pläne,
Jahreszahl 1224, Titelbild-Stein). Upload von Abschnitt 2 erst, wenn die gelben Lücken
gefüllt sind.

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
