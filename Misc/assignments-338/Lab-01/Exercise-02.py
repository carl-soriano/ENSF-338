import json 

with open('/Users/carlsoriano/Desktop/assignments-338/Labs/ex-2.json','r') as inF:
    content = json.load(inF)



with open('Labs/ex-2-out.json','w') as outF:
    content_out = json.dump(content, outF)

