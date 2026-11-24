
tableData = [['apples', 'oranges', 'cherries', 'banana'], 
             ['Alice', 'Bob', 'Carol', 'David'], 
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    colWidth = 0

    for row in data:
        for item in row:
            if len(item) > colWidth:
                colWidth = len(item)

    for i in range(len(data[0])):
        for row in data:
            print(row[i].rjust(colWidth), end='')
        print()
    


printTable(tableData) 