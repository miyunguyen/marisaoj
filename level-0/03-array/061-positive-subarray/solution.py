n = int(input())
nums = list(map(int, input().split()))


def solve():
    longest_positive_length = 0
    current_positive_length = 0

    for i in range(n):
        if nums[i] > 0:
            current_positive_length += 1
            longest_positive_length = max(
                longest_positive_length, current_positive_length
            )
        else:
            current_positive_length = 0

    print(longest_positive_length)


solve()


def first_solve():
    longest_positive_length = 0

    i = 0
    while i < n:
        if nums[i] > 0:
            j = i

            while j < n - 1 and nums[j + 1] > 0:
                j += 1

            longest_positive_length = max(longest_positive_length, j - i + 1)
            i = j + 1

        else:
            i += 1

    print(longest_positive_length)


# first_solve()
