# pastFriday13Finder.py - finds all the previous Friday the 13th from the current date

import time, datetime

current_day = datetime.datetime.now()           # create timedate object of the current date
one_day = datetime.timedelta(days=1)            # create a timedelta object of one day

while True:
    try:
        previous_day = current_day - one_day                    # set previous day
        if current_day.strftime('%A %d') == 'Friday 13':        # check if current day is Friday 13
            print(current_day.strftime('%A %d, %B %Y'))         # if it is, print current day along with the montha and year
        current_day = previous_day                              # move to the previos day
    except OverflowError:                                       # The first year is 0001 hence, OverflowError will show if we try to loop before the first year. We will catch this error and stop the loop since we have gotten to the first year
        break