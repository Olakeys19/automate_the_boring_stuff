#! python3
# blankRowInserter.py - takes two integers and a filename string as command line arguments. 
# Create a program blankRowInserter.py that takes two integers and a filename string as command line arguments. Let’s call the first integer N and the second integer M. Starting at row N, the program should insert M blank rows into the spreadsheet.

import sys, os
import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string
from openpyxl.styles import Font, Alignment
from copy import copy

if len(sys.argv) > 1:
    N = int(sys.argv[1])
    M = int(sys.argv[2])
    filename = sys.argv[3]
else:
    N = int(input('Enter starting row: '))
    M = int(input('Enter number of blank rows to insert: '))
    filename = input('Enter filename: ')

wb = openpyxl.load_workbook(filename)
sheet = wb.active
wb2 = openpyxl.Workbook()
copySheet = wb2.active
col_max = sheet.max_column



def copyFontAlignmentAndValue(source, destination, source_row, destination_row, source_coulumn, destination_column):
    destination.cell(row=destination_row, column=destination_column).font = copy(source.cell(row=source_row, column=source_coulumn).font)
    destination.cell(row=destination_row, column=destination_column).alignment = copy(source.cell(row=source_row, column=source_coulumn).alignment)
    destination.cell(row=destination_row, column=destination_column).value = source.cell(row=source_row, column=source_coulumn).value


for row in range(1, N):
    for column in range(1, col_max+1):
        copyFontAlignmentAndValue(sheet, copySheet, row, row, column, column)


for row in range(N, sheet.max_row+1):
    for column in range(1, col_max+1):
        copyFontAlignmentAndValue(sheet, copySheet, row, row+M, column, column)

basename = filename.split('.')[0]
extension = filename.split('.')[-1]
wb2.save(f'blank_rows_{basename}.{extension}')

print(f'File has been saved as blank_rows_{basename}.{extension}')



