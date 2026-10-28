n = int(input())
nums = list(map(int, input().split()))
x, y = map(int, input().split())

x -= 1
y -= 1


def solve():
    clockwise = 0
    counter_clockwise = 0

    i = x
    while i != y:
        clockwise += nums[i]
        i = (i + 1) % n

    total = sum(nums)
    counter_clockwise = total - clockwise

    print(min(clockwise, counter_clockwise))


solve()


def first_solve():
    clockwise = 0
    counter_clockwise = 0

    if x == y:
        print(0)
        return

    i = x
    while i != y:
        clockwise += nums[i]
        i = (i + 1) % n

    i = (x - 1) % n

    while i != y - 1:
        counter_clockwise += nums[i]
        i = (i - 1) % n

    print(min(clockwise, counter_clockwise))


# first_solve()
