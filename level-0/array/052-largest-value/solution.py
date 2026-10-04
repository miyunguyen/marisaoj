n = int(input())
nums = list(map(int, input().split()))

largest_value = nums[0]
largest_position = 0

for i, num in enumerate(nums):
    if num > largest_value:
        largest_value = num
        largest_position = i

print(largest_value, largest_position + 1)
