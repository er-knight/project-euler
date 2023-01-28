from math import sqrt

def isPrime(n: int) -> bool:
    for i in range(2, int(sqrt(n)) + 1):
        a, b = i, int(n / i)
        if n % a == 0 or n % b == 0:
            return False
    return True

p = 2
n = 3
while p < 10001:
    n += 2
    if isPrime(n):
        p += 1

print(n)
