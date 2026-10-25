s = input()


def is_palindrome(text):
    return text == text[::-1]


def expand(left, right):
    count = 0

    while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1

    return count


def solve():
    count = 0
    for i in range(len(s)):
        count += expand(i, i)
        count += expand(i, i + 1)

    print(count)


solve()


def first_solve():
    count = 0

    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                count += 1

    print(count)


# first_solve()
