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
        log_file.write('[Critical] {0}\n'.format(msg))