from collections import Counter
import string
import matplotlib.pyplot as plt 

def count():
    with open('Assignment-1/problem3-text.txt') as f:
        read = f.read()
        text = read.upper()
        
        letter_counts = Counter() #First create a dictionary 

        #Iterate through each character in the text and count the occurrences of each letter
        for char in text:
            if char in string.ascii_uppercase:
                letter_counts[char] += 1

        #Print the letter counts 
        for letter, count in letter_counts.items():
            print(f"{letter}: {count}")


    letters = list(string.ascii_uppercase)
    counts = [letter_counts[letter] for letter in letters]
    plt.bar(letters, counts)
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Letter Frequency Histogram')
    plt.show()
    plt.savefig("histogram_of_letter_frequencies.png")       

    #plotting a histogram but used .bar instead of .hist 

if __name__ == "__main__":
    count()
