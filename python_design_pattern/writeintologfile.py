def log_message(msg):
    with open("logger.log","a") as log_file:
        log_file.write("{0}\n".format(msg))


log_message("Second line")
log_message("Third line")
log_message("Fourth line")