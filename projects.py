spam = ['apples', 'bananas', 'cats', 'tofu', 'cats']

# # Using list slicing
# def stringed_list(list):
#     string = ''

#     for item in list[0:-1]:
#         string += item + ', '
#     string += 'and ' + list[-1]
#     print(string)

# # Looping over the index and item value in the list using enumerate()
# def stringed_list(lst):
#     string = ''
#     list_length = len(lst)
    
#     for i, item in enumerate(lst):
#         if i == list_length - 1:
#             string += 'and ' + item
#         else:
#             string += item + ', '
    
#     return string


# print(stringed_list(spam))

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


# j = 0
# while j < len(grid[0]):
#     for i, item in enumerate(grid):
#         print(grid[i][j], end='')
#     j += 1
#     print('')


for y in range(len(grid[0])):        # loop over columns
    for x in range(len(grid)):       # loop over rows
        print(grid[x][y], end='')
    print()



    