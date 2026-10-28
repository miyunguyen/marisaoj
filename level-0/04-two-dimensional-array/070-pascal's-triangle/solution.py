import math

n = int(input())

for i in range(n):
    for k in range(i + 1):
        print(math.comb(i, k), end=" ")
    print()
