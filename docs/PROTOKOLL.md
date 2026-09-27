# Arbeitsprotokoll

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
