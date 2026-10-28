n = int(input())
nums = list(map(int, input().split()))

largest_diff = abs(nums[0] - nums[1])
for i in range(1, n - 1):
    if abs(nums[i] - nums[i + 1]) > largest_diff:
        largest_diff = abs(nums[i] - nums[i + 1])

print(largest_diff)
