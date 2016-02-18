from functools import reduce
​
def reduce_factorial(n):
    if n < 1:
        return False
    return reduce(lambda x,y:x*y , range(1, n+1))
​
def recursion_factorial(n):
    if n < 1:
        return False
    elif n == 1:
        return n
    else:
        return n*recursion_factorial(n-1)
​
​
print(reduce_factorial(10))
print(recursion_factorial(10))