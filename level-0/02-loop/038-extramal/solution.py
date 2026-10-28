n = int(input())
nums = list(map(int, input().split()))

min = float("inf")
max = float("-inf")

for num in nums:
    if num < min:
        min = num

    if num > max:
        max = num

print(max, min)
