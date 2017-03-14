import math
def mathfib(n):
    return 1/math.sqrt(5)*(pow((1+math.sqrt(5))/2,n)-pow((1-math.sqrt(5))/2,n))
#
# def fib(n):
#     if n <=1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
#
# print fib(10)
print mathfib(1000)

def memoize(f):
    cache = {}
    return lambda *args: cache[args] if args in cache else cache.update({args: f(*args)}) or cache[args]

@memoize
def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)

print fib(630)