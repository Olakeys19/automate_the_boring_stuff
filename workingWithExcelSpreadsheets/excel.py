# # WORKING WITH EXCEL SPREADSHEETS

# # Opening Excel Documents with OpenPyXl
# import openpyxl
# wb = openpyxl.load_workbook('example.xlsx') # open the example.xlsx document and store in wb
# print(type(wb))

# # Getting sheets from the workbook
# print(wb.sheetnames) # wb.sheetnames to get all the sheets in the workbook. Each sheet is rep by a worksheet object
# sheet = wb['Sheet3'] # select Sheet3 and store in the variable sheet. 
# print(sheet)
# print(type(sheet))
# print(sheet.title) # sheet.title to get the title of sheet
# anotherSheet = wb.active # wb.active to select active worksheet
# print(anotherSheet)

# # Getting cells from the sheets
# sheet1 = wb['Sheet1'] # select Sheet1
# print(sheet1['A1']) # print the cell A1 (object) of Sheet1
# print(sheet1['A1'].value) # print the value of cell A1
# c = sheet1['B1'] # store the object cell B1 as variable c
# print(c.value)  # print the value of the cell

# print(f'Row {c.row}, Column {c.column} is {c.value}') # c.row, c.column, c.value to get the row name, column number and content of the cell respectively
# print(f'Cell {c.coordinate} is {c.value}') # c.coordinate to get the coordinate (column and row) of the cell
# print(sheet1['C1'].value)

# # Using the cell() method to get a cell
# print(sheet1.cell(row=1, column=2)) # get sheet one cell which corresponds to the first row and second column
# print(sheet1.cell(row=1, column=2).value) # get the value of the sheet one cell which corresponds to the first row and second column

# for i in range(1, 8, 2): # loop through 1 to 8 in steps of 2
#     print(i, sheet1.cell(row=i, column=2).value) # print the cell value of each cell


# # Determining the size of a sheet
# print(sheet1.max_row) # find the max number of row in a worksheet
# print(sheet1.max_column) # find the max number of column in a worksheet


# # Converting Between Column Letters and Numbers
# from openpyxl.utils import get_column_letter, column_index_from_string
# print(get_column_letter(1)) # get column letter from number
# print(get_column_letter(27))
# print(get_column_letter(900))

# print(get_column_letter(sheet1.max_column)) 
# print(column_index_from_string('AHP')) # get column number from letter


# # Getting Rows and Columns from the Sheets
# print(tuple(sheet1['A1':'C3'])) # get all row objects from A1 to C3 as tuples

# for rowOfCellObjects in sheet1['A1':'C3']:
#     for cellObj in rowOfCellObjects:
#         print(cellObj.coordinate, cellObj.value)
#     print('--- END OF ROW ---')


# print(tuple(sheet1.columns)) # get all column objects as tuples
# for cellObj in tuple(sheet1.columns)[1]:
#     print(cellObj.value)


