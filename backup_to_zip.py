"""
This program copies the entire folder and file into a zip
file whose filenames increment.
"""

import zipfile,os
from pathlib import Path

def backup_to_zip(folder):
    # back up entire content into a zip.
    folder = Path(folder) # Make sure folder is Path, not a string.

    number = 1
    while True:
        zip_filename = Path(folder.parts[-1] + "_" + str(number) + ".zip")
        if not zip_filename.exists():
            break
        number += 1

        print(f"Creating {zip_filename}...")
        backup_zip = zipfile.ZipFile("zip_filename", "w")
    print("Done.")

backup_to_zip(Path("D:\PROGRAMMES\Code Arena\Back-up-Folder--zip-") / 'spam')
