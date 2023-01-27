import timeit as time

def fib(n):
    if n == 0 or n == 1:
        return n 
    else: 
        return fib(n-2) + fib(n -1) 
    
def fib_2(n):
    n = fib(n)
    list = []
    for i in range(0,30):
        list.append(fib(i))
    print(list)

def fib_3(n):
    n = fib(n)
    mylist = [ fib(i) for i in range (0,30)]
    print(mylist)

mycode = '''
def fib(n):
    if n == 0 or n == 1:
        return n 
    else: 
        return fib(n-2) + fib(n -1) 
''' 
mycode_2 = '''
def fib_2(n):
    n = fib(n)
    list = []
    for i in range(0,30):
        list.append(fib(i))
    print(list)
''' 
mycode_3 = '''
def fib_3(n):
    n = fib(n)
    mylist = [ fib(i) for i in range (0,30)]
    print(mylist)
''' 

if __name__ == "__main__":
    fib_2(30)
    fib_3(30)
    print(time.timeit(stmt= mycode,  number = 10000))
    print(time.timeit(stmt= mycode_2,  number = 100))
    print(time.timeit(stmt= mycode_3,  number = 100))
    





    