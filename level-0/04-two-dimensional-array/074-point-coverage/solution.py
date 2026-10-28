n = int(input())


def solve():
    covered = [[False] * 101 for _ in range(101)]

    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                covered[x][y] = True

    count = 0
    for x in range(101):
        for y in range(101):
            if covered[x][y]:
                count += 1

    print(count)


solve()


def first_solve():
    covered = set()
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                covered.add((i, j))

    print(len(covered))


# first_solve()
