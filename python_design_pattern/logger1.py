def write_log(level,msg):
    with open('loggers.log','a') as log_file:
        log_file.write("[{0}] {1}\n".format(level,msg))

def critical(msg):
    write_log("CRITICAL",msg)


def critical(msg):
    write_log("CRITICAL",msg)