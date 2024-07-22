def read_file(name):
    with open(name,"r") as file:
        text=file.read().replace("\n"," ")
    return text

def test_function(text,pattern, function):
    position = function(text, pattern)
    if position != -1:
        print(f"Substring found at index {position}")
        print(text[position:min(position+80,len(text))],"\n")
    else:
        print("Substring not found\n")