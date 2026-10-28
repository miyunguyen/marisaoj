n = int(input())
nums = list(map(int, input().split()))


def solve():
    dominants = 0
    current_max = nums[n - 1]

    for i in range(n - 2, -1, -1):
        if nums[i] > current_max:
            current_max = nums[i]
            dominants += 1

    print(dominants)


def naive_solution():
    dominants = 0

    for i in range(0, n - 1):
        is_dominant = True
        for j in range(i + 1, n):
            if nums[i] <= nums[j]:
                is_dominant = False

        if is_dominant:
            dominants += 1

    print(dominants)
