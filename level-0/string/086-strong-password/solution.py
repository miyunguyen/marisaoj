s = input()


def solve():
    if len(s) < 8:
        print("WEAK")
        return

    has_digit = False
    has_upper = False
    has_lower = False

    for c in s:
        if c.isdigit():
            has_digit = True
        elif c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True

    print("STRONG" if has_digit and has_upper and has_lower else "WEAK")


solve()


def first_solve():
    has_digit = False
    has_upper = False
    has_lower = False
    is_long = False

    if len(s) >= 8:
        is_long = True

    for c in s:
        if c.isupper():
            has_upper = True
        if c.islower():
            has_lower = True
        if c.isdigit():
            has_digit = True

    print("STRONG" if has_upper and has_lower and has_digit and is_long else "WEAK")


# first_solve()
