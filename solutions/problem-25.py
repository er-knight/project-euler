from functools import cache

def numberOfDigits(n: int) -> int:
    return len(str(n))

@cache
def fibonacci(n: int) -> int:
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 1
while numberOfDigits(fibonacci(n)) < 1000:
    n += 1

print(n)