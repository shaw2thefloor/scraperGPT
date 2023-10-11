import json

def read():
    try:
        with open("output.txt", "r") as f:
            txt = json.loads(f.read())
            print(txt["content"])
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
