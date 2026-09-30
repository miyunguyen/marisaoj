a, b = map(int, input().split())


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


for i in range(a, 0, -1):
    if a % i == 0 and b % i == 0:
        print(a // i, b // i)
        break

print(a // gcd(a, b), b // gcd(a, b))
