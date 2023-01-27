import json 

def add_field():
    with open("/Users/carlsoriano/Desktop/assignments-338/Assignment-1/p4-input-file.json", "r") as inF:
        data_animals = json.load(inF)

    length = len(data_animals)

    for i in range(length):
        data_animals[i].update({"Pet ID Number": i })

    with open("/Users/carlsoriano/Desktop/assignments-338/Assignment-1/p4-output-file.json", "w") as outW:
        data_reverse = json.dump(data_animals,outW) 

if __name__ == "__main__":
    add_field() 
    