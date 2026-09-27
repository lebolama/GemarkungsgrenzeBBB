# Backup, Upload und Dokumentation

## Server

- Website: `https://beierstettel.de/Grenze/`
- Hosting: freenet-Webspace (`web12.freenetdomain.de`), statische Dateien + PHP
  (Quelle: `lebolama/claude-Lab`, `Archive-App/web/betrieb/VEROEFFENTLICHUNG.md`)
- Verzeichnis auf dem Server: `httpdocs/Grenze/`
- Zugangsdaten: nur lokal bei Hendrik (`C:\claude-Lab`, Passwort über cmd-Skript).
  **Nie ins Repo.** Protokoll (FTP/FTPS/SFTP) beim ersten Upload aus den
  vorhandenen Unterlagen ermitteln und hier eintragen (ohne Passwort).

## Werkzeug (Stand 27.09.2026)

Upload und Sicherung laufen über ein lokales Werkzeug auf Hendriks PC
(`werkzeuge/ftp.py`, nicht im Repo), FTPS auf Port 21, Zielordner
`/httpdocs/Grenze`. Befehle: `liste`, `sichern`, `hochladen DATEI…`
(geschützte Seiten nur mit `--geschuetzt-freigegeben`). Freigabe in
`C:\claude-Lab\.claude\settings.local.json`; Befehl immer exakt so und ohne
Pipe aufrufen: `PYTHONIOENCODING=utf-8 python werkzeuge/ftp.py …`

Lokalen Expression-Web-Ordner mit **PowerShell** (`Copy-Item`) angleichen –
der Windows-„Überwachte Ordnerzugriff“ blockiert die Git-Bash.

## Grundregeln

1. **Vor jedem Upload** den aktuellen Serverstand des Ordners `Grenze/`
   vollständig herunterladen und datiert sichern:
   `backups/AAAA-MM-TT_HHMM_server/` (lokal auf Hendriks PC; im Repo nur,
   wenn Größe vertretbar – große Datendateien ggf. per `.gitignore` ausschließen).
2. Zusätzlich die lokale Expression-Web-Kopie
   (`C:\Users\User\Documents\My Web Sites\beierstettel\httpdocs\Grenze`)
   vor Änderungen sichern.
3. Nur geänderte Dateien hochladen. **Nie** `standorte.html`, `karteXL.html`,
   `reconstruction_xl.html` oder von ihnen genutzte Dateien ohne ausdrücklichen
   Befehl.
4. Nach dem Upload: Seiten im Browser prüfen (Desktop und Handybreite),
   Links prüfen, die drei geschützten Seiten auf unveränderte Funktion prüfen.
5. Eintrag in `docs/PROTOKOLL.md`: Datum, Uhrzeit, hochgeladene Dateien,
   Backup-Ordner, Grund, Prüfergebnis.
6. Nach dem Upload die lokale Expression-Web-Kopie auf denselben Stand bringen,
   damit Hendrik nicht versehentlich einen alten Stand zurückspielt.

## Rückspielen (Rollback)

Betroffene Dateien aus dem jüngsten Backup-Ordner wieder hochladen, im
Protokoll vermerken.
