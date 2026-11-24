# Opening a file in read mode
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents) 

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)


with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines: 
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
print(float(pi_string))
print(pi_string)


# Opening a file in write mode
# NOTE: In write mode, python erases the file before writing
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming. \n")

# filename = 'message.py'
# with open(filename, 'w') as file_object:
#     file_object.write("filename = 'programming.txt' \n\twith open(filename, 'w') as file object: \n\tfile_object.write('I love programming')")


# Opening a file in Append Mode
# NOTE: In append mode, python begins writing at the end of the file instead of clearing the file as in write mode
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")



