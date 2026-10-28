n = int(input())
nums = list(map(int, input().split()))


def two_pass_solution():
    ans = []

    for num in nums:
        if num < 0:
            ans.append(num)

    for num in nums:
        if num > 0:
            ans.append(num)

    print(" ".join(str(item) for item in ans))


def in_place_solution():
    next_negative = 0

    for i in range(n):
        if nums[i] < 0:
            j = i
            while j > next_negative:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1

            next_negative += 1

    print(" ".join(str(num) for num in nums))
