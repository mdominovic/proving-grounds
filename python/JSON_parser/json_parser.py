import requests
import json
from ToDo import ToDo


def parse_json():
    json_file = requests.get('https://jsonplaceholder.typicode.com/todos')

    todo_list = json_file.json()
    userId_list = list()

    for item in todo_list:
        for key, value in item.items():
            if key == "userId":
                userId_list.append(value)

    userId_list = list(set(userId_list))

    obj_list = list()
    for userId in userId_list:
        todo_obj = ToDo(todo_list, userId)
        obj_list.append(todo_obj)

    dict_list_objects = list()
    for object in obj_list:
        dict_object = object.__dict__
        dict_list_objects.append(dict_object)

    # print(json.dumps(dict_list_objects))

    return json.dumps(dict_list_objects)

if __name__ == "__main__":
    output = parse_json()
