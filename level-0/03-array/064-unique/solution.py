n = int(input())
nums = list(map(int, input().split()))


def solve():
    for i in range(n):
        if nums[i] != nums[i - 1] or i == 0:
            print(nums[i], end=" ")


solve()


def first_solve():
    print(*sorted(set(nums)))


# first_solve()
