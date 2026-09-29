a, b, c = map(int, input().split())


def my_min(*args: int):
    current_min = args[0]

    for num in args:
        if num < current_min:
            current_min = num

    return current_min


def my_max(*args: int):
    current_max = args[0]

    for num in args:
        if num > current_max:
            current_max = num

    return current_max


print(my_min(a, b, c), my_max(a, b, c))
