#TODO: Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. The results should be printed to the screen.

import re, os, pprint

textExt = re.compile(r'.txt$')
userRe = input(r'Enter a regular expression to search for: ').strip()
userRegex = re.compile(userRe)


# Navigate to folder
folder_dir = input(r'Enter a folder directory: ').strip()

# Loop through all .txt files in the folder
try:
    for item in os.listdir(f'{folder_dir}'): # loop through all files and folders in the specified folder directory.
        basename = os.path.basename(item) # return the base name of each item in the folder.
        mo1 = textExt.search(basename) # search for the regular expression pattern defined by textExt in the base name of each item. If the pattern is found, mo1 will be a match object; otherwise, it will be None.

        if mo1 != None: # if mo1 is not None, it means that the base name of the item matches the regular expression pattern for .txt files.
            with open(basename, 'r', encoding='utf-8') as f_obj: # open the .txt file in read mode with UTF-8 encoding.
                text = f_obj.readlines() # read all lines from the file and store them in the variable text as a list of strings, where each string represents a line from the file.
                for line in text:
                    # search for any line that matches a regular expression
                    mo2 = userRegex.findall(line)
                    if mo2 != []:
                        print(f'Found ({userRe}): {mo2} in {basename} line {text.index(line)+1}')
except FileNotFoundError:
    print('Please enter a valid directory')




                
                
                