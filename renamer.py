#! Python 3
#! renamer.py - a program to rename all files in a directory, compress them into a zip file based on the parent folder name, and delete the loose files. Copy the directory to your clipboard or enter it in the console when prompted. 

from pathlib import Path
import logging, os, zipfile, pyperclip

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

if Path(pyperclip.paste()).is_dir():
        folderPath = Path(pyperclip.paste())
else:
    folderPath = Path(input("Enter the path to the files you want to rename:\n\n"))
    while not folderPath.is_dir():
        print(f'{folderPath} is not a valid path.')
        folderPath = Path(input("Enter the path to the files you want to rename:\n\n"))

os.chdir(folderPath)

parentDirIndex = str(folderPath)[::-1].find('\\')
parentDir = str(folderPath)[-parentDirIndex:]

logging.debug(f'The folder path is {folderPath}.')
logging.debug(f'The file header is {parentDir}.')

fileNum = 1
for file in os.listdir():
    file = Path(file)
    newFilename = f'{parentDir} {fileNum}{file.suffix}'
    if parentDir not in file.name:
        os.rename(file, newFilename)
    logging.debug(f'The full filepath is {file}')
    fileNum += 1
    logging.debug(f'{file} was renamed to {newFilename}')

fileNum = 1
while True:
    zipFileName = f'{parentDir} {fileNum}.zip'
    if not os.path.exists(zipFileName):
        break
    fileNum += 1

with zipfile.ZipFile(zipFileName, 'w') as zip:
    for file in os.listdir():
        if '.zip' not in file:
            # filePath = folderPath / Path(file)
            zip.write(file, compress_type=zipfile.ZIP_DEFLATED)
            logging.debug(f'{file} was added to {zipFileName}.zip')
            os.remove(file)
