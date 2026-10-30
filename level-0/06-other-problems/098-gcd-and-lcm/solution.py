def solve():
    pass


def first_solve(a: int, b: int):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def lcm(a, b):
        return a * b // gcd(a, b)

    print(gcd(a, b), lcm(a, b))


a, b = map(int, input().split())

first_solve(a, b)
