s = input()


def solve():
    print("YES" if s == s[::-1] else "NO")


solve()


def first_solve():
    is_palindrome = True

    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            is_palindrome = False

    print("YES" if is_palindrome else "NO")


# first_solve()
