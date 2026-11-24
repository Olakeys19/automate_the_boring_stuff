# A simple stopwatch program
import time

# Display the program's instructions
print('Press ENTER to begin and to mark laps. Ctrl-C quits')
input() # Press Enter to begin
print('Started')
startTime = time.time() # Get the first lap's start time
lastTime = startTime
lapNumber = 1

# Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f'Lap #{lapNumber}: {totalTime}({lapTime})', end='')
        lapNumber += 1
        lastTime = time.time()  # Reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone')