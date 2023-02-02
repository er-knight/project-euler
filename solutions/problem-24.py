def nextPermutation(p: list[int]) -> list[int]:
    
    #  find longest non-increasing suffix
    i = len(p) - 1
    while i > 0 and p[i - 1] >= p[i]:
        i -= 1

    if i <= 0: # current is last permutation 
        return p[::-1] # return first permutation

    j = len(p) - 1
    # pivot: p[i - 1]
    # find rightmost element grater than pivot
    while p[j] <= p[i - 1]:
        j -= 1

    # swap pivot with current p[j]
    p[i - 1], p[j] = p[j], p[i - 1]

    # reverse the suffix, p[i:]
    p[i:] = reversed(p[i:])

    return p 
    
p = [i for i in range(10)]
for i in range(999999):
    p = nextPermutation(p)

print(*p, sep="")