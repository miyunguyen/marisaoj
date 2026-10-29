import math


def solve(n: int, nums: list[int]) -> int:

    frequency = {}
    pairs = 0
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
        pairs += frequency[num] - 1

    return pairs


def first_solve(n: int, nums: list[int]) -> int:
    frequency = {}
    pairs = 0
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    for count in frequency.values():
        pairs += math.comb(count, 2)

    return pairs


n = int(input())
nums = list(map(int, input().split()))

# print(first_solve(n, nums))
print(solve(n, nums))
