for a in range(1001):
    for b in range(a + 1, 1001):
        for c in range(b + 1, 1001):
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                print(a * b * c)
                exit(0)