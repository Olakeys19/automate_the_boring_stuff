import os

# os.path.join('usr', 'bin', 'spam') # the os.path.join() function concatenates various path components with exactly one directory separator based on the operating system. It follows each non-empty part except the last path component with a directory separator. The return value is the concatenated path.
# os.getcwd() # the os.getcwd() function returns a string representing the current working directory.
# os.chdir('C:\\Windows\\System32') # the os.chdir() function changes the current working directory to the specified path.

# # The dot (.) and double dot (..) in file paths are used to represent the current directory and the parent directory, respectively. For example, if you are in the directory C:\Users\Olakeys\Documents and you want to access a file in the parent directory, you can use ..\filename.txt. If you want to access a file in the current directory, you can use .\filename.txt.

# os.makedirs('C:\\Users\\Olakeys\\Desktop\\NewFolder') # the os.makedirs() function creates a directory recursively. If the specified path already exists, it raises a FileExistsError.

# myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
# for filename in myFiles:
#     print(os.path.join('C:\\Users\\olakeys', filename))

# # Handling Absolute and Relative Paths
# print(os.path.abspath('.')) # the os.path.abspath() function returns a normalized absolutized version of the pathname path. It computes the absolute path by combining the current working directory with the provided path.
# print(os.path.abspath('.\\Scripts'))
# print(os.path.isabs('.')) # the os.path.isabs() function returns True if the pathname path is an absolute pathname, and False if it is a relative pathname.
# print(os.path.isabs(os.path.abspath('.'))) # the os.path.abspath() function returns an absolute path, so os.path.isabs() will return True for it.
# print(os.path.relpath('C:\\Windows', 'C:\\')) # the os.path.relpath() function returns a relative filepath to path from the current directory or from an optional start point. In this case, it calculates the relative path from C:\ to C:\Windows, which is 'Windows'.
# print(os.path.relpath('C:\\Windows', 'C:\\Users\\Olakeys')) # the os.path.relpath() function calculates the relative path from C:\Users\Olakeys to C:\Windows. To get from C:\Users\Olakeys to C:\Windows, you would need to go up two directories (..\\..) and then down into the Windows directory, resulting in '..\\..\\Windows'.

# path = 'C:\\Windows\\System32\\calc.exe'
# print(os.path.basename(path)) # the os.path.basename() function returns the base name of pathname path. This is the second element of the pair returned by os.path.split(path). In this case, it returns 'calc.exe'.
# print(os.path.dirname(path)) # the os.path.dirname() function returns the directory name of pathname path. This is the first element of the pair returned by os.path.split(path). In this case, it returns 'C:\\Windows\\System32'.
# print(os.path.split(path)) # the os.path.split() function splits the pathname path into a pair, (head, tail) where tail is the last pathname component and head is everything leading up to that. In this case, it returns ('C:\\Windows\\System32', 'calc.exe').

# print(path.split(os.path.sep)) # the os.path.sep variable is the character used by the operating system to separate pathname components. On Windows, it is '\\', and on Unix/Linux/Mac, it is '/'. The path.split(os.path.sep) will split the path into its components based on the separator, resulting in ['C:', 'Windows', 'System32', 'calc.exe'].


# # Finding File Sizes and Folder Contents
# print(os.path.getsize('C:\\Windows\\System32\\calc.exe')) # the os.path.getsize() function returns the size, in bytes, of path. In this case, it returns the size of 'calc.exe'.
# print(os.listdir('C:\\Windows\\System32')) # the os.listdir() function returns a list containing the names of the entries in the directory given by path. In this case, it returns a list of all files and folders in 'C:\\Windows\\System32'.

# totalSize = 0
# for filename in os.listdir('C:\\Windows\\System32'):
#     totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
# print(totalSize)

# Checking Path Validity 
print(os.path.exists('C:\\Windows\\System32\\calc.exe')) # the os.path.exists() function returns True if path refers to an existing path or an open file descriptor, and False otherwise. In this case, it checks if 'calc.exe' exists in 'C:\\Windows\\System32'.
print(os.path.isfile('C:\\Windows\\System32\\calc.exe')) # the os.path.isfile() function returns True if path is an existing regular file. In this case, it checks if 'calc.exe' is a file in 'C:\\Windows\\System32'.
print(os.path.isdir('C:\\Windows\\System32')) # the os.path.isdir() function returns True if path is an existing directory. In this case, it checks if 'C:\\Windows\\System32' is a directory.


# Working with Files
helloFile = open('hello.txt') # the open() function opens a file and returns a corresponding file object. In this case, it opens 'hello.txt' in read mode by default.
helloContent = helloFile.read() # the read() method reads the entire contents of the file as a string. In this case, it reads the contents of 'hello.txt' and stores it in the variable helloContent.
print(helloContent)
helloFile.close()

sonnetFile = open('sonnet29.txt')
print(sonnetFile.readlines())
sonnetFile.close()

# Saving Variables with the shelve Module
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats

print(list(shelfFile.keys())) # the keys() method of a shelve object returns a list of all the keys in the shelve. In this case, it returns ['cats'].
print(list(shelfFile.values())) # the values() method of a shelve object returns a list of all the values in the shelve. In this case, it returns [['Zophie', 'Pooka', 'Simon']].
shelfFile.close()

# The shelve module provides a simple interface to store Python objects in a file. It allows you to save and retrieve data using a dictionary-like syntax. When you open a shelve file, it creates a persistent dictionary that can be used to store and retrieve data across different runs of the program. You can use the keys() and values() methods to access the keys and values stored in the shelve, just like you would with a regular dictionary.

# The shelve module is a convenient way to store and retrieve Python objects without having to worry about the underlying file handling. It abstracts away the complexities of file I/O and allows you to work with data in a more intuitive way. You can use it to save variables, lists, dictionaries, or any other Python objects that you want to persist across program runs. Just remember to close the shelve file when you're done to ensure that all changes are saved properly.

# Saving Variables with the pprint.pformat() Function
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby', 'religion': 'Catholic', 'color': 'black'}, {'name': 'Pooka', 'desc': 'fluffy', 'religion': 'Protestant', 'color': 'white'}]
pprint.pformat(cats) # the pprint.pformat() function returns a formatted string representation of the object passed to it. In this case, it returns a string that represents the list of dictionaries in a more readable format.
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n') # the write() method of a file object writes a string to the file. In this case, it writes the string 'cats = ' followed by the formatted string representation of the cats list, and then a newline character.
fileObj.close()
