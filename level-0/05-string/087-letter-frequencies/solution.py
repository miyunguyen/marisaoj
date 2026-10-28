s = input()

letter_freq = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
}


def solve():
    letter_freq = [0] * 26

    for c in s:
        if "a" <= c <= "z":
            index = ord(c) - ord("a")
            letter_freq[index] += 1

    print(*letter_freq)


solve()


def first_solve():
    for c in s:
        letter_freq[c] += 1

    print(*letter_freq.values())


# first_solve()
