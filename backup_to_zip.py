"""
This program copies the entire folder and file into a zip
file whose filenames increment.
"""

import zipfile,os
from pathlib import Path

def backup_to_zip(folder):
    # back up entire content into a zip.
    folder = Path(folder) # Make sure folder is Path, not a string.
    print(folder)

    number = 1
    while True:
        zip_filename = Path(folder.parts[-1] + "_" + str(number) + ".zip")
        if not zip_filename.exists():
            print("yes")
            break
        number += 1

        print(f"Creating {zip_filename}...")
        backup_zip = zipfile.ZipFile("zip_filename", "w")

        # Walking through every single folders, subfolders and files.
        for folder_name, subfolders, filenames in os.walk(folder):
            folder_name = Path(folder_name)
            print(f"Adding files in folder {folder_name}...")

            # Compressing all the folder and files into a zip.
            for filename in filenames:
                print(f"Adding files {filename}...")
                backup_zip.write(folder_name / filename)
        backup_zip.close()
        print("Done.")

backup_to_zip(Path("d:/PROGRAMMES/Code Arena/Back-up-Folder--zip-") / "spam")
