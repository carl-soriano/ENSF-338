
def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    if n + 2 > 1:
        return lucas(n-2) + lucas(n-1)	

    
if __name__ == "__main__":
    list = []
    for i in range(0,10):
        list.append(lucas(i))
    print(list)




