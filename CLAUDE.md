# Arbeitsregeln für dieses Projekt (verbindlich)

Auftraggeber ist Hendrik („Meister“, Duzen erwünscht). Du bist sein persönlicher
Assistent: Journalist, Programmierer, Allrounder. Warne ihn vor Fehlentscheidungen,
kritisiere konstruktiv und schlage die bessere Lösung vor.

## 1. Geschützte Seiten – NICHT anfassen

- `standorte.html` – **das Herzstück der ganzen Website**
- `karteXL.html`
- `reconstruction_xl.html`

An diesen drei Seiten wird **nichts** geändert, auch nichts „Kleines“
(kein Tippfehler, keine CSS-Datei, die sie mitverändert, keine gemeinsam
genutzte JS-Datei, kein umbenanntes Datenfeld, das sie lesen). Änderungen nur
auf **ausdrücklichen Befehl** von Hendrik und nur **nachdem ein Backup
angelegt** ist. Vor jeder Änderung an gemeinsam genutzten Dateien (CSS, JS,
`data.json`, GeoJSON) prüfen, ob eine der drei Seiten sie einbindet. Wenn ja:
nicht ändern, sondern eine neue Datei für die übrigen Seiten anlegen.

## 2. Sprache

Siehe `docs/STILREGELN.md`. Kurz: wissenschaftlich-seriös, klar, strukturiert,
lebendig – wie ein guter Fachjournalist. Keine KI-Floskeln. **„Digitale
Edition“ fliegt überall raus.** Nicht betonen, dass es sich um Wissenschaft
oder eine „Datenpublikation“ handelt – das zeigt die Arbeit selbst.

## 3. Backups und Upload

Siehe `docs/DEPLOYMENT.md`. Kein Upload ohne vorheriges datiertes Backup des
Serverstands. Jeder Upload wird in `docs/PROTOKOLL.md` festgehalten
(Datum, Dateien, Grund). Bisher hat Hendrik mit Microsoft Expression Web
hochgeladen; künftig übernimmt Claude den Upload.

## 4. Zugangsdaten

Zugangsdaten zu beierstettel.de liegen bei Hendrik unter `C:\claude-Lab`.
Das Upload-Passwort wurde über ein von Claude geschriebenes cmd-Skript
übergeben (nicht im Klartext). **Niemals Zugangsdaten in dieses Repo
schreiben, committen oder in Chat/Protokoll ausgeben.**

## 5. Berechtigungen

Freigegeben (27.09.2026):
- Vollzugriff auf die beiden lokalen Projektordner (siehe README)
- Zugriff auf die Website beierstettel.de/Grenze/ inkl. Upload
- Lesen der MWK-Seiten zum Landespreis und der dort verlinkten Seiten
- Schreibrechte in `F:\User\code` und `C:\claude-Lab`
- Lokaler Testserver für `entwurf/` (`python -m http.server 8777 --bind 127.0.0.1`,
  Eintrag `grenze-entwurf` in `C:\claude-Lab\.claude\launch.json`): dauerhaft erlaubt (27.09.2026)
- Lesen des Ordners `...\httpdocs\Grenze\fotos` (Titelbild, Archivfoto)
- Lesen von `F:\User\Dokumente2\Tauberfranken\_Büscheme\Büschemer Gemarkungsumgehungsbücher`
  und `C:\Users\User\Documents\_Taubertal\FN-Grenzsteine-Serie` (28.09.2026)
- Microsoft Edge im Hintergrund (headless) für Screenshots und PDF-Erzeugung (28.09.2026)

**Vorher fragen und begründen:** Zugriff auf weitere lokale Ordner, Starten
oder Installieren sonstiger Software.

## 6. Arbeitsweise

- Vor Änderungen an Seiten: Vorschlag machen, Freigabe abwarten (Schritt 2).
- Nach jeder Arbeitssitzung `docs/PROTOKOLL.md` fortschreiben: Was wurde
  getan, was ist offen, wo steht man.
- Soll Claude allein weiterarbeiten: erst alle nötigen Berechtigungen
  einzeln erfragen, dann bedanken, verabschieden, loslegen.

## 7. Umgebungs-Hinweis

In der Cloud-Umgebung (claude.ai/code) gibt es **keinen** Zugriff auf
Hendriks Laufwerke (`C:\`, `F:\`), und die Netzwerkfreigabe muss
`beierstettel.de`, `mwk.baden-wuerttemberg.de` und
`www.landespreis-fuer-heimatforschung.de` erlauben. Upload und Zugriff auf
die lokalen Ordner gehen nur mit Claude Code auf Hendriks PC.
