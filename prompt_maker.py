import json



def read_pdf_list():
    with open("doi_list.txt", "r") as f:
        txt = json.loads(f.read())
    print(txt["content"])


if __name__ == '__main__':
    read_pdf_list()