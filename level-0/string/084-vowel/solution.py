s = input()


def solve():
    vowels = set("aeiou")
    print(sum(c.lower() in vowels for c in s))


solve()


def first_solve():
    vowels = ["A", "I", "U", "E", "O", "a", "i", "u", "e", "o"]

    count = 0
    for c in s:
        if c in vowels:
            count += 1

    print(count)


# first_solve()
