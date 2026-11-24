# Escape Characters \
# An escape character lets you use characters that are otherwise impossible to put into a string.
# print('The boy's mother is a cow') will not work becuase of the single quotes
print('The boy\'s mother is a cow') # We use \ to escape the issue above, use \\ if you mean backslash not escape

# Raw Strings
# You can place an r before the beginning quotation mark of a string to make it a raw string. 
# A raw string completely ignores all escape characters and prints any backslash that appears in the string.
print(r'The boy\'s mother is a cow')

# Multiline Strings and comments with triple Quotes
print('''Dear Alice,
      
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
      
Sincerely,
Bob''')

# The isX String Methods
'''
1. .isupper() returns true if a string is in upper case
2. .islower() returns true if a string is in lower case
3. .isalpha() returns True if the string consists only of letters and is not blank.
4. .isalnum() returns True if the string consists only of letters and numbers and is not blank.
5. .isdecimal() returns True if the string consists only of numeric characters and is not blank.
6. .isspace() returns True if the string consists only of spaces, tabs, and new lines and is not blank.
7. .istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.
'''
print(('\n\t hi').isspace())

# The startswith() and endswith() methods check if a string starts or ends wuth a specified string respectively

# The join() and split() methods 

# The join method is called on a string value and is passed a list of string to join them with the specified string value

# The split method is called on a string and returns a list where the string is split by a specified condition
print('My name is Simon'.split(' '))


# Justifying Text with rjust(), ljust(), and center()
# The rjust() and ljust() string methods return a padded version of the string they are called on, with spaces inserted to justify the text. The first argument to these methods is an integer length for the justified string. An optional second argument will specify a fill character other than a space character

print('Hello'.rjust(10, '*'))
print('Hello'.ljust(20, '-'))
# The center() string method works like ljust() and rjust() but centers the text rather than justifying it to the left or right
print('Hello'.center(20, '-'))

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# The strip(), rstrip(), and lstrip() methods are used to remove whitespace