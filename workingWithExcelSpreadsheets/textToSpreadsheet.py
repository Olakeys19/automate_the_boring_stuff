#! python3
# textToSpreadsheet - takes multiple text files and copies the contents of each text file to a new column in a spreadsheet

import openpyxl
from openpyxl.styles import Alignment


filenames = [] # empty list to store filenames
while True:
    filename = input('Enter name of text file, enter done to proceed: ').strip()
    if filename == 'done':
        break
    filenames.append(filename)

print(filenames)

wb = openpyxl.Workbook()
sheet = wb.active

for i, filename in enumerate(filenames, start=1):                             # loop over each filename in the list, store the index as i
    try:
        with open(filename, 'r', encoding='utf-8') as f_obj:                                # open file
            text = f_obj.readlines()                                                        # store the lines in the file in the text variable
        
            for row in range(1, len(text)+1):                                 # loop over the lines of the text, text[row-1] because items in list start at index 0
                sheet.cell(row=row, column=i).value = text[row-1]                           # store each line as a new row
                sheet.cell(row=row, column=i).alignment = Alignment(wrap_text=True)         # wrap to ensure entire text is shown
    except FileNotFoundError:
        print(f'{filename} was not found in the current working directory')

            
wb.save('textToSpreadsheet1.xlsx')







