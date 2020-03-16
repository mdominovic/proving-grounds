import json
import os
import re

def parse_results():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_location = os.path.join(current_dir, "test_result_output.txt")
    with open(file_location, 'r') as file_txt:
        file_joined = "".join(file_txt.read())
        paths = re.findall(r"\/{2}.+:\w+", file_joined)
        results = re.findall(r"(PASSED|FAILED)", file_joined)
        time = re.findall(r"[0-9]+\.[0-9]+s", file_joined)
        cached_list = []
        for line in file_joined.split("\n"):
            if "cached" in line:
                cached_list.append(True)
            else:
                cached_list.append(False)

    dict_results = {}

    if len(paths) == len(results):
        for i in range(0,len(paths)):
            dict_results.update({paths[i] : {"result": results[i], "time" : time[i], "cached" : cached_list[i]}})

    return json.dumps(dict_results, indent=4)

if __name__ == "__main__":
    output = parse_results()
    print(output)