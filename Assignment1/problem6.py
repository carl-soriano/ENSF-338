import json 
import matplotlib.pyplot as plt 


def countries():
    with open("/Users/carlsoriano/Desktop/assignments-338/Assignment-1/p6-input-file.json", "r") as inF:
        data = json.load(inF)

    list_under = []
    list_over = []
    a = 10000
    for element in data:
        income = element ['incomeperperson'] #get the fiel "incomeperperson"
        for element in data:                    #put data in new list 
            if income == None:               #account for none 
                list_under.append(element["internetuserate"])               
            elif income < a:                #under 10000 income 
                list_under.append(element["internetuserate"])
            elif income > a:                              #over 10000 income 
                list_over.append(element["internetuserate"])
   

    newlist_under = [0 if x is None else x for x in list_under] #accounts for none in list 
    newlist_over = [0 if x is None else x for x in list_over]
    
    plt.style.use('seaborn-deep')
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(1, 1, 1)
    n, bins, patches = ax1.hist(newlist_under)
    ax1.set_xlabel('Internet Usage')
    ax1.set_ylabel('Income')
    ax1.set_title('Over 10000 Income')

    fig2 = plt.figure()
    ax2 = fig2.add_subplot(1, 1, 1)
    n, bins, patches = ax2.hist(newlist_over)
    ax2.set_xlabel('Internet Usage')
    ax2.set_ylabel('Income')
    ax2.set_title('Under 10000 Income')

    plt.tight_layout()
    plt.show()

    




if __name__ == "__main__":
   countries() 