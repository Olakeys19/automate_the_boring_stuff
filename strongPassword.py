import re

passwordRegex = re.compile(r'''
                           ^(?=.{8,}$)                              # must be at least 8 characters
                           (?=.*[a-z])                              # must contain a lowercase letter
                           (?=.*[A-Z])                              # must contain an uppercase letter
                           (?=.*\d)                                 # must contain a digit
                           (?!.*\s).*$                              # should not include any space, tab or newline charcter
                           ''', re.VERBOSE)


def isStrongPassword(password):
    mo = passwordRegex.search(str(password))
    digit = re.compile(r'\w')
    # if mo != None:
    #     print(mo.group())
    if mo == None:
        print('Password must contain a lowercase, uppercase, digit, and must be up to 8 characters')
    else:
        print('Password accepted: ' + str(password))
    

isStrongPassword('***Enisha19***')

startAndEndRegex = re.compile(r'^(Alice|Bob|Carol)(\s)(eats|pets|throws)(\s)(apples|cats|baseball)$')
mo = startAndEndRegex.search('Alice throws baseball')
print(mo.group())

lastNameRegex = re.compile(r'^([A-Z])([a-zA-Z-]*)(\s)(Nakamoto)$')
mo = lastNameRegex.search('Satoshi Nakamoto')
print(mo.group())

commaRegex = re.compile(r'^((\d){,3})(([,])([0-9]{3,3}))*$')
mo = commaRegex.search('1,234')
print(mo.group())

numRegex = re.compile(r'\d+')
mo = numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')
print(mo)

def regexStrip(text, char=None):
    if char == None:
        stripRegex = re.sub(r'^\s+|\s+$', '', text)
    else:
        stripRegex = re.sub(rf'^[{re.escape(char)}]+|[{re.escape(char)}]+$', '', text)
    print(stripRegex)

regexStrip('    I am tired  ')
