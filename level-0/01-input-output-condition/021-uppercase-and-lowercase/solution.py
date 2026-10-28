c = input()


def solve_ascii(c: str):
    if ord(c) >= 65 and ord(c) <= 90:
        print(chr(ord(c) + 32))
    else:
        print(chr(ord(c) - 32))


def solve_built_in_function(c: str):
    print(str.swapcase(c))
