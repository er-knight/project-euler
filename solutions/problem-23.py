from math import sqrt

def sumOfDivisors(n: int) -> int:
    s = 1
    for i in range(2, int(sqrt(n)) + 1):
        a, b = i, int(n / i)
        if n % a == 0:
            s += a
        if n % b == 0 and b != a:
            s += b
    return s

def isAbundant(n: int) -> bool:
    return sumOfDivisors(n) > n

def isSumOfAbundantNumbers(n: int, a: set[int]) -> bool:
    for i in a:
        if (n - i) in a:
            return True
    return False

# by mathematical analysis, it can be shown that 
# all integers greater than 28123 can be written 
# as the sum of two abundant numbers

a = set() # set of abundant numbers
for n in range(1, 28123):
    if isAbundant(n):
        a.add(n)

s = 0
for n in range(1, 28123):
    if not isSumOfAbundantNumbers(n, a):
        s += n

print(s)