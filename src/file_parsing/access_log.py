

import os

from datetime import datetime


def get_file_path():
    return os.getcwd()+"/access.log"


def read_access_log():
    new_data = []
    with open(get_file_path(), "r", newline='') as file_data:
        for data in file_data:
            new_data = data.strip().split('-')
            ip_address = new_data[0].strip()
            next_value = new_data[2].split()
            date_value = datetime.strptime(next_value[0][1:], "%d/%b/%Y:%H:%M:%S")
            crud_verb = next_value[2][1:]
            uri = next_value[3]
            #status = next_value[5]
            new_data.append([ip_address, date_value, crud_verb])
    for d in new_data:
        print(d)


read_access_log()