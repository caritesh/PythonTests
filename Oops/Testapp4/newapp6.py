#this can be used directly instead of using cachef
#from functools import lru_cache
#@lru_cache(maxsize=1000)


cachef = {}

def fib(n):
    if type(n) != int:
        raise TypeError("wrong value")
    if n < 1:
        raise ValueError("n must be positive")
    assert n < 10,f'number exceeds limit'
    
    if n in cachef:
        return cachef[n]
    
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        value = fib(n-1) + fib(n-2)

    cachef[n] = value
    return value

for n in range (1,1000):
    print(n, ":", fib(n))

#to check ration between consecutive terms
for n in range(1,51):
    print(fib(n+1)/fib(n))
