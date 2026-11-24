# # Charts

# import openpyxl
# from openpyxl.chart import BarChart, Reference

# wb = openpyxl.Workbook()
# sheet = wb.active

# # Create data
# for i in range(1, 11):
#     sheet[f'A{i}'] = i

# # Reference the data
# data = Reference(
#     sheet,
#     min_col=1,          # starting column
#     min_row=1,          # starting row
#     max_col=1,          # ending column
#     max_row=10          # ending row
# )

# # Create chart
# chart = BarChart()
# chart.add_data(data, titles_from_data=False)
# chart.title = "First Series"

# # Add chart to worksheet
# chart.width = 20 # set chart width to 20cm
# chart.height = 10 # set chart height to 10cm
# sheet.add_chart(chart, "C3") # Use cell C3 as starting position for the chart

# wb.save("sampleChart.xlsx")

# wb2 = openpyxl.load_workbook('sampleChart.xlsx')
# wb2.save('test.xlsx')