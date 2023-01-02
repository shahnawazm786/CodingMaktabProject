'''
For the sake of our logger, we will handle  the following levels:
Critical
Error
Warning
Info
Debug
'''
def log_message(msg):
    with open("logger.log","a") as log_file:
        log_file.write("{0}\n".format(msg))

def critical(msg):
    with open("logger.log","a") as log_file:
        log_file.write('[CRITICAL] {0}\n'.format(msg))

def error(msg):
    with open("logger.log","a") as log_file:
        log_file.write('[ERROR] {0}\n'.format(msg))

def warn(msg):
    with open("logger.log","a") as log_file:
        log_file.write('[WARN] {0}\n'.format(msg))

def error(msg):
    with open("logger.log","a") as log_file:
        log_file.write('[Error] {0}\n'.format(msg))
