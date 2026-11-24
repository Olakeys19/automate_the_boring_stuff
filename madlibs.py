# Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this: The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.

import shelve, os

def checkTerm(term):
    global text
    capterm = term.upper()
    lowterm = term.lower()
    if capterm in text:
        if lowterm[0] in ['a', 'e', 'i', 'o', 'u']:
            replacement = input(f'Enter an {term}: ')
            text = text.replace(term.upper(), replacement, 1)
        else:
            replacement = input(f'Enter a {term}: ')
            text = text.replace(term.upper(), replacement, 1)
    else: 
        return None
    
    return text
        

terms = ['adjective', 'noun', 'adverb', 'verb']

filename = input('Enter a text file directory: ')
with open(filename, 'r') as f_obj:
    text = f_obj.read()


while True:
    for term in terms:
        checkTerm(term)
    if all(checkTerm(term) == None for term in terms):
        print()
        break


print(f'The modified text is: \n{text}')
print()

if os.path.dirname(os.path.abspath(filename)) == os.getcwd():
    with open(f'mod_{filename}', 'w') as f_obj:
        f_obj.write(text + '\n')
else:
    with open(rf'{os.path.dirname(filename)}{os.path.sep}mod_{os.path.basename(filename)}', 'w') as f_obj:
        f_obj.write(text + '\n')

print('The modified file has been saved in the orignal directory of the text file')

