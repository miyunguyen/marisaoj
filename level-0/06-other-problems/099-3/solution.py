def first_solve(n: int, nums: list[int]):
    count = 0
    needed = [0, 0, 0]
    for num in nums:
        count += needed[num % 3]
        needed[-num % 3] += 1

    return count


n = int(input())
nums = list(map(int, input().split()))

print(first_solve(n, nums))
