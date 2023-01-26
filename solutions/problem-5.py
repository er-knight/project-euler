from math import gcd

def lcm(a: int, b: int) -> int:
    return int(a * b / gcd(a, b))

m = lcm(1, 2)
for i in range(3, 21):
    m = lcm(m, i)

print(m)