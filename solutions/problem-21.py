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

def isAmicable(n: int) -> bool:
    s = sumOfDivisors(n)
    return s != n and sumOfDivisors(s) == n

s = 0
for n in range(1, 10000):
    if isAmicable(n):
        s += n

print(s)