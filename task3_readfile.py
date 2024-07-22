def read_file(name):
    with open(name,"r") as file:
        text=file.read().replace("\n"," ")
    return text
