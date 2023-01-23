import datetime
def log(event, str):
    log_file = 'log.txt'
    with open (log_file, 'a', encoding='utf-8') as file:
        str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' ' + event + ' ' + str + '\n'
        file.write(str)