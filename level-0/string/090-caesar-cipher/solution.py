s = input()
k = int(input())


def solve():
    pass


solve()


def first_solve():
    encrypted = []

    for c in s:
        if c == " ":
            encrypted.append(c)
        else:
            shifted = chr((ord(c) - ord("a") + k) % 26 + ord("a"))
            encrypted.append(shifted)

    print("".join(encrypted))


first_solve()
