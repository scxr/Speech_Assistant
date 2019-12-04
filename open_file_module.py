import json, os
def open_file(file_to_look_for):
    try:
        with open('myfiles.json') as json_file:
            data=json.load(json_file)
            os.startfile(data[file_to_look_for])
    except Exception as e:
        print("could not find this file")
