import openpyxl

from openpyxl.utils import column_index_from_string, get_column_letter
print(column_index_from_string('P'))

#! python3
# multiplication_table_maker.py
# Creates an NxN multiplication table in an Excel spreadsheet.

import sys
import random
import openpyxl
from openpyxl.styles import Font, Alignment

# letters = []
# for num in range(1, 27):
#     letters.append(f'{get_column_letter(num).upper()}')
# print(letters)

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

wb = openpyxl.load_workbook('crossword3.xlsx')
sheet = wb.active


# Fill the multiplication table.
for row in range(1, sheet.max_row+1):
    for column in range(1, sheet.max_column+1):
        resultCell = sheet.cell(row=row, column=column)
        resultCell.alignment = Alignment(horizontal="center", vertical="center")

        if (resultCell.value == None):
            resultCell.value = f'{random.choice(letters)}'

wb.save('crosswordUpdated3.xlsx')
        

