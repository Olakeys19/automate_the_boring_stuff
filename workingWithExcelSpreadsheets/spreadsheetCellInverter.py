#! python3
# spreadsheetCellInverter.py - interchanges a spreadsheet's rows and columns

import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active
wbInverted = openpyxl.Workbook()
invertedSheet = wbInverted.active

for row in range(1, max(sheet.max_row, sheet.max_column)+1):
    for column in range(1, max(sheet.max_row, sheet.max_column)+1):
        invertedSheet.cell(row=row, column=column).value = sheet.cell(row=column, column=row).value

wbInverted.save('invertedProduceSales.xlsx')
