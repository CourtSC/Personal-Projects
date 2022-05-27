#! Python 3
#! renamer.py - A program to rename all files in a directory, compress them into a zip file based on the parent folder name, and delete the loose files. Copy the directory to your clipboard or enter it in the console when prompted.

from pathlib import Path
import logging, os, zipfile, pyperclip

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.disable(logging.CRITICAL)

# Set the current working directory.
input("Copy the path you would like to organize to your clipboard and press Enter.")
try:
    folderPath = Path(pyperclip.paste())
except:
    while not folderPath.is_dir:
        print(f"{folderPath} is not a valid path.")
        input(
            "Copy the path you would like to organize to your clipboard and press Enter."
        )
        folderPath = Path(pyperclip.paste())
os.chdir(folderPath)
assert Path.cwd() == folderPath

# Configure file names.
parentDirIndex = str(folderPath)[::-1].find("\\")
parentDir = str(folderPath)[-parentDirIndex:]
logging.debug(f"The folder path is {folderPath}.")
logging.debug(f"The file header is {parentDir}.")

# Extract all files that are already zipped.
for file in os.listdir():
    if ".zip" in file:
        with zipfile.ZipFile(file, "r") as zip:
            zip.extractall()
        os.remove(
            file
        )  # Writing a new zip file later in this program will automatically overwrite zip files with the same name as the parent folder, but if another .zip file is present then this line will delete it when we're done with it.
        logging.debug(f"{file} extracted to {Path.cwd()}")

# Rename the files.
skipFiles = [Path(file) for file in os.listdir() if parentDir in file]
fileNum = len(skipFiles) + 1
for file in os.listdir():
    file = Path(file)
    newFilename = f"{parentDir} {fileNum}{file.suffix}"
    if parentDir not in file.name:
        os.rename(file, newFilename)
        fileNum += 1
    logging.debug(f"The full filepath is {file}")
    logging.debug(f"{file} was renamed to {newFilename}")

# Zip all of the files up.
with zipfile.ZipFile(f"{parentDir}.zip", "w") as zip:
    for file in os.listdir():
        if ".zip" not in file:
            zip.write(file, compress_type=zipfile.ZIP_DEFLATED)
            logging.debug(f"{file} was added to {parentDir}.zip")
            os.remove(file)
