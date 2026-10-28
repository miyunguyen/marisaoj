s = input()


def solve():
    print(sum(int(c) for c in s))


solve()


def first_solve():
    sum = 0

    for c in s:
        sum += int(c)

    print(sum)


# first_solve()
