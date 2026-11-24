import pprint as p

# The get() method
picnicItems = {'apples': 5, 'cups': 2}
print( 'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.') # Here we set the default value of eggs to zero if egg is not in the dictionary to avoid: 
# print('I am bringing ' + str(picnicItems['eggs']) + ' eggs.') # Key error

# The setdefault() method
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black') # set default color to black if not in dictionary
print(spam)

spam = {'color': 'black', 'age': 5, 'name': 'Pooka'}
spam.setdefault('color', 'white') # color does not change because it already exists
print(spam)


message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
p.pprint(count)
answer = p.pformat(count)  
print(answer)


# # Try to complete this project on your own
# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = '0'
#     else:
#         turn = 'X'
# printBoard(theBoard)


allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for v in guests.values():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))

def displayInventory(inv):
    total = 0
    for key, value in inv.items():
        total = total + value
        print(value, key)
    print('Total number of items:', total)

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory.keys():
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1
    return inventory

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
new_inventory = addToInventory(stuff, dragonLoot)
displayInventory(new_inventory)
