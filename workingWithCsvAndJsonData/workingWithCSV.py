import csv

# # Reading csv
# exampleFile = open('example.csv')                   # open csv file as a file object
# exampleReader = csv.reader(exampleFile)             # create a reader object with csv.reader()
# exampleData  = list(exampleReader)                  # call list on the reader object to create a nested list of the contents of the csv file
# print(exampleData)
# print(exampleData[0][0])                    # get the first item in the first list; first row, first column
# print(exampleData[6][1])                    # get the second item in the seventh list; senenth row, second column


# # Reading Data from Reader Objects in a for Loop
# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)  
# for row in exampleReader:
#     print(f'Row #{exampleReader.line_num} {row}') # reader object's line_num variable contains the number of the current line

# # Writing CSV Files
# # Writer Objects
# outputFile = open('output.csv', 'w', newline='') # set newline='' to avoid double line spacing
# outputWriter = csv.writer(outputFile)           # call the csv writer on the output file object
# outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham']) # use writerow to write values in list format as a row
# outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
# outputWriter.writerow([1, 2, 3.141592, 4])
# outputFile.close()


# # The delimiter and lineterminator keyword arguments
# # The delimiter is a character that appears between cells on a row. By default, the delimiter for a CSV file is a comma
# # The line terminator is the character that comes at the end of a row. By default, the line terminator for a CSV file is a newline
# csvFile = open('example.tsv', 'w', newline='')      # we are using tsv as file extension because we are going to make our values tab seperated
# csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')      # delimiter set to a tab value, lineterminator set to double line spacing
# csvWriter.writerow(['apples', 'oranges', 'grapes'])
# csvWriter.writerow(['eggs', 'bacon', 'ham'])
# csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
# csvFile.close()

# # Output of example.tsv
# """
# apples	oranges	grapes

# eggs	bacon	ham

# spam	spam	spam	spam	spam	spam

# """


# Handling Header Rows
# Dictreader and Dictwriter objects perform the same functions using dictionaries, treating the values in the first row as the keys
example_file = open('exampleWithHeader3.csv')
example_dict_reader = csv.DictReader(example_file)  # store the content of the csv file as a dictionary object where the first row serves as keys 
example_dict_data = list(example_dict_reader)       # return a list of dictionaries, ecach row is a dictionary
print(example_dict_data)

example_file = open('exampleWithHeader3.csv')
example_dict_reader = csv.DictReader(example_file)
for row in example_dict_reader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])  # use the keys (first row) to access the values in other rows


# Asssigning keys to DictReader()
example_file = open('example.csv')
example_dict_reader = csv.DictReader(example_file, ['time', 'name', 'amount'])  # use time, name and amount as keys for the dictionaries since the first row of example.csv is not a header row
for row in example_dict_reader:
    print(row['time'], row['name'], row['amount'])


# Dictwriter objects use dictionaries to create CSV files
output_file = open('output3.csv', 'w', newline='')
output_dict_writer = csv.DictWriter(output_file, ['Name', 'Pet', 'Phone'])
output_dict_writer.writeheader()
output_dict_writer.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
output_dict_writer.writerow({'Name': 'Bob', 'Phone': '555-9999'})
output_dict_writer.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})
output_file.close()


# Verstile Pliantext Format
