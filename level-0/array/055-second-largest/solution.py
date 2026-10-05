n = int(input())
nums = list(map(int, input().split()))


def solve():

    if nums[0] > nums[1]:
        largest = nums[0]
        second_largest = nums[1]
    else:
        largest = nums[1]
        second_largest = nums[0]

    for i in range(2, n):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        elif nums[i] > second_largest:
            second_largest = nums[i]

    print(second_largest)


solve()


def first_solve():
    largest = max(nums)

    smallest_diff = largest - min(nums)
    second_largest = 0

    for num in nums:
        if abs(largest - num) < smallest_diff and abs(largest - num) != 0:
            second_largest = num
            smallest_diff = abs(largest - num)

    print(second_largest)
