# # # THE TIME MODULE
# # import time

# # # # Returning the Epoch Timestamp
# # # # The Unix epoch is a time reference commonly used in programming: midnight on January 1, 1970, Coordinated Universal Time (UTC). The time.time() function returns the number of seconds since that moment as a float value.

# # # print(time.time())  # Number of seconds since January 1, 1970 till current date
# # # print(time.ctime()) # Returns a string of the current date and time
# # # this_moment = time.time()
# # # print(time.ctime(this_moment))

# # # # Using Epoch timestamps to profile code
# # # # Measure how long it takes to multiply 100,000 numbers.
# # # import time
# # # def calculate_product():
# # #     # Calculate the product of the first 100,000 numbers.
# # #     product = 1
# # #     for i in range(1, 100001):
# # #         product = product * i
# # #     return product

# # # start_time = time.time()    # call time.time() before running the program
# # # result = calculate_product()    # run the program
# # # end_time = time.time()      # call time.time() after running the program
# # # print(f'It took {end_time - start_time} seconds to calculate.')


# # # Pausing programs with the time.sleep() function
# # import time
# # for i in range(3):
# #     print('Tick')       # print tick
# #     time.sleep(1)       # pause for 1 second
# #     print('Tock')       # print tock
# #     time.sleep(1)       # pause for 1 second

# # time.sleep(5)       # don't end the program until after five seconds



# # THE DATETIME MODULE
# import datetime
# print(datetime.datetime.now())      # show the current date and  accotding to your computer's clock

# dt = datetime.datetime(2026, 10, 21, 16, 29, 0) # arguments: year, month, day, hour, minute, second
# print(dt.year, dt.month, dt.day)
# print(dt.hour, dt.minute, dt.second)

# # Converting Unix epoch timestamp to datetime object
# import datetime, time
# epochToDateTime = datetime.datetime.fromtimestamp(time.time())
# print(epochToDateTime)

# print(datetime.datetime.fromtimestamp(1000000))     # get the date for 1000000 seconds after the Unix epoch


# # Comparing datetime objects
# halloween_2026 = datetime.datetime(2026, 10, 31, 0, 0, 0)
# new_years_2027 = datetime.datetime(2027, 1, 1, 0, 0, 0)
# oct_31_2026 = datetime.datetime(2026, 10, 31, 0, 0, 0)
# print(halloween_2026 == oct_31_2026)    # True because both datetime objects are equal
# print(halloween_2026 > new_years_2027)  # False because new_years_2027 > halloween_2026
# print(new_years_2027 > halloween_2026)
# print(new_years_2027 != oct_31_2026)


# # Representing Duration
# # The timedelta data type represents a duration of time rather than a moment in time
# delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8) # store the time object in delta
# print(delta.days, delta.seconds, delta.microseconds)    # timedelta represents time in days, seconds and microseconds
# print(delta.total_seconds())        # represent the total time in seconds only
# print(str(delta))       # represent the time as a nicely formatted, human readable string of the time object

# # Arithmetic operations on datetime values
# now = datetime.datetime.now()           # store the current date and time as a datetime object
# print(now)
# thousand_days = datetime.timedelta(days=1000)   # make a timedelta object for 1000 days
# print(thousand_days)
# print(now + thousand_days)  # add now and thousand_days together to get a datetime object for 1000 days from now

# oct_21st = datetime.datetime(2026, 10, 21, 16, 29, 0)
# about_thirty_years = datetime.timedelta(days=365 * 30)
# print(oct_21st)
# print(oct_21st - about_thirty_years)
# print(oct_21st - (2 * about_thirty_years))


# # # Pausing until a specific date
# # import datetime, time
# # halloween_2027 = datetime.datetime(2027, 10, 31, 0, 0, 0)
# # while datetime.datetime.now() < halloween_2027:
# #     time.sleep(1)


# # Converting datetime objects into strings
# #  Use the strftime() method to display a datetime object as a string. (The f in the name of the strftime() function stands for format.)
# """
# # strftime() directives
# %Y  -   Year with century, as in '2014'
# %y  -   Year without century, '00' to '99' (2000 to 2099)
# %m  -   Month as a decimal number, '01' to '12'
# %B  -   Full month name, as in 'November'
# %b  -   Abbreviated month name, as in 'Nov'
# %d  -   Day of the month, '01' to '31'
# %j  -   Day of the year, '001' to '366'
# %w  -   Day of the week, '0' (Sunday) to '6' (Saturday)
# %A  -   Full weekday name, as in 'Monday'
# %a  -   Abbreviated weekday name, as in 'Mon'
# %H  -   Hour (24-hour clock), '00' to '23'
# %I  -   Hour (12-hour clock), '01' to '12'
# %M  -   Minute, '00' to '59'
# %S  -   Second, '00' to '59'
# %p  -   'AM' or 'PM' 
# # %%  -   Literal '%' character

# """
# oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
# print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
# print(oct21st.strftime('%I:%M %p'))
# print(oct21st.strftime("%B of '%y"))


# # Converting strings into date time objects using strptime()
# # The strptime() function is the inverse of the strftime() method. A custom format string using the same directives as strftime() must be passed so that strptime() knows how to parse and understand the string. (The p in the name of the strptime() function stands for parse.)
# print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
# print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
# print(datetime.datetime.strptime("October of '15", "%B of '%y"))
# print(datetime.datetime.strptime("November of '63", "%B of '%y"))

# # To get a datetime object from the string 'October 21, 2015', pass 'October 21, 2015' as the first argument to strptime() and the custom format string that corresponds to 'October 21, 2015' as the second argument u. 
# # NOTE: The string with the date information must match the custom format string exactly, or Python will raise a ValueError exception



# # MULTITHREADING
# import threading, time
# # print('Start of program')

# # def takeANap():
# #     time.sleep(5)
# #     print('Wake up!')

# # threadObj = threading.Thread(target=takeANap)
# # threadObj.start()

# # print('End of program')

# # Passing Arguments to the Thread’s Target Function
# # Example
# """
# Say, we wanted to run the function below as a thread
# print('cats', 'dogs', 'frogs', sep=' & ')

# # This print() call has three regular arguments, 'Cats', 'Dogs', and 'Frogs', and one keyword argument, sep=' & '
# # The regular arguments can be passed as a list to the args keyword argument in threading.Thread(). The keyword argument can be specified as a dictionary to the kwargs keyword argument in threading.Thread().

# """
# threadObj = threading.Thread(target=print, args=['cats', 'dogs', 'frogs'], kwargs={'sep': ' & '})
# threadObj.start()


# LAUNCHING OTHER PROGRAMS FROM PYTHON
import subprocess
# # subprocess.run(['C:\\Windows\\System32\\calc.exe'])
# calc_proc = subprocess.Popen(['C:\\Windows\\System32\\calc.exe'])
# # The return value is a Popen object, which has two useful methods: poll() and wait().
# # The poll() method will return None if the process is still running at the time poll() is called. If the program has terminated, it will return the process’s integer exit code. 
# #  The wait() method will block until the launched process has terminated. This is helpful if you want your program to pause until the user finishes interacting with the other program. The return value of wait() is the process’s integer exit code.

# print(calc_proc.poll() == None)
# print(calc_proc.wait()) # Doesn't return until Calculator closes
# print(calc_proc.poll())

# paint_proc = subprocess.Popen('F:\\Program Files\\Image-Line\\FL Studio 2024\\FL64.exe')
# paint_proc.kill()
# # Note that the kill() method immediately terminates a program and bypasses any “Are you sure you want to quit?” confirmation window. Any unsaved work in the program will be lost.


# # Passing Command Line Arguments to Processes
# subprocess.run(['C:\\Windows\\notepad.exe', 'C:\\Users\\ogoay\\OneDrive\\Desktop\\python_work\\hello.txt'])     # open notepad, then load hello.txt


# # Receiving Output Text from Launched Commands
# import subprocess
# proc = subprocess.run(['ping', '-n', '4', 'nostarch.com'], capture_output=True, text=True)
# print(proc.stdout)


# Opening Files with Default Applications
file_obj = open('hello.txt', 'w')  # Create a hello.txt file.
file_obj.write('Hello, world!')
file_obj.close()

import subprocess
subprocess.run(['start', 'hello.txt'], shell=True)      # open hello.txt with default app