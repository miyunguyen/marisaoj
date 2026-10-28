n, m = map(int, input().split())

nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))


def solve():
    pass


solve()


def first_solve():
    for i in range(m):
        column_sum = 0
        for j in range(n):
            column_sum += nums[j][i]
        print(column_sum, end=" ")


first_solve()
