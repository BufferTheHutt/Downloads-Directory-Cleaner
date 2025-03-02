#!/usr/bin/env python3

import os

# Zuordnung --> ggf. Anpassen
FILE_TYPE_MAP = {
    "Bilder": ["jpg", "jpeg", "png", "webp", "gif", "bmp"],
    "Archive": ["zip", "xz", "gz", "7z", "rar"],
    "Pakete_Binaries": ["rpm", "deb", "snap", "apk", "exe"],
    "Office": ["doc", "odt", "rtf", "pdf", "xls", "ods", "csv", "tsv", "ppt", "pptx", ".pages", ".numbers", "odp", "xlsx", "docx"],
    "Textfiles": ["txt"],
    "Fonts": ["ttf"],
    "Webseiten": ["html", "css"],
    "Images": ["iso"],
}

# Pfade definieren
downloads_directory = "/home/<USER>/Downloads" # <-- PFAD ANPASSEN!!!
# -----------------------------------------------------------
inhalte_downloads = os.listdir(downloads_directory)