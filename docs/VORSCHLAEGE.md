# Verbesserungsvorschläge für beierstettel.de/Grenze/ (Schritt 2)

Status: **noch nicht erstellt.** Voraussetzung ist die Sichtung der Live-Site
Seite für Seite (Text, Layout, Bedienbarkeit, Handy-Ansicht, Links,
Rechtliches). Die drei geschützten Seiten werden nur angesehen, nicht verändert.

## Von Hendrik bereits benannt

- „Digitale Edition“ überall entfernen. Startseite: Titel „Die Grenzsteine der
  Gemarkung Tauberbischofsheim“.
- Alle Texte von KI-Sprache befreien, Selbstetikettierung
  („wissenschaftliche Datenpublikation“) streichen.
- „Recherche“ und „Experten-Recherche“: funktional gut, aber ohne jede
  Erklärung → Hilfetexte ergänzen.
- Layout vieler Seiten verbessern.

## Vorläufige Beobachtungen am älteren Code in diesem Repo

(Nur Hinweise, an der Live-Site zu überprüfen.)

- `suche.html`: Titel „Vergleichsanalyse“, Navigation nennt „Recherche“ –
  uneinheitlich. Links auf `vergleich.html` und `karte.html` – existieren sie?
  Filter „≥1 b / =1 b …“ sind ohne Erklärung unverständlich. Ergebnisse zeigen
  nur nackte ID-Nummern.
- `rekonstruktion.html`: OpenStreetMap-Kacheln ohne Quellenangabe
  (Attribution ist Lizenzpflicht). Leaflet ohne feste Versionsnummer von unpkg
  geladen (kann bei neuer Leaflet-Version brechen). Der „Unsicherheitsradius“
  entspricht dem Abstand zum Vorgängerstein – methodisch fragwürdig, für die
  Jury erklärungsbedürftig.
- Uneinheitliche Seitentitel und Navigationsleisten.
- Zu prüfen: Impressum und Datenschutzerklärung (Pflicht; Google-Fotos-Links,
  externe Kartenkacheln, unpkg-CDN).
