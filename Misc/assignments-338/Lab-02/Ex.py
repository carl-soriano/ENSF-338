import cProfile, pstats, io



def fib(n):
  if n == 0 or n == 1:
    return n
  else:
    return fib(n-1) + fib(n-2)

def fib2(n, cache ={}):
    if n== 0 or n ==1:
        return n
    else: 
        if n in cache:
            return cache[n] 
        else:
            cache[n] = fib2(n-1) + fib2(n-2)
            return cache[n]

if __name__ == "__main__":
    rez = []
    pr = cProfile.Profile()
    pr.enable()
    for i in range(35):
        rez.append(fib2(i))

    pr.disable()
    
    print(rez)
    pr.print_stats(sort = 'cumulative')
    pr.dump_stats('stats.prof')