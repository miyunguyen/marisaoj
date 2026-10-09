n = int(input())
nums = list(map(int, input().split()))


def solve():
    i = 0
    while i < n - 1 and nums[i] < nums[i + 1]:
        i += 1

    while i < n - 1 and nums[i] > nums[i + 1]:
        i += 1

    print("YES" if i == n - 1 else "NO")


solve()


def first_solve():
    is_bitonic = False

    for i in range(n):
        valid = True
        j = 0

        while j < i:
            if nums[j] >= nums[j + 1]:
                valid = False
                break
            j += 1

        if not valid:
            continue

        j = i + 1
        while j < n - 1:
            if nums[j] <= nums[j + 1]:
                valid = False
                break
            j += 1

        if valid:
            is_bitonic = True
            break

    print("YES" if is_bitonic else "NO")


# first_solve()  # time limit exceeded
