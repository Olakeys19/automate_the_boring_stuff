# The global statement
# If you need to modify a global variable from within a function, use the global statement
eggs = 'global'
def spam():
    global eggs
    eggs = 'spam'

spam()
print(eggs)