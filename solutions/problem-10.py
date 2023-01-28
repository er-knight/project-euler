from math import sqrt

def primes(n: int) -> list[int]:
    p = [True for i in range(n + 1)]
    i, sqrt_n = 2, int(sqrt(n))
    while i <= sqrt_n:
        if p[i]:
            for j in range(i * i, n + 1, i):
                p[j] = False
        i += 1

    return [i for i in range(2, n + 1) if p[i]]

print(sum(primes(2000000)))