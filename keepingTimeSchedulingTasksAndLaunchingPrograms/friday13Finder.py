# friday13Finder.py - finds the next ten friday the 13th 

import time, datetime

i = 1

current_day = datetime.datetime.now()           # create a datetime object for the current day
one_day = datetime.timedelta(days=1)            # create a timedelta object for one day

while i < 11:                              # run the loop ten times since i has been set to 1
    next_day = current_day + one_day       # set the next day value
    if current_day.strftime('%A %d') == 'Friday 13':        # check if the current day is Friday 13
        print(current_day.strftime('%A %d, %B %Y'))         # if current day is Friday 13, print the month and year
        i += 1      # add an increment of 1 to i for each friday 13 found
    current_day = next_day      # move to the next day after each iteration

