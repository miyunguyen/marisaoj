n = int(input())
nums = list(map(int, input().split()))


def solve():
    pass


solve()


def first_solve():
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    count = 0

    for v in freq.values():
        if v > 2:
            count += 1

    print(count)


first_solve()
