f = 1
for n in range(2, 101):
    f *= n
print(sum(int(d) for d in str(f)))