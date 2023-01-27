import json 

with open("/Users/carlsoriano/Desktop/assignments-338/Assignment-1/p2-input-file.json", "r") as inF:
    data = json.load(inF)

data.reverse()

with open("/Users/carlsoriano/Desktop/assignments-338/Assignment-1/p2-output-file.json", "w") as outW:
    data_reverse = json.dump(data,outW, indent = 4)


