#! python3
# addGaps.py - inserts gaps into numbered files so that a new filw can be added

import os, shutil, re
folder = input('Enter a directory: ').strip()
os.chdir(folder)

endsWithNumberRegex = re.compile(r'^([A-Za-z]*)?(\d+)(\d)')



filenames = []
for filename in os.listdir():
    mo = endsWithNumberRegex.search(filename)
    if mo != None:
        filenames.append(filename)

number = len(filenames)
while True:
    try:
        gapPoint = int(input('Enter file number to add gap: '))
        if gapPoint > number:
            print(f'Files are not up to {gapPoint}')
        else:
            break
    except ValueError:
        print('You must enter a number')
    
if sorted(filenames)[-1].endswith(f'{number+1}.txt'):
    print('Gap already exists!')
else:
    for filename in sorted(filenames, reverse=True):
        if number == gapPoint:
            break
        mo = endsWithNumberRegex.search(filename)
        if mo != None:
            prefix = mo.group(1)
            trailingnum = mo.group(2)
            lastnum = mo.group(3)
            newFileName = prefix + trailingnum + str(number + 1) + '.txt'
            shutil.move(filename, newFileName)
            number -= 1
            
print(os.listdir()) 