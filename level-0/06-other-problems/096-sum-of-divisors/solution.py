import math


def solve():
    pass


def first_solve(number):
    total = 0
    square_root = math.isqrt(number)
    for divisor in range(1, square_root + 1):
        if number % divisor == 0:
            total += divisor + number // divisor

    if square_root * square_root == number:
        total -= square_root

    return total


print(first_solve(int(input())))
