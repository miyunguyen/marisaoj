n = int(input())
nums = list(map(int, input().split()))


def solve():
    pass


solve()


def first_solve():
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    most_frequent_value = min(nums)
    most_frequent = 0

    for k, v in freq.items():
        if v > most_frequent or (v == most_frequent and k > most_frequent_value):
            most_frequent = v
            most_frequent_value = k

    print(most_frequent_value)


first_solve()
