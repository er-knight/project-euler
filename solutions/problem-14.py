# def totalTerms(n: int) -> int:
#     c = 1
#     while n != 1:
#         if n % 2 == 0:
#             n = int(n / 2)
#         else:
#             n = 3 * n + 1
#         c += 1
#     return c


from functools import cache

@cache
def totalTerms(n: int) -> int:
    if n == 1:
        return 1
    return 1 + totalTerms(int(n / 2) if n % 2 == 0 else 3 * n + 1)

k, l = 1, 1
for n in range(1, 1000000):
    t = totalTerms(n)
    if t > l:
        k, l = n, t 
print(k)
