import json, os

def load_json_obj(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

if __name__ == '__main__':
    file_name = "hierarchicaldataset.json"
    data = load_json_obj(file_name)
    print(data)
