n = int(input())
nums = list(map(int, input().split()))


def solve():
    pass


solve()


def first_solve():
    is_palindrome = True

    for i in range(0, n // 2):
        if nums[i] != nums[n - i - 1]:
            is_palindrome = False
            break

    if is_palindrome:
        print("YES")
    else:
        print("NO")


first_solve()
