# keyword Arguments and print()
# Case 1:
# end keyword argument
print('Hello')
print('World')

print('Hello', end='')
print('World')
# This shows that the print() function has a default end keyword argumrnt end=/n

# Case 2
# sep keyword argument
print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep=',')
# This shows that the print() function has a default sep keyword argument sep=' '

