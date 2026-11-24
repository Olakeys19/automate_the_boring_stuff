import re

# Using regular expressions in Python
# 1. Import the regex module with import re.
# 2. Create a Regex object with the re.compile() function. (Remember to use a raw string.)
# 3. Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
# 4. Call the Match object’s group() method to return a string of the actual matched text

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print('Phone number found: ' + mo.group())

# Grouping with parentheses
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group(0))
# print(mo.group())
# print(mo.groups()) # returns a tuple of all the groups in the regex
# areaCode, mainNumber = mo.groups()
# print(areaCode)
# print(mainNumber)

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') # using \( and \) escape characters to match literal parentheses
mo = phoneNumRegex.search('My number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))

# Matching multiple groups with the Pipe (|)
heroRegex = re.compile(r'Batman|Tina Fey') # the | character is used to match either Batman or Tina Fey. It returns the first match it finds in the searched string.
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())
mo3 = heroRegex.findall('Batman and Tina Fey') # finding all matches of Batman and Tina Fey in the searched string. It returns a list of all matches found.
print(mo3)

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') # using parentheses to group the alternatives in the regex. The group() method will return the text that matched the part of the regex inside the parentheses.
mo = batRegex.search('Batman lost a wheel')
print(mo.group())
print(mo.group(1))

# Optional matching with the Question Mark
batRegex = re.compile(r'Bat(wo)?man') # the (wo)? part of the regex means that the wo is optional. The regex will match both Batman and Batwoman.
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') # the (\d\d\d-)? part of the regex means that the area code is optional. The regex will match both 415-555-4242 and 555-4242.
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

# Matching zero or more with the Star
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())  
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

# Matching one or more with the Plus
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1 == None) # the search() method returns None if it doesn’t find a match. So we can check if mo1 is None to see if the regex found a match or not.
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman') 
print(mo3.group())

# Matching specific repetitions with Curly Brackets
haRegex = re.compile(r'(Ha){3}') # The regex will match only the first 3 Ha’s in a row, even if there are more than 3 Ha’s in the searched string. It will return None if there are not at least 3 Ha’s in a row in the searched string.
mo1 = haRegex.search('HaHaHa')  
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 == None) # the search() method returns None if it doesn’t find a match. So we can check if mo2 is None to see if the regex found a match or not.

print()
haRegex2 = re.compile(r'(Ha){3,5}') # The regex will match the first 3 to 5 Ha’s in a row, even if there are more than 5 Ha’s in the searched string. It will return None if there are not at least 3 Ha’s in a row in the searched string.
mo1 = haRegex2.search('HaHaHa') 
print(mo1.group())
mo2 = haRegex2.search('HaHaHaHaHaHaHa') 
print(mo2.group())

haRegex3 = re.compile(r'(Ha){,5}') # The regex will match the first 0 to 5 Ha’s in a row, even if there are more than 5 Ha’s in the searched string. It will return an empty string if there are not at least 0 Ha’s in a row in the searched string.
mo1 = haRegex3.search('HaHaHa') 
print(mo1.group())
mo2 = haRegex3.search('oh')
print(mo2.group())

haRegex4 = re.compile(r'(Ha){3,}') # The regex will match the first 3 or more Ha’s in a row. It will return None if there are not at least 3 Ha’s in a row in the searched string.
mo1 = haRegex4.search('HaHaHaHaHa')
print(mo1.group())
mo2 = haRegex4.search('HaHa')
print(mo2 == None) # the search() method returns None if it doesn’t find a match. So we can check if mo2 is None to see if the regex found a match or not.

# Greedy vs Nongreedy Matching
print()
print('Greedy vs Nongreedy Matching')
greedyHaRegex = re.compile(r'(Ha){3,5}') # Greedy matching: The regex will match the longest string that matches the regex. In this case, it will match the first 5 Ha’s in a row, not 3 or 4.
mo1 = greedyHaRegex.search('HaHaHaHaHaHaHa')    
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?') # Nongreedy matching: The regex will match the shortest string that matches the regex. In this case, it will match the first 3 Ha’s in a row, not 4 or 5.
mo2 = nongreedyHaRegex.search('HaHaHaHaHaHaHa')
print(mo2.group())


# The findall() method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group()) # the search() method returns only the first match of the regex in the searched string.

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo) # the findall() method returns a list of strings of every match of the regex in the searched string, instead of just one match like the search() method. The findall() method will not return a list if there is only one match of the regex in the searched string. It will return a string instead.

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo) # if the regex has groups, the findall() method will return a list of tuples. Each tuple contains the strings for the groups in the regex. If there is only one group, the findall() method will return a list of strings instead of a list of tuples.

# Character classes
# 1. \d - any numeric digit from 0 to 9
# 2. \D - any character that is not a numeric digit from 0 to 9
# 3. \w - any letter, numeric digit, or the underscore character. 
# 4. \W - any character that is not a letter, numeric digit, or the underscore character. 
# 5. \s - any space, tab, or newline character.
# 6. \S - any character that is not a space, tab, or newline character.
xmasRegex = re.compile(r'\d+\s\w+') # the \d+ means one or more numeric digits, the \s means a space, and the \w+ means one or more word characters. So this regex will match strings like '12 drummers', '11 pipers', '10 lords', etc.
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)

# Making your own character classes with square brackets []
vowelRegex = re.compile(r'[aeiouAEIOU]') # the [aeiouAEIOU] character class matches any vowel, both lowercase and uppercase.
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.') 
print(mo)

consonantRegex = re.compile(r'[^aeiouAEIOU]') # The ^ character at the beginning of the character class means "not".
mo = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

# The caret (^) and dollar sign ($) characters
beginsWithHello = re.compile(r'^Hello') # the ^ character at the beginning of the regex means that the string must begin with 'Hello' for a match to be found.
mo1 = beginsWithHello.search('Hello world!')
print(mo1.group())
mo2 = beginsWithHello.search('He said Hello.')
print(mo2 == None) 

endsWithNumber = re.compile(r'\d$') # the $ character at the end of the regex means that the string must end with a numeric digit for a match to be found.
mo1 = endsWithNumber.search('Your number is 42')
print(mo1.group())
mo2 = endsWithNumber.search('Your number is forty two.')
print(mo2 == None)

wholeStringIsNum = re.compile(r'^\d+$') # the ^ character at the beginning and the $ character at the end of the regex means that the entire string must be made up of one or more numeric digits for a match to be found.
mo1 = wholeStringIsNum.search('1234567890')
print(mo1.group())
mo2 = wholeStringIsNum.search('12345xyz67890')
print(mo2 == None)
mo3 = wholeStringIsNum.search('12 34567890')
print(mo3 == None)

# The wildcard character (.)
atRegex = re.compile(r'.at') # the . character matches any character (only one) except a newline. So this regex will match strings like 'cat', 'hat', 'rat', etc.
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

# Matching everything with the Dot-Star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') # the .* means "match any character (except a newline) zero or more times". So this regex will match any string that has 'First Name: ' followed by any characters, followed by ' Last Name: ' followed by any characters. The parentheses around the .* parts of the regex mean that the group() method will return the text that matched those parts of the regex.
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

nongreedyRegex = re.compile(r'<.*?>') # the .*? means "match any character (except a newline) zero or more times, but as few characters as possible". So this regex will match the smallest string that starts with '<' and ends with '>'.
mo = nongreedyRegex.search('<To serve humans> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>') 
mo = greedyRegex.search('<To serve humans> for dinner.>')
print(mo.group()) 

print()
# Matching newlines with the Dot character
noNewlineRegex = re.compile('.*') 
mo1 = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo1.group()) 
print()

newlineRegex = re.compile('.*', re.DOTALL) # the re.DOTALL argument to re.compile() will make the . character match any character, including a newline.
mo2 = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo2.group())
print()

# Case-Insensitive Matching
robocop = re.compile(r'robocop', re.I) # the re.I OR re.IGNORECASE argument to re.compile() will make the regex case-insensitive, so it will match 'robocop', 'ROBOCOP', 'Robocop', etc.
mo1 = robocop.search('Robocop is part man, part machine, all cop.')
print(mo1.group())

mo2 = robocop.search('ROBOCOP protects the innocent.')
print(mo2.group())

mo3 = robocop.search('Al, why does your programming book talk about robocop so much?')
print(mo3.group())
print()

# Substituting Strings with the sub() method
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo) # the sub() method will replace any matches of the regex in the searched string with the string provided as the first argument to sub().

agentNamesRegex = re.compile(r'Agent (\w)\w*') # the (\w) part of the regex will match the first letter of the agent's name and save it as a group. The \w* part of the regex will match the rest of the agent's name, but it will not be saved as a group because it is not inside parentheses.

mo = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol about Agent Bob\'s mission.') # the \1 in the replacement string means "the text that was matched by group 1 in the regex". So this will replace the agent's name with the first letter of their name followed by four asterisks.
print(mo)

# Managing Complex Regexes with the re.VERBOSE flag
# The re.VERBOSE argument to re.compile() will allow you to add whitespace and comments to the regex string, which can make it easier to read and understand. The regex will ignore any whitespace and comments in the regex string.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE) # you can combine the re.IGNORECASE, re.DOTALL, and re.VERBOSE flags with the | character in the second argument to re.compile(). The | in this case is called the bitwise OR operator, and it will combine the three flags into a single value that can be passed to re.compile().
