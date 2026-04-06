

import os
import json


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, "data.json")

def read_data():

    try:
        with open(FILE, "r") as f:
            data = json.load(f) #dectionary
            return data
    except Exception as e:
        print(e)
        return None


def write_data(data):
    try:
        with open(FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(e)
