s = input()
t = input()


def solve():
    count = 0
    for start in range(len(s) - len(t) + 1):
        if s[start : start + len(t)] == t:
            count += 1

    print(count)


solve()


def first_solve():
    count = 0

    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            if s[start:end] == t:
                count += 1

    print(count)


# first_solve()
