#! python3
# spreadsheetToText.py - opposite of textToSpreadsheet.py; opens a spreadsheet and writes the cells of each column into a unique text file.

import openpyxl
from openpyxl.utils import get_column_letter

filename = 'textToSpreadsheet1.xlsx'
wb = openpyxl.load_workbook(filename)
sheet = wb.active

for column in range(1, sheet.max_column+1):
    with open(f'{filename.split('.')[0]}Column{column}.txt', 'w') as f_obj:
        for row in range(1, sheet.max_row):
            try:
                f_obj.write(sheet.cell(row=row, column=column).value)
            except TypeError:
                None
                # print(f'Cell {get_column_letter(column)}{row} is empty')


