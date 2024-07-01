import json

def read(path):
    try:
        with open(path, "r") as f:
            txt = f.read()
            print(txt)

    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
