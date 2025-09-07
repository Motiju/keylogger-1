import time
import json
import os
from iWriter import IWriter

class FileWriter(IWriter):
    @staticmethod
    def send_data(text):
        current_time = time.strftime("%d-%m-%Y-%H:%M:%S", time.localtime())

        file_name = "data.json"
        if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
            data = {}
        else:
            with open(file_name, "r") as file:
                data = json.load(file)

        data[current_time] = text

        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)


print(111)  
FileWriter.send_data("hello world")



