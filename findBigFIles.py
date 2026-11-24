#! python3
# findBigFiles.py - finds files greater than 100MB in a specified folder

import os, shutil

folder = input('Enter a directory: ').strip()
os.chdir(folder)

print(f'Files greater than 100MB in {folder}')

for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if os.path.getsize(os.path.join(foldername, filename)) > 104857600:
            print(f'{os.path.join(foldername, filename)} is {round(os.path.getsize(os.path.join(foldername, filename))/(1024*1024), 2)}MB')