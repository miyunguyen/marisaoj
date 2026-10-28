n = int(input())
nums = list(map(int, input().split()))


def two_largest_smallest() -> tuple[list[int], list[int]]:
    if nums[0] > nums[1]:
        largest = nums[0]
        second_largest = nums[1]
    else:
        largest = nums[1]
        second_largest = nums[0]

    if nums[0] < nums[1]:
        smallest = nums[0]
        second_smallest = nums[1]
    else:
        smallest = nums[1]
        second_smallest = nums[0]

    for i in range(2, n):
        if nums[i] < smallest:
            second_smallest = smallest
            smallest = nums[i]
        elif nums[i] < second_smallest:
            second_smallest = nums[i]

        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        elif nums[i] > second_largest:
            second_largest = nums[i]

    return [smallest, second_smallest], [largest, second_largest]


def solve():
    smallest_pair, largest_pair = two_largest_smallest()
    two_smallest_product = smallest_pair[0] * smallest_pair[1]
    two_largest_product = largest_pair[0] * largest_pair[1]
    print(max(two_largest_product, two_smallest_product))


solve()


def first_solve():
    max_product = float("-inf")

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            max_product = max(max_product, nums[i] * nums[j])

    print(max_product)


# first_solve()
