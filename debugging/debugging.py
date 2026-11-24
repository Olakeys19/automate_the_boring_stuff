# # Raising Exceptions
# raise Exception('This is the error message.')

# # Getting the Traceback as a String
# import traceback
# try:
#     raise Exception('This is the error message.')
# except:
#     errorFile = open('errorInfo.txt', 'w')
#     errorFile.write(traceback.format_exc()) # traceback.format_exc() returns a string of the traceback info
#     errorFile.close()
#     print('The traceback info was written to errorInfo.txt')


# # Assertions
# podBayDoorStatus = 'open'
# assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".' # If the assertion fails, an AssertionError exception is raised with the message 'The pod bay doors need to be "open".'
# podBayDoorStatus = 'closed'
# assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".' # This will raise an AssertionError exception with the message 'The pod bay doors need to be "open".' because the assertion fails.

# # Disabling Assertions
# # You can disable assertions by running Python with the -O (optimize) flag. When you do this, all assert statements will be ignored and not executed.
# # For example, if you run the script with python -O script.py, the assert statements in the script will be disabled and will not raise any exceptions, even if the conditions they check are false.


# Logging
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s') # This sets up the logging configuration. The level=logging.DEBUG argument specifies that all logging messages at the DEBUG level and above (i.e., INFO, WARNING, ERROR, CRITICAL) will be logged. The format argument specifies the format of the log messages, which includes the timestamp, the log level, and the message itself.


# Logging to a File
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s') # This will log all messages at the DEBUG level and above to a file named 'myProgramLog.txt' instead of the console. The format of the log messages will include the timestamp, the log level, and the message itself.



# LOGGING DISABLE
# logging.disable(logging.CRITICAL) # This will disable all logging messages at the CRITICAL level and below (i.e., DEBUG, INFO, WARNING, ERROR). You can change the level to disable different levels of logging messages. For example, logging.disable(logging.ERROR) will disable all logging messages at the ERROR level and below (i.e., DEBUG, INFO, WARNING).


# LOGGING LEVELS
logging.debug('This is a debug message.') # DEBUG is the lowest level of logging, used for detailed information, typically of interest only when diagnosing problems.
logging.info('This is an info message.') # INFO is used for general information about the program's operation.
logging.warning('This is a warning message.') # WARNING is used to indicate that something unexpected happened, but the program can still continue to function.
logging.error('This is an error message.') # ERROR is used to indicate that something unexpected happened, and the program cannot continue to function properly.
logging.critical('This is a critical message.') # CRITICAL is the highest level of logging, used for indicating that the program cannot continue to function.
