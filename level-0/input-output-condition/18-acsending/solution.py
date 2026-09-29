a, b, c = map(int, input().split())


def solve_if_else(a: int, b: int, c: int):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b

    print(a, b, c)


def solve_sort(a: int, b: int, c: int):
    print(" ".join(map(str, sorted([a, b, c]))))


solve_sort(a, b, c)
