n = int(input())
nums = list(map(int, input().split()))

n = n - 1 if n % 2 == 0 else n

for i in range(n - 1, -1, -2):
    print(nums[i], end=" ")
