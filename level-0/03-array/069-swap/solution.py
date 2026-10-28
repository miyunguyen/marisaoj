n, q = map(int, input().split())
nums = list(map(int, input().split()))


def solve():
    pass


solve()


def first_solve():
    queries = []
    for _ in range(q):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        queries.append((x, y))

    while len(queries) != 0:
        x, y = queries.pop()

        nums[x], nums[y] = nums[y], nums[x]

    print(*nums)


first_solve()
