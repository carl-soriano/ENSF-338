import time 


def upper():
    with open('/Users/carlsoriano/Desktop/assignments-338/Assignment-1/p7-text.txt', 'r') as inF:
        read = inF.read()
        upper = read.upper()

if __name__ == "__main__":
    start_time = time.perf_counter()
    upper()
    end_time = time.perf_counter()

print(end_time - start_time)







