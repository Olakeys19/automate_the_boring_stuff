import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') # This sets up the logging configuration. The level=logging.DEBUG argument specifies that all logging messages at the DEBUG level and above (i.e., INFO, WARNING, ERROR, CRITICAL) will be logged. The format argument specifies the format of the log messages, which includes the timestamp, the log level, and the message itself.

# logging.disable(logging.CRITICAL) # This will disable all logging messages at the CRITICAL level and below (i.e., DEBUG, INFO, WARNING, ERROR). You can change the level to disable different levels of logging messages. For example, logging.disable(logging.ERROR) will disable all logging messages at the ERROR level and below (i.e., DEBUG, INFO, WARNING).

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1 ):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total

print(factorial(5)) 
logging.debug('End of program')


# logging.debug('Some debugging details.')
# logging.info('The logging module is working.')
# logging.warning('An error message is about to be logged.')
# logging.error('An error has occurred.')
# logging.critical('The program is unable to recover!')

