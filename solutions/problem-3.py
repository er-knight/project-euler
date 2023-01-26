from math import sqrt

def isPrime(n: int) -> bool:
    for i in range(2, int(sqrt(n)) + 1):
        a, b = i, int(n / i)
        if n % a == 0 or n % b == 0:
            return False
    return True

n = 600851475143
m = 0 # largest prime factor
for i in range(2, int(sqrt(n)) + 1):
    a, b = i, int(n / i)
    if n % a == 0 and isPrime(a):
        m = max(m, a)
    if n % b == 0 and isPrime(b):
        m = max(m, b)

print(m)