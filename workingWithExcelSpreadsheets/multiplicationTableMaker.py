#! python3
# multiplicationTableMaker.py - creates an NxN multiplicaion table in an excel spreadsheet

import sys
import openpyxl
from openpyxl.styles import Font
from openpyxl.styles import Alignment

print("This program creates an NxN multiplication table based on the number 'N' given.")

wb = openpyxl.Workbook()
sheet = wb.active

x = 1
y = 1
j = 1

if len(sys.argv) >= 2:
    N = int(sys.argv[1])
else:
    N = int(input('Enter a number: '))

sheet.freeze_panes = 'A2'
sheet.freeze_panes = 'B2'


sheet.cell(row=1, column=1).alignment = Alignment(horizontal='center', vertical='center')
sheet.cell(row=1, column=1).font = Font(bold=True, italic=True, )
sheet.cell(row=1, column=1).value = 'x'

for rowNum in range(2, N+2):
    sheet.cell(row=rowNum, column=1).alignment = Alignment(horizontal='center', vertical='center')
    sheet.cell(row=rowNum, column=1).font = Font(bold=True, italic=True)
    sheet.cell(row=rowNum, column=1).value = y

    y += 1

for columnNum in range(2, N+2):
    sheet.cell(row=1, column=columnNum).alignment = Alignment(horizontal='center', vertical='center')
    sheet.cell(row=1, column=columnNum).font = Font(bold=True, italic=True)
    sheet.cell(row=1, column=columnNum).value = x
    x += 1

for rowNum in range(2, N+2):
    i = rowNum - 1
    for columnNum in range(2, N+2):
        sheet.cell(row=rowNum, column=columnNum).alignment = Alignment(horizontal='center', vertical='center')
        sheet.cell(row=rowNum, column=columnNum).value = i
        i += j
    j += 1

wb.save(f'multiplicationTable{N}x{N}.xlsx')
print(f'multiplicationTable{N}x{N}.xlsx has been created in the cwd')



