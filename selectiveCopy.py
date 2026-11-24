#! python3
# selectiveCopy.py - moves all .pdf files from specified location to a new location

import os, shutil

# Walk through a folder tree
path = input('Enter path: ').strip()
os.chdir(path)
for foldername, subfolders, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('.pdf'):
            try:
                shutil.move(os.path.join(foldername, filename), '.\\pdfs')
            except shutil.Error:
                print(rf'Could not move {filename} in {foldername}')
                
print('Done')
