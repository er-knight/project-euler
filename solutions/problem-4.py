m = 0 # largest palindrome
for i in range(100, 1000):
    for j in range(100, 1000):
        product = str(i * j)
        if product == product[::-1]:
            m = max(m, int(product))
print(m)