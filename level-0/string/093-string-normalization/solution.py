s = input()


def solve():
    words = s.split()
    normalized_words = [word.capitalize() for word in words]
    print(" ".join(normalized_words))


solve()


def first_solve():
    words = s.split()
    ans = []
    for word in words:
        ans.append(word.capitalize())

    print(" ".join(ans))


# first_solve()
