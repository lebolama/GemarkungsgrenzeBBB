# Verbesserungsvorschläge für beierstettel.de/Grenze/

Stand: 27.09.2026. Grundlage ist die Sichtung aller 33 HTML-Seiten des Live-Stands
(Quelltext in `site/`, dazu im Browser auf Desktop und in Handybreite geprüft).
Jeder Punkt hat eine Nummer, damit Hendrik einzeln freigeben, ablehnen oder
ändern kann.

## ✅ Entscheidungen Hendriks (27.09.2026)

1. **Alle Punkte freigegeben**, einschließlich Wegfall der Analyse-Seiten (3.1).
2. **Punkt 7.1 ausdrücklich befohlen:** Leaflet-Version in `standorte.html`,
   `karteXL.html`, `reconstruction_xl.html` und `service-worker.js` auf 1.9.4
   festschreiben (ebenso `leaflet.markercluster` in `karteXL.html`). Nur diese
   Änderung, nur mit Backup vorher. Alles andere an den drei Seiten bleibt tabu.
3. **Quellenangaben (4.3):** Hendrik liefert Archiv/Signatur je Grenzgang,
   Literatur und Fundort des Großrinderfelder Protokolls 1784 – **Claude muss
   ihn daran erinnern** (Ziel: bis 06.10.2026).
4. **Fotos bleiben bei Google Fotos** (Speicherplatz). Punkt 7.3 entfällt;
   stattdessen vor der Einreichung alle Fotolinks automatisch auf Erreichbarkeit
   prüfen.
5. **Nutzungsrechte (2.4):**
   - *Daten* (`data.json`, CSV, Tabellen): Weiterverwendung erlaubt, auch für
     Folgeforschung, **wenn Hendrik Beierstettel als Quelle genannt wird** →
     entspricht der Standardlizenz **CC BY 4.0**.
   - *Fotos*: **alle Rechte vorbehalten**; Nutzung nur nach persönlicher
     Zustimmung (Anfrage per E-Mail).
   - *Texte der Website*: ebenfalls alle Rechte vorbehalten (Zitieren nach
     Zitatrecht bleibt ohnehin erlaubt).
6. **Stein 1 und ähnliche Fälle:** Lesart bestätigt – ein Stein mit jüngerer
   Jahreszahl ersetzt einen älteren Stein an derselben Stelle. Im Dossier und
   auf „Begriffe“ allgemein erklären.
7. **Frist 31.10.2026: ja.**
8. **Lokaler Testserver** (`python -m http.server`, nur 127.0.0.1): **dauerhaft erlaubt.**
9. **Titelbild:** Hendriks eigenes Foto `fotos/DSC08806.JPG` (verkleinert, ohne
   EXIF/GPS als `bilder/grenzstein-mainzer-rad.jpg`).
10. **Archivfoto** Landesarchiv BW, Staatsarchiv Wertheim, K-LRA 91 Nr. 253,
    Bild 17 (Permalink http://www.landesarchiv-bw.de/plink/?f=7-168711-17;
    laut Findbuch u. a. „Grenzstein von 1474 im Brehmbachtal zwischen Königheim
    und Tauberbischofsheim“): darf verwendet werden, **wenn die Quelle klar
    genannt ist.**
11. **Upload:** Hendrik gibt Claude den Zugriff auf die Upload-Unterlagen in
    `C:\claude-Lab` über eine Freigabe in den Claude-Code-Einstellungen (steht aus).

Legende Priorität: **P1** vor der Einreichung unverzichtbar · **P2** deutlich
besser für die Jury · **P3** wünschenswert, kann warten.

---

## 0. Kurzfazit

Die Website hat einen starken Kern: `standorte.html`, das Stein-Dossier
(`stein.html`) und die Rekonstruktionskarte zeigen eine Datenfülle, wie sie
kaum ein Heimatforschungsprojekt bietet. Drumherum stehen aber rund zwanzig
Seiten, die Codex nach dem Baukastenprinzip erzeugt hat: gleiche Kacheln,
Fachjargon ohne Erklärung, Titel wie „Hypothesen-Generator“ oder „Automatische
Periodisierung“ und Deutungssätze, die nicht aus den Quellen stammen,
sondern aus einer Formel. Zwei Seiten liefern nachweislich falsche Werte.
Eine Jury aus Historikern und Heimatpflegern wird genau dort hängen bleiben.

**Empfehlung:** Weniger Seiten und diese besser. Aus 33 Seiten werden etwa 12.
Alles, was die Forschung zeigt, bleibt erhalten; alles, was nur Forschung
simuliert, fällt weg oder wird von Hendrik neu und von Hand formuliert.
Das ist bis 31.10. zu schaffen, wenn Hendrik die Quellenangaben (Punkt 4.3)
liefert.

---

## 1. Fehler, die sofort auffallen (P1)

| Nr. | Seite | Befund | Vorschlag |
|---|---|---|---|
| 1.1 | `abstaende.html` | Zeigt für jeden Grenzgang „Messungen: 394 · Ø Abstand: 0,00 m“. Der Code sucht Felder (`row["1608"]`), die es in `data.json` nicht gibt. | Neu berechnen aus den Spalten „Meter zum vorherigen“ bzw. „Ruthen zum vorherigen“, oder Seite streichen. |
| 1.2 | `distanzkarte.html` | Leere Karte, kein einziger Punkt. Code liest `r.gps` und `r.id`, die heißen aber `_gps_parsed`/`ID`. | Streichen. Die Abstände sind in `standorte.html` ohnehin besser dargestellt. |
| 1.3 | `zeitachse.html`, `zeitachse_v2.html`, `Zeitachse.html`, `statistik.html` (Diagramm 2) | Zählen **ausgefüllte Datenfelder**, nicht Steine, beschriften das aber als „Dokumentierte Steine“. Die Kurve sagt also nichts über die Zahl der Steine. | Durch eine richtige Zählung aus `_derived.presence_by_year` ersetzen (1569: 104, 1608: 118, 1683: 111, 1700: 114, 1749: 116, 1784: 7, 1872: 201, 1887–93: 351, 2021: 144). |
| 1.4 | `statistik.html` Diagramm 3 | Kreisdiagramm „mind. ein ‚x‘ vorhanden / kein ‚x‘“ ist ohne Aussage. | Streichen. |
| 1.5 | `projekt.html` | „206 Grenzsteine, 6 historische Zeitpunkte, 75 Datenfelder“. Der Datensatz hat 394 Positionen, 9 Quellenstände (1569/80, 1608, 1683, 1700, 1749, 1784, 1872, 1887–93, 2021) und 94 Felder. | Zahlen korrigieren und an **einer** Stelle pflegen. |
| 1.6 | `edition.html`, `quellen.html` | Nennen nur 6 Grenzgänge (bis 1872). Es fehlen die Großrinderfelder Grenzbegehung 1784 und die Grenzberichtigungen 1887–93. „1 Ruthe = 3,65 m“ gilt nicht für 1872 ff. (neue badische Rute 3,00 m). | Vervollständigen. |
| 1.7 | Versionsangaben | Startseite „Version 1.5“, `edition.html`/`version.json`/Zitierempfehlung „Version 1.0“. | Eine Versionsnummer, am Stichtag der Einreichung festgeschrieben. |
| 1.8 | Doppelte Dateien | `Zeitachse.html` und `zeitachse.html` liegen beide auf dem Server (unter Windows nicht darstellbar, s. `site/_namenskollision/`). Dazu gibt es `suche.html` und `suche_2.html`, `zeitachse_v2.html`, `reconstruction.html` neben `reconstruction_xl.html`. | Je Thema eine Seite. Alte Adressen als Weiterleitung behalten, damit keine Links brechen. |
| 1.9 | `veraenderung.html` | Öffentlich sichtbarer Entwicklerhinweis: „Wenn Spaltenbezeichnungen **in deiner Datei** ungewöhnlich abweichen …“ | Entfernen. |
| 1.10 | 27 von 33 Seiten | Kein `<meta name="viewport">`. Auf dem Handy wird die Seite auf 981 px Breite geschrumpft und ist kaum lesbar. (Nicht betroffen: Start, Chronik, Rekonstruktion, `standorte.html`.) | Auf allen überarbeiteten Seiten ergänzen. |

## 2. Rechtliches (P1)

| Nr. | Befund | Vorschlag |
|---|---|---|
| 2.1 | **Es gibt keine Datenschutzerklärung.** Die Seiten laden Inhalte von unpkg.com, cdn.jsdelivr.net, cdnjs.cloudflare.com, OpenStreetMap- und CARTO-Kachelservern und verlinken auf Google Fotos. Dabei wird die IP-Adresse der Besucher an Dritte übertragen. | Datenschutzerklärung schreiben (ein Muster gibt es aus der Archivsuche auf demselben Webspace). Mittelfristig Bibliotheken selbst hosten (s. 7.1). |
| 2.2 | Impressum ist nur von der Startseite verlinkt, nicht von den Unterseiten. Inhalt ist knapp, aber für eine private, nichtkommerzielle Seite im Kern ausreichend. Die Mailadresse steht nur per JavaScript da. | Impressum und Datenschutz auf **jeder** Seite im Fuß verlinken. Einen Satz „Projektcharakter: wissenschaftliche digitale Edition“ streichen. |
| 2.3 | OSM-Namensnennung fehlt auf `karte.html`, `karte-b.html`, `distanzkarte.html` (Lizenzpflicht der ODbL). CARTO-Kacheln ohne Nennung. | Namensnennung ergänzen bzw. Seiten zusammenlegen/streichen. |
| 2.4 | `download.html`: „Freie wissenschaftliche Nutzung unter Angabe der Quelle“ ist keine klare Lizenz. | Eine Standardlizenz wählen, z. B. CC BY 4.0 für Daten und Texte (Hendrik entscheidet). |

## 3. Aufbau und Navigation (P1/P2)

Heute: 33 Seiten, fünf verschiedene Navigationsleisten, die meisten zeigen
„Start | Recherche | Vergleich | Karte“ und führen zur alten `suche.html`. Die
Startseite nennt 15 Links in einer Liste, darunter zwei mit Satzlänge.

**Vorschlag für den neuen Aufbau** (Arbeitstitel, Wortlaut der Menüpunkte kurz):

| Menü | Seite(n) | Herkunft |
|---|---|---|
| **Start** | `index.html` | neu geschrieben |
| **Karte der Grenzsteine** | `standorte.html` | geschützt, unverändert |
| **Verschwundene Steine** | `reconstruction_xl.html` | geschützt, unverändert |
| **Amtliche Grenzpunkte** | `karteXL.html` | geschützt, unverändert |
| **Steine suchen** | `recherche.html` | aus `suche_2.html`, mit Hilfetext |
| **Steine vergleichen** | `vergleich.html` | aus `suche.html`/`vergleich.html` zusammengeführt, mit Hilfetext |
| **Einzelner Stein** | `stein.html` | bleibt, Texte überarbeitet |
| **Die Grenzgänge** | `grenzgaenge.html` | neu: was ist ein Grenzgang, die neun Quellen im Überblick, Zahlen je Jahr (ersetzt Zeitachse, Statistik, Veränderung) |
| **Geschichte** | `chronik.html` | bleibt, gekürzt und überarbeitet |
| **Quellen und Methode** | `quellen.html` | aus `quellen.html`, `edition.html`, `projekt.html` zusammengeführt |
| **Begriffe** | `begriffe.html` | neu: Gemarkung, Grenzgang, Dreimärker, Rute, Mainzer Rad, „b“, Wappenschild, Läufer usw. |
| **Über das Projekt** | `projekt.html` | neu: wer, warum, wie lange; Grenzsteinbeauftragter der Stadt |
| **Daten** | `download.html` | bleibt, mit Feldbeschreibung und Lizenz |
| Fuß: Impressum · Datenschutz | `impressum.html`, `datenschutz.html` | Datenschutz neu |

Eine gemeinsame Kopf- und Fußzeile für alle nicht geschützten Seiten. Die drei
geschützten Seiten behalten ihren eigenen Kopf; ein Link „zurück zur
Startseite“ ist dort schon vorhanden.

**Wegfallen** (mit Weiterleitung auf die passende neue Seite):
`suche.html`, `suche_2.html`, `zeitachse.html`, `Zeitachse.html`,
`zeitachse_v2.html`, `statistik.html`, `veraenderung.html`, `abstaende.html`,
`distanzkarte.html`, `karte.html`, `karte-b.html`, `analysen.html`,
`anomalien.html`, `hypothesen.html`, `perioden.html`, `periodisierung.html`,
`symbolcluster.html`, `b_typologie.html`, `bericht.html`, `changelog.html`,
`edition.html`, `reconstruction.html`.

Begründung für die Analyse-Seiten (3.1, P1): Sie erzeugen Deutungen per Formel,
z. B. „Die Intensität der B-Markierung gilt als Indikator für territoriale
Symbolstärke“, „Kurzlebige Typen deuten auf Reformphasen“, „Anomalie:
außergewöhnlich alt“ (Schwelle: 1,5 × Durchschnittsalter). Keine dieser Aussagen
ist belegt. Für eine Jury, die „wissenschaftliche Qualität“ bewertet, ist das
der gefährlichste Teil der Website. **Wenn Hendrik zu einzelnen Fragen eigene
Beobachtungen hat** (etwa zur Zahl der „b“ oder zum Wechsel vom Mainzer Rad zu
anderen Zeichen), gehören sie als von ihm formulierter Text mit Belegsteinen auf
„Die Grenzgänge“.

## 4. Seite für Seite

### 4.1 Startseite `index.html` (P1)
- Titel „Digitale Edition der Grenzsteine …“ → **„Die Grenzsteine der Gemarkung Tauberbischofsheim“**. `<title>` ebenso.
- Fußzeile „Digitale Edition — wissenschaftliche Datenpublikation“ streichen.
- Kachel „Projekt“ durch 4–6 Sätze ersetzen: was die Grenze ist (rund 30 km, neun Nachbargemarkungen), was die Quellen sind (Grenzgänge 1569 bis 1893), was 2021 geschah (Geländebegehung, 143 Steine wiedergefunden, 126 am ursprünglichen Platz), was man hier tun kann.
- Statt 15 Links drei große Einstiege: **Karte** (`standorte.html`), **Stein suchen**, **Geschichte und Quellen**. Darunter die übrigen Seiten kurz.
- Bildbeschreibung des Titelbilds (`alt`) sachlich: was zeigt das Bild?
- Hinweis auf die Handynutzung im Gelände (Standortfunktion in `standorte.html`) als Stärke herausstellen.

### 4.2 Recherche (`suche_2.html` → `recherche.html`) (P1)
Funktioniert, ist aber ohne Erklärung nicht zu bedienen.
- Oben 2–4 Sätze: Was finde ich hier? Wie fange ich an? Beispiel: „Alle Steine an der Grenze zu Impfingen, die 1608 ein Mainzer Rad trugen“.
- Aufklappbares „So funktioniert’s“: Filter A und B, was „Nur A / Nur B / Beide“ bedeutet, was Volltext durchsucht.
- Ergebnis zeigt heute „1 / Dittigheim“. Besser: „Stein 1 · Grenze zu Dittigheim · 1569–1887 belegt · 2021 gefunden“.
- Checkbox „b“ erklären (Bischofsheimer Zeichen), „Rad“ → „Mainzer Rad“.
- Auf dem Handy: Filter untereinander statt nebeneinander.
- Jahr „1887“ heißt richtig „1887–93 (Grenzberichtigungen)“; 1784 fehlt in der Auswahl.

### 4.3 Quellen und Methode (`quellen.html` + `edition.html` + `projekt.html`) (P1)
- **Genaue Quellenangaben mit Archiv und Signatur je Grenzgang.** Heute steht nur „Stadtarchiv Tauberbischofsheim“. Die Teilnahmebedingungen verlangen ausdrücklich ein Quellen- und Literaturverzeichnis. → **Braucht Hendriks Zuarbeit.**
- Methode in Prosa: Wie wurden die Beschreibungen Stein für Stein einander zugeordnet? Wie wurde 2021 gesucht und eingemessen (Gerät, Genauigkeit)? Wie entstehen die rekonstruierten Standorte und was bedeuten die Klassen A–D?
- Umrechnung der Längenmaße (fränkische Werkrute 3,65 m; neue badische Rute 3,00 m) mit Beleg.
- Transkriptionsregeln kurz und konkret; „diplomatisch“ mit Beispiel.
- Literaturverzeichnis (z. B. Stadtgeschichte, Arbeiten zu Grenzsteinen in Tauberfranken). → Hendrik.
- Streichen: „Wissenschaftlicher Status: entspricht den methodischen Standards digitaler Quelleneditionen“, „Forschungswert“-Liste, „Editionsprinzip der Quellenintegration“.

### 4.4 Stein-Dossier `stein.html` (P2)
Stark. Verbesserungen:
- Navigation zum vorigen/nächsten Stein entlang der Grenze.
- „Frühestes mögliches Setzjahr 1841“ neben „Erstnennung 1569“ verwirrt (Beispiel Stein 1). Satz ergänzen: „Der heutige Stein trägt die Jahreszahl 1841; er ersetzt einen älteren Stein an derselben Stelle.“ (nur wenn das so stimmt – Hendrik).
- Mindestens ein Foto direkt anzeigen statt nur „Google-Fotoalbum öffnen“ (s. 7.3).
- Kleine Karte des Standorts einbetten.
- Bereich „Forschungsnotizen“ (Eingabefelder, die nur im Browser des Besuchers gespeichert werden, mit Knopf „Löschen“) für Besucher ausblenden; er irritiert und wirkt unfertig.
- „Abgeleitete Forschungsfelder (vollständig) automatisch berechnet“ → in „Technische Angaben“ umbenennen und zugeklappt lassen.
- Wenn `stein.html` ohne `?id=` aufgerufen wird (Link „Steine“ in der alten Navigation): Liste aller Steine zeigen statt leerer Seite.

### 4.5 Chronik `chronik.html` (P2)
Inhaltlich brauchbar, als einzige Nebenseite schon mit Einleitung.
- Belege überwiegend Wikipedia. Für die Jury durch Fachliteratur ersetzen oder ergänzen (Stadtgeschichte, LEO-BW, Historischer Atlas).
- Sätze wie „Kann Grenzpflege/Markierung beeinflussen“ nur, wo es für diese Grenze tatsächlich belegt ist; sonst streichen.
- „Grenzbegehung/Editionseintrag: chronologisch einsortiert und farblich hervorgehoben“ (steht achtmal da) streichen.
- „bewusst ‚kuratiert‘ … robuste Kontextschicht zur Grenzstein-Edition“ → einfacher Satz.

### 4.6 Vergleich (`vergleich.html`, `suche.html`) (P2)
Zusammenführen zu einer Seite „Zwei Grenzgänge vergleichen“: Jahr A und Jahr B wählen, Ergebnis in ganzen Sätzen („1608 sind 118 Steine beschrieben, 1683 sind es 111; 14 Steine werden 1683 nicht mehr genannt: …“), mit Links auf die betroffenen Steine. Hilfetext oben.

### 4.7 Karten `karte.html`, `karte-b.html` (P2)
Zeigen weniger als `standorte.html`, fehlerhafte Legende (Farbe nach „frühestem möglichem Setzjahr“, ohne Erklärung), Debug-Kasten „Datenstatus … Marker aktiv“ über der Karte, Jahresauswahl ohne 1784/1887/2021. → Streichen, auf `standorte.html` weiterleiten. Der „b“-Filter kann, wenn gewünscht, in die Recherche.

### 4.8 Download `download.html` (P2)
- Feldbeschreibung (was steht in welcher Spalte, was bedeutet „x“, leeres Feld, „?“).
- Zusätzlich CSV oder die Excel-Tabelle zum Herunterladen (für Heimatforscher ohne Programmierkenntnisse).
- Lizenz (2.4), Zitiervorschlag ohne „Digitale Edition“.

### 4.9 Impressum (P1) – s. 2.2. Zitierempfehlung dort streichen (gehört zu „Daten“).

### 4.10 Neue Seite „Begriffe“ (P2)
Kurze Erklärungen, jeweils mit Beispielstein: Gemarkung · Grenzgang/Grenzbegehung ·
Grenzberichtigung · Dreimärker · Läufer/Hauptstein (falls zutreffend) · Rute
(fränkische Werkrute, neue badische Rute) · Mainzer Rad · Wappenschild · „b“ für
Bischofsheim · Rückseite · Nummerierung damals und 2021.

### 4.11 Neue Seite „Über das Projekt“ (P2)
Wer (Hendrik Beierstettel, Tauberbischofsheim, ehrenamtlicher
Grenzsteinbeauftragter der Stadt, Tauberfränkische Heimatfreunde e.V.), seit
wann, wie viele Begehungstage, was als Nächstes kommt. Offen und kurz: welche
technischen Hilfsmittel eingesetzt wurden (auch KI-Werkzeuge für Programmierung
und Textentwürfe) und was Eigenleistung ist. Das entspricht dem, was die
Teilnahmebedingungen ohnehin verlangen.

## 5. Sprache (P1, alle Seiten außer den geschützten)

Nach `STILREGELN.md`. Die auffälligsten Stellen:
- „Digitale Edition“ wörtlich auf 7 Seiten (index 4×, edition, impressum, projekt je 2×, changelog, download, quellen je 1×); dazu „Edition“/„Grenzstein-Edition“ in weiteren Seiten (chronik, analysen, zeitachse …). Überall raus.
- Selbstetikettierung: „wissenschaftliche Datenpublikation“, „Forschungsinterface“, „Analyse-Dashboard“, „Forschungsbericht Generator“, „wissenschaftliche Auswertungs- und Forschungswerkzeuge“, „Datenintegrität“, „Wissenschaftlicher Status“.
- Anglizismen und Technikjargon: „Changelog“, „Dashboard“, „Cluster“, „Live-Filter“, „POIs (Points of Interest)“.
- Stichwortlisten statt Sätzen (Projekt, Quellen, Edition).
- Seitentitel uneinheitlich; fünf Seiten ohne `<title>`.

## 6. Gestaltung (P2)

- Eine gemeinsame Stilvorlage für die nicht geschützten Seiten. **Gute Nachricht:** `assets/style.css` wird von keiner der drei geschützten Seiten eingebunden (geprüft). Sie darf also überarbeitet werden, ohne CLAUDE.md §1 zu berühren.
- Farben und Schrift beibehalten (Dunkelrot, Serifenschrift), das passt zum Thema und zu `standorte.html`.
- Kacheln mit Schwebe-Effekt (Startseite, Analysen) durch ruhige Textblöcke ersetzen.
- Lesebreite für Fließtext begrenzen (ca. 70 Zeichen).
- Druckansicht für Stein-Dossier und Quellenseite (für die schriftliche Dokumentation nützlich).

## 7. Technik (P2/P3)

| Nr. | Befund | Vorschlag |
|---|---|---|
| 7.1 | **Alle drei geschützten Seiten** laden Leaflet ohne Versionsnummer von unpkg (`unpkg.com/leaflet/dist/leaflet.js`). Heute liefert das 1.9.4. Leaflet 2.0 ist als Vorabversion erschienen und ändert die Programmierschnittstelle. Sobald 2.0 als „latest“ erscheint, können **alle drei Kernseiten über Nacht ausfallen** – womöglich mitten in der Jurierung. Der Service-Worker von `standorte.html` speichert die unversionierte Adresse ebenfalls. | **Dringende Empfehlung, braucht Hendriks ausdrückliche Freigabe:** in den drei Seiten und im Service-Worker `leaflet` durch `leaflet@1.9.4` ersetzen (oder Leaflet auf den eigenen Server legen). Mini-Änderung, Backup vorher, danach alle Funktionen prüfen. Gleiches für `leaflet.markercluster` in `karteXL.html`. |
| 7.2 | `chart.js` (jsDelivr) ebenfalls ohne Version. | Auf den überarbeiteten Seiten feste Version, besser selbst gehostet. |
| 7.3 | ~~Entfällt (Entscheidung 4).~~ Fotos nur als Google-Fotos-Freigabelinks. Solche Links können jederzeit ungültig werden; das Haus der Geschichte archiviert prämierte Arbeiten. | Je gefundenem Stein 1–2 verkleinerte Fotos (z. B. 1200 px, ~200 KB) auf den eigenen Server. Bei 143 Steinen etwa 30–60 MB. Speicherplatz auf dem freenet-Webspace prüfen. |
| 7.4 | Beim allerersten Aufruf von `standorte.html` blieb die Karte einmal grau (Kacheln in Zoomstufe 20 angefordert, OSM liefert bis 19 → Fehler 400). Nach Neuladen einwandfrei, nicht sicher reproduzierbar. | Nur beobachten. Falls es wieder auftritt: `maxZoom: 19` in `standorte.html` – Änderung nur auf Befehl. |
| 7.5 | Die DGK5-Karte (`Flurnamen/dgk5-tauberbischofsheim.jpg`) ist 40 MB groß und wird vom Service-Worker für die Offline-Nutzung komplett geladen. | Hinweis im Offline-Knopf auf die Datenmenge; später ggf. als Kachelsatz. Geschützte Seite → nur auf Befehl. |
| 7.6 | `data.json` (2,5 MB) wird auf jeder Unterseite neu geladen. | Für die neue Recherche vertretbar; kein Handlungsbedarf vor der Einreichung. |
| 7.8 | `karteXL.html` (geschützt): Die Ebenen „Historische Grenzsteine“ und „Rekonstruierte Steine“ bleiben beim Einschalten leer, auch live und schon vor jeder Änderung (geprüft 27.09.). Der Code liest `r.gps`/`r.id`, in `data.json` heißen die Felder `_gps_parsed`/`ID` – derselbe Fehler wie bei `distanzkarte.html`. Die LGL-Grenzpunkte (65) und die Grenzlinie funktionieren. Außerdem lautet die Überschrift „Kartenanalyse“, und die Navigation führt auf die wegfallenden Seiten (dort greifen die Weiterleitungen). | ✅ **Auf Hendriks Befehl repariert** (27.09.2026), in `entwurf/`. |
| 7.7 | Lokaler Expression-Web-Ordner weicht vom Server ab (z. B. neuere `reconstruction.html` lokal, `reconstruction_xl.html` fehlt lokal). | Nach jedem Upload den lokalen Ordner angleichen (DEPLOYMENT.md). Hendrik sollte bis dahin **nichts** mehr mit Expression Web hochladen. |

## 8. Für die Bewerbung (P1)

- Stichtagsfassung einfrieren (`/Grenze-2026/` oder ZIP), s. `LANDESPREIS.md`.
- Schriftliche Dokumentation (≤ 8 MB PDF) mit Screenshots der Kernseiten.
- Eine Seite „Quellen und Methode“, die so gut ist, dass sie gleichzeitig das
  geforderte Quellen- und Literaturverzeichnis ersetzt.

---

## Zeitplan (Vorschlag, bei Freigabe am 28.09.)

| Zeitraum | Arbeit |
|---|---|
| 28.09.–02.10. | Rechtliches, Fehlerseiten entfernen/weiterleiten, neue Navigation, Startseite, Stilvorlage. Punkt 7.1 (falls freigegeben). Erster Upload mit Backup. |
| 03.10.–10.10. | Recherche mit Hilfetexten, Vergleich, Stein-Dossier, Begriffe. |
| 06.10.–15.10. | Quellen und Methode, Über das Projekt, Chronik – **dafür braucht es Hendriks Quellenangaben und Literatur bis ca. 06.10.** |
| 15.10.–24.10. | Dokumentation (PDF), Kriterienkatalog, Formulartexte, Fotos. |
| 25.10.–29.10. | Gesamtprüfung Desktop/Handy, Linkprüfung, Stichtagsfassung einfrieren. |
| bis 30.10. | Hendrik reicht ein (ein Tag Puffer vor Fristende). |

---

## Rückfragen an Hendrik (gesammelt)

1. **Freigabe der Liste:** Welche Punkte ja, welche nein, welche anders? Besonders: Einverstanden, dass die Analyse-Seiten (3.1) wegfallen?
2. **Punkt 7.1 (Leaflet-Version in den drei geschützten Seiten festschreiben):** Gibst du dafür den ausdrücklichen Befehl? Es wäre die einzige Änderung an diesen Seiten.
3. **Quellen:** Kannst du je Grenzgang Archiv und Signatur (oder Fundstelle) nennen, dazu die Literatur, die du benutzt hast? Wo liegt das Großrinderfelder Protokoll von 1784?
4. **Fotos:** Sollen Fotos auf den eigenen Server (7.3)? Wenn ja: Hast du die Originale lokal, und in welchem Ordner?
5. **Lizenz** für Daten und Texte: CC BY 4.0 in Ordnung?
6. **Stein 1 und ähnliche Fälle:** Stimmt die Lesart „Stein von 1841 ersetzt einen älteren Stein an derselben Stelle“? Dann würde ich das im Dossier allgemein erklären.
7. **Frist:** Nach dieser Liste halte ich den 31.10.2026 für machbar, wenn Punkt 3 bis Anfang Oktober geklärt ist. Gehen wir auf diese Frist?
