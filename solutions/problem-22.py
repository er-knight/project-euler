from pathlib import Path

def alphabeticalValue(s: str) -> int:
    v = 0
    for c in s:
        v += (ord(c) - ord('A') + 1)
    return v

with (Path(__file__).parent / "names.txt").open("r") as f:
    names = sorted([name.strip('"') for name in f.read().split(",")]) 

t = 0
for i, name in enumerate(names, start=1):
    t += alphabeticalValue(name) * i

print(t)
