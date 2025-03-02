#!/usr/bin/env python3

import os
import shutil
from config import FILE_TYPE_MAP, downloads_directory, inhalte_downloads

# Sicherstellen, dass alle Zielordner existieren
for dir_name in FILE_TYPE_MAP.keys():
    tmp_dir_name = os.path.join(downloads_directory, dir_name)
    os.makedirs(tmp_dir_name, exist_ok=True)

# Sonstige-Ordner anlegen
sonstige_Ordner = os.path.join(downloads_directory, "Sonstige")
os.makedirs(sonstige_Ordner, exist_ok=True)

# Funktion zum sicheren Verschieben
def move_file_safe(src, dest_folder):
    """ Datei sicher verschieben: Falls Datei existiert, umbenennen """
    filename = os.path.basename(src)
    dest_path = os.path.join(dest_folder, filename)

    counter = 1
    while os.path.exists(dest_path):
        name, ext = os.path.splitext(filename)
        dest_path = os.path.join(dest_folder, f"{name}_{counter}{ext}")
        counter += 1

    shutil.move(src, dest_path)
    return dest_path

# Dateien sortieren
for inhalt in inhalte_downloads:
    source_path = os.path.join(downloads_directory, inhalt)

    if os.path.isdir(source_path):  # Falls Verzeichnis, überspringen
        continue

    splitted = inhalt.rsplit(".", 1)
    if len(splitted) == 2:  # Wenn Splittung erfolgreich --> 2 Teile entstehen
        extension = splitted[-1].lower()
        print(f"📂 Datei: {inhalt} | Endung: {extension}")

        for category, ext_list in FILE_TYPE_MAP.items():
            if extension in ext_list:
                target_path = os.path.join(downloads_directory, category)
                print(f"✅ Verschiebe {inhalt} nach {target_path}")
                move_file_safe(source_path, target_path)
                break  # ✅ Falls verschoben, verlasse die Schleife!
        else:
            print(f"⚠️ Keine Kategorie gefunden – verschiebe {inhalt} nach {sonstige_Ordner}")
            move_file_safe(source_path, sonstige_Ordner)
    else:
        print(f"⚠️ Keine Endung erkannt – verschiebe {inhalt} nach {sonstige_Ordner}")
        move_file_safe(source_path, sonstige_Ordner)

print("\n✅ Sortierung abgeschlossen!")
