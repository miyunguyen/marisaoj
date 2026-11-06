import sys

n = int(sys.stdin.readline())

hashset = set()

for _ in range(n):
    hashset.add(sys.stdin.readline())

q = int(sys.stdin.readline())

for _ in range(q):
    print("YES" if sys.stdin.readline() in hashset else "NO")