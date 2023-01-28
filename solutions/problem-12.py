from math import sqrt

def divisorsCount(n: int) -> int:
    c = 0
    for i in range(1, int(sqrt(n)) + 1):
        a, b = i, int(n / i)
        if n % a == 0:
            c += 1
        if n % b == 0 and a != b:
            c += 1
    return c

i, n = 1, 1
while divisorsCount(n) <= 500:
    i += 1
    n += i

print(n)
150