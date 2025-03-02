# Downloads-Directory-Cleaner 🗂️

Ein Python-Skript zum automatischen Sortieren von Dateien im `Downloads`-Ordner in Kategorieunterordner.

[![Demo](https://img.shields.io/badge/-Demo-blueviolet)](https://img.shields.io/badge/-Demo-blueviolet) | [Desktop-Icon-Anleitung](#desktop-anwendung-erstellen)

## Inhaltsverzeichnis

- [Funktionen](#funktionen)
- [Installation](#installation)
- [Konfiguration](#konfiguration)
- [Verwendung](#verwendung)
- [Desktop-Anwendung erstellen](#desktop-anwendung-erstellen)
- [Häufige Probleme](#häufige-probleme)
- [Contributing](#contributing)
- [Lizenz](#lizenz)

## Funktionen
- Sortiert Dateien nach Typ (Bilder, Archive, Office-Dokumente, etc.)
- Erkennt über 20 Dateiendungen
- Legt automatisch einen `Sonstige`-Ordner für unbekannte Typen an
- Vermeidet Überschreiben durch automatisches Umbenennen (z.B. `datei_2.txt`)

## Installation
1. **Repository klonen**:
   ```bash
   git clone https://github.com/deinbenutzername/downloads-organizer.git
   cd downloads-organizer
   ```
   
**Abhängigkeiten:**
- Python 3.x
- Keine externen Bibliotheken benötigt 🎉

## Konfiguration
Passe die Datei `config.py` an:

- Ändere den Pfad in `downloads_directory` zu deinem Download-Ordner:
  ```python
  downloads_directory = "/home/DEIN_BENUTZERNAME/Downloads"  # ← Pfad anpassen!
  ```
- Erweitere `FILE_TYPE_MAP` für eigene Kategorien/Endungen:
  ```python
  "Musik": ["mp3", "wav", "flac"],
  "Videos": ["mp4", "mov", "avi"]
  ```

## Verwendung
Als Skript:
```bash
python3 optimized_sort.py
```

Als Desktop-Anwendung:
Folge der [Desktop-Icon-Anleitung](#desktop-anwendung-erstellen)

## Desktop-Anwendung erstellen
Skript ausführbar machen:
```bash
chmod +x optimized_sort.py
```

Erstelle eine `.desktop`-Datei (z. B. unter `~/.local/share/applications/organizer.desktop`):
```ini
[Desktop Entry]
Version=1.0
Type=Application
Name=Downloads Organizer
Exec=/pfad/zum/downloads-organizer/optimized_sort.py
Icon=/pfad/zum/ordner/icon.png
Terminal=false
Categories=Utility;
```

Icon herunterladen oder eigenes erstellen.

## Häufige Probleme
**"Pfad nicht gefunden":**
- Prüfe die Schreibweise in `config.py`.
- Stelle sicher, dass du die richtigen Benutzerrechte für den Ordner besitzt.

**Dateien werden nicht verschoben:**
- Teste das Skript im Terminal: `python3 optimized_sort.py`.
- Überprüfe die Dateiberechtigungen.

## Contributing
Pull Requests sind willkommen!  
Mögliche Erweiterungen:
- GUI hinzufügen
- Cloud-Integration (Google Drive, Dropbox)
- Logging-Funktion

## Lizenz
MIT License - Frei für persönliche und kommerzielle Nutzung.
