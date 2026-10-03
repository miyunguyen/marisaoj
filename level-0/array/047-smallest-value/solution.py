n = int(input())
nums = list(map(int, input().split()))

min = nums[0]

for num in nums:
    if num < min:
        min = num

print(min)
