import math

n = int(input())


def solve():
    if n <= 1:
        print("NO")
        return

    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            print("NO")
            return

    print("YES")


solve()
