# Backups

Jeder Ordner `AAAA-MM-TT_HHMM_server` bzw. `..._lokal` ist eine vollständige
Sicherung von `Grenze/` zum genannten Zeitpunkt. Die Dateien selbst liegen nur
lokal auf Hendriks PC (`C:\claude-Lab\GemarkungsgrenzeBBB\backups\`); im Repo
steht je Sicherung nur `_MANIFEST.json` (Dateiname, Größe, SHA-256, beim
Server zusätzlich `Last-Modified`). Damit lässt sich jederzeit prüfen, ob eine
Datei einem gesicherten Stand entspricht.

| Ordner | Quelle | Anlass |
|---|---|---|
| `2026-09-27_1518_server` | https://beierstettel.de/Grenze/ (per HTTP gespiegelt) | Erst-Backup vor Beginn der Überarbeitung |
| `2026-09-27_1518_lokal` | `C:\Users\User\Documents\My Web Sites\beierstettel\httpdocs\Grenze` | Erst-Backup der Expression-Web-Kopie |

Hinweis: Die Server-Sicherung wurde über HTTP gezogen. Sie enthält alle Dateien,
die von den Seiten aus verlinkt sind oder im lokalen Ordner vorkommen. Dateien,
die auf dem Server liegen, aber nirgends verlinkt sind, fehlen darin. Die erste
Sicherung per FTP (vor dem ersten Upload) schließt diese Lücke.
