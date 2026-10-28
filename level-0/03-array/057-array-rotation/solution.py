n, k = map(int, input().split())
nums = list(map(int, input().split()))

k %= n


def solve():
    print(*nums[k:], end=" ")
    print(*nums[0:k])


solve()


def first_solve():
    ans = []
    for i in range(n):
        ans.append(nums[(i + k) % n])
    print(*ans)


# first_solve()
