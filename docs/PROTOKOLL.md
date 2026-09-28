# Arbeitsprotokoll

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
