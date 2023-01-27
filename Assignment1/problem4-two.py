import json 
from statistics import mean

def avg_float():
    with open("/Users/carlsoriano/Desktop/assignments-338/Assignment-1/p4-input-file.json", "r") as inF:
        data_animals = json.load(inF)
   
    w = []                  #make empty list 

    for element in data_animals:
        weight = element['weight']  #find field with float 
        for element in data_animals: #put data in new list 
            if weight > 5:
                w.append(weight) #using append to put into new list 

    average_weight = sum(w)/len(w)  #get average of new list 

    print(f"{average_weight}")      
               


if __name__ == "__main__":
    avg_float() 
    