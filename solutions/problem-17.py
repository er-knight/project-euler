# pypi.org/project/num2words
# python -m pip install num2words

from num2words import num2words

def lettersCount(n: int) -> int:
    return len(num2words(n).replace(" ", "").replace("-", ""))

assert lettersCount(342) == 23
assert lettersCount(115) == 20

c = 0
for n in range(1, 1001):
    c += lettersCount(n)
print(c)