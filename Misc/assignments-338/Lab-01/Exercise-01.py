#Writting fib-sequence ex 

#write a recursive code to generate a fib sequence 


def fib(n):
    if n == 0 or n == 1:
        return n 
    else: 
        return fib(n-2) + fib(n -1) 


if __name__ == "__main__":
    list = []
    for i in range(0,35):
        list.append(fib(i))
    print(list)
    
