n, q = map(int, input().split())
nums = list(map(int, input().split()))


def solve():
    pass


solve()


def first_solve():
    pass
    for _ in range(q):
        i, x = map(int, input().split())

        nums.insert(i - 1, x)

        print(*nums)


first_solve()
