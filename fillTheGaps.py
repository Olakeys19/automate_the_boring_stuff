#! python3
# fillTheGaps.py - finds all files with a given prefix in a single folder, locates any gaps in the numbering and renames all later files to close this gap

import os, shutil, re
folder = input('Enter a directory: ').strip()
os.chdir(folder)

endsWithNumberRegex = re.compile(r'^([A-Za-z]*)?(\d+)(\d)')


filenames = []
for filename in os.listdir():
    mo = endsWithNumberRegex.search(filename)
    if mo != None:
        filenames.append(filename)

number = 1

for filename in sorted(filenames):
    mo = endsWithNumberRegex.search(filename)
    if mo != None:
        prefix = mo.group(1)
        trailingnum = mo.group(2)
        lastnum = mo.group(3)
        newFileName = prefix + trailingnum + str(number) + '.txt'
        if lastnum != number:
            shutil.move(filename, newFileName)
        number += 1
    
print(os.listdir())






