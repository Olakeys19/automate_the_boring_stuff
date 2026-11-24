# # # CONTROLLING MOUSE MOVEMENT AND CLICKS
# # # PyAutoGUI’s mouse functions use x- and y-coordinates. The origin, where x and y are both zero, is at the upper-left corner of the screen. The x-coordinates increase going to the right, and the y-coordinates increase going down. All coordinates are positive integers; there are no negative coordinates.

# # import pyautogui
# # screen_size = pyautogui.size()  # Obtain the screen resolution.
# # screen_size 
# # screen_size[0], screen_size[1]      # Access the width and height
# # screen_size.width, screen_size.height   # Access the width and height using attributes
# # tuple(screen_size)      # Convert the Size object to a tuple


# # # Moving the Mouse 
# # # The pyautogui.moveTo() function will instantly move the mouse cursor to a specified position on the screen. Integer values for the x- and y-coordinates make up the function’s first and second arguments, respectively. An optional duration integer or float keyword argument specifies the number of seconds it should take to move the mouse to the destination. If you leave it out, the default is 0 for instantaneous movement. (All of the duration keyword arguments in PyAutoGUI functions are optional.) 

# # import pyautogui
# # # pyautogui.moveTo() function will move the mouse cursor to a specified position on the screen.
# # for i in range(10):  # Move the mouse in a square.
# #     pyautogui.moveTo(100, 100, duration=0.25)
# #     pyautogui.moveTo(200, 100, duration=0.25)
# #     pyautogui.moveTo(200, 200, duration=0.25)
# #     pyautogui.moveTo(100, 200, duration=0.25)

# # # pyautogui.move() function will move the mouse cursor relative to its current position. The first argument is the number of pixels to move the mouse cursor horizontally, and the second argument is the number of pixels to move it vertically. Positive values move the cursor right and down, while negative values move it left and up.

# # import pyautogui
# # for i in range(10):
# #     pyautogui.move(100, 0, duration=0.25)  # Right
# #     pyautogui.move(0, 100, duration=0.25)  # Down
# #     pyautogui.move(-100, 0, duration=0.25)  # Left
# #     pyautogui.move(0, -100, duration=0.25)  # Up


# # # Getting the Current Position
# # pyautogui.position()  # Get the current mouse position.
# # p = pyautogui.position()  # And again
# # p[0]  # The x-coordinate is at index 0.
# # p.x  # The x-coordinate is also in the x attribute.


# # Controlling Mouse Interaction
# # Clicking
# import pyautogui
# pyautogui.click()  # Click the mouse at its current location, it uses left click by default. You can also specify the x- and y-coordinates of the click as arguments to the click() function. The click() function is a combination of the mouseDown() and mouseUp() functions, which press and release the mouse button, respectively.

# pyautogui.click(10, 5)  # Move the mouse to (10, 5) and click. An optional third argument button='left', 'middle' or 'right' can be used to specify which mouse button to click. The default is left.

# # As a further convenience, the pyautogui.doubleClick() function will perform two clicks with the left mouse button. The pyautogui.rightClick() and pyautogui.middleClick() functions will perform a click with the right and middle mouse buttons, respectively.


# # Dragging
# # PyAutoGUI provides the pyautogui.dragTo() and pyautogui.drag() functions to drag the mouse cursor to a new location or a location relative to its current one. The arguments for dragTo() and drag() are the same as moveTo() and move(): the x-coordinate/horizontal movement, the y-coordinate/vertical movement, and an optional duration of time.

# import pyautogui
# pyautogui.sleep(5)
# pyautogui.click()  # Click to make the window active.
# distance = 300
# change = 20
# while distance > 0:
#    pyautogui.drag(distance, 0, duration=0.2)  # Move right.
#    distance = distance - change
#    pyautogui.drag(0, distance, duration=0.2)   # Move down.
#    pyautogui.drag(-distance, 0, duration=0.2)  # Move left.
#    distance = distance - change
#    pyautogui.drag(0, -distance, duration=0.2)  # Move up.


# # Scrolling
# pyautogui.scroll(200)       # Scroll up 200 “clicks” (the mouse wheel is moved 200 notches).
# pyautogui.scroll(-200)      # Scroll down 200 “clicks” (the mouse wheel is moved 200 notches).


# # Planning Your Mouse Movements
# # The pyautogui.mouseInfo() function will display a small window that shows the current mouse cursor’s x- and y-coordinates, the RGB color value of the pixel under the cursor, and the name of the window that is currently under the cursor. This is useful for planning your mouse movements and clicks. You can run this function in a separate Python shell or script while you are running your main program.



# # Taking Screenshots
# import pyautogui
# im = pyautogui.screenshot()         # Take a screenshot of the entire screen and save it to the im variable.

# pyautogui.pixel(0, 0)   #   Get the RGB color value of the pixel at (0, 0).

# # PyAutoGUI’s pixelMatchesColor() function will return True if the pixel at the given x- and y-coordinates on the screen matches the given color. The first and second arguments are integers for the x- and y-coordinates, and the third argument is a tuple of three integers for the RGB color the screen pixel must match

# pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))       # Returns True if the pixel at (50, 200) is the color (130, 135, 144).
# pyautogui.pixelMatchesColor(0, 0, (117, 117, 117))  # Returns True if the pixel at (0, 0) is the color (117, 117, 117).


# # Image Recognition
# import pyautogui
# box = pyautogui.locateOnScreen('Screenshot.png')  # Returns a Box object with the coordinates of where the image is found on the screen.
# box.left, box.top, box.width, box.height  # Access the Box object’s attributes
# box[0]  #  Access the Box object’s left attribute using an index

# list(pyautogui.locateAllOnScreen('Screenshot.png'))     # Returns a list of Box objects for every instance of the image found on the screen. 

# pyautogui.click((643, 745, 70, 29))    # Click the center of the region defined by the Box object returned by locateOnScreen(). The click() function can take a Box object as an argument, and it will click the center of that box.

# pyautogui.click('Screenshot.png')    # Click the center of the first instance of the image found on the screen. The click() function can take a string filename as an argument, and it will locate the image on the screen and click its center.

# try:
#     location = pyautogui.locateOnScreen('Screenshot.png')
# except pyautogui.ImageNotFoundException:
#     print('Image could not be found.')



# # GETTING WINDOW INFORMATION
# # Obtaining the Active Window
# import pyautogui
# pyautogui.getActiveWindow()   # Returns a Window object for the currently active window. If no windows are open, it returns None.


# import pyautogui
# active_win = pyautogui.getActiveWindow()     # Returns a Window object for the currently active window. If no windows are open, it returns None.
# str(active_win)      # Returns a string representation of the Window object, including its title, size, and coordinates.
# active_win.title  #  Returns the title of the active window as a string.
# active_win.size   #  Returns a Size object with the width and height of the active window.
# active_win.left, active_win.top, active_win.right, active_win.bottom    #  Returns the coordinates of the active window’s edges as integers.
# active_win.topleft  #  Returns the top-left corner of the active window as a Point object.
# pyautogui.click(active_win.left + 10, active_win.top + 20)     # Click 10 pixels to the right and 20 pixels down from the top-left corner of the active window. The click() function can take a Point object as an argument, and it will click that point on the screen.


# # Finding Windows with Other Functions
# """
# pyautogui.getAllWindows() Returns a list of Window objects for every visible window on the screen

# pyautogui.getWindowsAt(x, y) Returns a list of Window objects for every visible window that includes the point (x, y)

# pyautogui.getWindowsWithTitle(title) Returns a list of Window objects for every visible window that includes the string title in its title bar

# PyAutoGUI also has a pyautogui.getAllTitles() function, which returns a list of strings of every visible window.
# """


# # Manipulating Windows
# # Resizing and Moving Windows
# import pyautogui
# active_win = pyautogui.getActiveWindow() 
# active_win.width     # Gets the current width of the window
# active_win.topleft  # Gets the current position of the window
# active_win.width = 1000  # Resizes the width
# active_win.topleft = (800, 400)  # Moves the window

# # Minimizing, Maximizing, and Restoring Windows
# import pyautogui
# active_win = pyautogui.getActiveWindow()
# active_win.isMaximized  # Returns True if the window is maximized
# active_win.isMinimized  # Returns True if the window is minimized
# active_win.isActive  # Returns True if the window is the active window

# active_win.maximize()  # Maximizes the window
# active_win.isMaximized
# active_win.restore()  # Undoes a minimize/maximize action
# active_win.minimize()  # Minimizes the window


# import time
# # Waits 5 seconds while you activate a different window:
# time.sleep(5); active_win.activate()      # Activates the window you were typing in before the 5-second wait. If the window is minimized, it will be restored and activated.
# active_win.close()  # This will close the window you're typing in.


# # CONTROLLING THE KEYBOARD
# # PyAutoGUI’s keyboard functions send virtual keypresses to the operating system, which then sends them to the active window. The active window is the one that is currently selected and ready to receive keyboard input. You can use the pyautogui.getActiveWindow() function to get a Window object for the active window, and then call its activate() method to make it active.

# # Sending Key Press Strings
# import pyautogui
# pyautogui.click(100, 200); pyautogui.write('Hello, world!')

# # Notice how placing two commands on the same line, separated by a semicolon, keeps the interactive shell from prompting you for input between running the two instructions. This prevents you from accidentally bringing a new window into focus between the click() and write() calls, which would mess up the example.

# pyautogui.write('Hello, world!', 0.25)  # The second argument is the number of seconds to wait between each keypress. The default is 0, which means no delay between keypresses. You can also use a float value for the delay, such as 0.25 for a quarter-second delay.


# # Specifying Key Names
# pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])    # Types the letters a and b, presses the left arrow key twice, and then types X and Y. The key names are case-sensitive. The letters a and b are lowercase, while X and Y are uppercase. The left arrow key is specified as 'left'. You can also use 'up', 'down', 'right', 'enter', 'esc', 'backspace', 'delete', 'home', 'end', 'pageup', 'pagedown', 'tab', and many other keys. See the PyAutoGUI documentation for a complete list of key names.


# # Pressing and Releasing the Keyboard
# pyautogui.press('enter')  # Presses the enter key
# pyautogui.keyDown('shift')  # Holds down the shift key
# pyautogui.keyUp('shift')  # Releases the shift key

# pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')    # this will type a dollar sign ($) on most keyboards. The dollar sign is typed by holding down the shift key and pressing the 4 key. The keyDown() and keyUp() functions can be used to hold down and release any key, including modifier keys like shift, ctrl, and alt


# # Running Hotkey Combinations
# pyautogui.hotkey('ctrl', 'c')  # Presses the ctrl and c keys at the same time, which is the keyboard shortcut for copying text. The hotkey() function can take any number of key names as arguments, and it will press them all at the same time. You can also use a list of key names as an argument, such as pyautogui.hotkey(['ctrl', 'c']).


# Setting Up GUI Automation Scripts
import pyautogui
pyautogui.sleep(3)  # Pauses the program for 3 seconds
pyautogui.countdown(10)  # Counts down over 10 seconds
print('Starting in ', end=''); pyautogui.countdown(3)


# Displaying Message Boxes
pyautogui.alert('This is an alert box.')  # Displays a simple alert box
pyautogui.confirm('Do you want to continue?')  # Displays a confirmation box and returns 'OK' or 'Cancel'
pyautogui.prompt('What is your name?')  # Displays a prompt box and returns the user's input
pyautogui.password('Enter your password')  # Displays a password box and returns the user's input, but the input is hidden with asterisks