# # # WRITING EXCEL DOCUMENTS
# import openpyxl

# # # # Creating and Saving Excel Documents

# # # # # # Creating and saving a workbook
# # # # # wb = openpyxl.Workbook() # Create a workbook
# # # # # print(wb.sheetnames)
# # # # # sheet = wb.active # select active sheet object
# # # # # print(sheet.title)
# # # # # sheet.title = 'Spam Bacon Eggs Sheet' # change active sheet title to spam bacon eggs sheet
# # # # # print(wb.sheetnames)

# # # # # wb.save('example2.xlsx') # save workbook as a file named example2.xlsx in the cwd

# # # # # Another example
# # # # wb = openpyxl.load_workbook('example.xlsx')
# # # # sheet = wb.active
# # # # sheet.title = 'Spam Spam Spam'
# # # # wb.save('example_copy.xlsx')


# # # # Creating and Removing sheets
# # # # Creating
# # # wb = openpyxl.Workbook()
# # # print(wb.sheetnames)
# # # wb.create_sheet() # create a new worksheet at the last index, Sheet1 will be created
# # # print(wb.sheetnames) # verify

# # # wb.create_sheet(index=0, title='First Sheet') # create a sheet titled First sheet at index 0
# # # print(wb.sheetnames)

# # # wb.create_sheet(index=2, title='Middle Sheet') # create a sheet titled Middle Sheet at index 2
# # # print(wb.sheetnames)

# # # # Removing
# # # wb.remove(wb['Middle Sheet']) # remove the worksheet object with name 'Middle Sheet'
# # # del wb['Sheet1'] # remove the worksheet object with name 'Sheet1'
# # # print(wb.sheetnames)


# # # Writing Values to Cells
# # wb = openpyxl.Workbook() # Create a workbook, a default Sheet is always created by default
# # sheet = wb['Sheet'] # select default Sheet Object created
# # sheet['A1'] = 'Hello world!' # save Hello world! as the value of A1 in Sheet
# # print(sheet['A1'].value)


# # # Setting the Font Style of Cells
# # from openpyxl.styles import Font 
# # wb = openpyxl.Workbook()
# # sheet = wb['Sheet']

# # # sheet['A1']x
# # # sheet['A1'] = 'Hello world!'
# # # wb.save('styled.xlsx')

# # # # Keyword Arguments for Font Style Attributes
# # # # 1. name - the font name such as 'Calibri'
# # # # 2. size - the point size
# # # # 3. bold - True, for bold font
# # # # 4. italic - True, for italic font

# # # A1: Bold Times New Roman
# # sheet['A1'] = 'Bold Times New Roman'
# # sheet['A1'].font = Font(name='Times New Roman', bold=True)

# # # B3: 24 pt Italic
# # sheet['B3'] = '24 pt Italic'
# # sheet['B3'].font = Font(size=24, italic=True)

# # wb.save('styles.xlsx')


# # # FORMULAS
# # # wb = openpyxl.Workbook()
# # # sheet = wb.active
# # # sheet['A1'] = 200 # write 200 to cell A1
# # # sheet['A2'] = 300 # write 300 to cell A2
# # # sheet['A3'] = '=SUM(A1:A2)' # store the sum of A1 and A2 in cell A3
# # # wb.save('writeFormula.xlsx')


# # wbFormulas = openpyxl.load_workbook('writeFormula.xlsx')
# # sheet = wbFormulas.active
# # print(sheet['A3'].value) # returns the formula used 

# # wbDataOnly = openpyxl.load_workbook('writeFormula.xlsx', data_only=True)
# # sheet = wbDataOnly.active
# # print(sheet['A3'].value) # returns the calculated sum only if Excel has been opened and saved with the value from the formula already


# # ADJUSTING ROWS AND COLUMNS
# # # Setting Row Height and Column Width
# # wb = openpyxl.Workbook()
# # sheet = wb.active
# # sheet['A1'] = 'Tall row'
# # sheet['B2'] = 'Wide column'
# # sheet.row_dimensions[1].height = 70 # set row 1 heught to 70. Height can be integer or float value between 0 and 409
# # sheet.column_dimensions['B'].width = 20 # set column B width to 20. Width can be integer or float between 0 and 255. 
# # # NOTE: width or height of 0 means hidden from the user
# # wb.save('dimensions.xlsx')


# # # Merging and unmerging cells
# # # Merging
# # wb = openpyxl.Workbook()
# # sheet = wb.active
# # sheet.merge_cells('A1:D3')
# # sheet['A1'] = 'Twelve cells merged together.'
# # sheet.merge_cells('C5:D5')
# # sheet['C5'] = 'Two merged cells'
# # wb.save('merged.xlsx')

# # # Unmerging
# # sheet.unmerge_cells('A1:D3')
# # sheet.unmerge_cells('C5:D5')
# # wb.save('merged.xlsx')


# # Freeze Panes
# # NOTE: all rows above and allcolumns to the left of the selected cell will be frozen, but the row and column of the cell itself will not be frozen.
# # Example
# # 1. sheet.freeze_panes = 'A2' will freeze Row 1
# # 2. sheet.freeze_panes = 'B1' will freeze Column A
# # 3. sheet.freeze_panes = 'C1' will freeze Columns A and B
# # 4. sheet.freeze_panes = 'C2' will freeze Row 1 and columns A and B
# # 5. sheet.freeze_panes = 'A1' or  sheet.freeze_panes = None equals no frozen pane

# # wb = openpyxl.load_workbook('produceSales.xlsx')
# # sheet = wb.active
# # sheet.freeze_panes = 'A2'
# # wb.save('freezeExample.xlsx')





