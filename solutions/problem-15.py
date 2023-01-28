from functools import cache

def totalPaths(n: int) -> int:
    
    @cache
    def helper(i: int, j: int) -> int:
        if i == n and j == n:
            return 1
        return (
            (helper(i + 1, j) if i < n else 0) + 
            (helper(i, j + 1) if j < n else 0)
        )

    return helper(0, 0)

print(totalPaths(20))
