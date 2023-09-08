import json

def read():
    with open("output.txt", "r") as f:
        txt = json.loads(f.read())
    print(txt["content"])
