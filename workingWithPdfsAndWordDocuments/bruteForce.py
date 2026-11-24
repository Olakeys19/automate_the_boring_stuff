#! python3
# bruteForce.py - uses the words in dictionary.txt to try to crack the password of encrypted pdfs

import pypdf

with open('dictionary.txt', 'r') as f_obj:                          # open the dictionary.txt file containing 44000 English words
    words = f_obj.read()                                            
    word_list = words.split('\n')
    # print(word_list)

pdfFile = open('encryptedminutes.pdf', 'rb')                               
reader = pypdf.PdfReader(pdfFile)

for word in word_list:
    if (reader.decrypt(word)) == 2:                                 # if decrypt() returns 2, then the password is correct
        print('Password is {word}')
        break
    elif reader.decrypt(word.lower()) == 2:
        print(f'Password is {word.lower()}')
        break




