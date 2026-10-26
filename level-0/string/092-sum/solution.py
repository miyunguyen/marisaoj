s = input()


def solve():
    number_sum = 0
    current_number = 0

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char == " ":
            number_sum += current_number
            current_number = 0

    number_sum += current_number

    print(number_sum)


solve()


def first_solve():
    number_sum = 0

    words = s.split()

    for word in words:
        number = []
        for char in word:
            if char.isdigit():
                number.append(char)

        if len(number) != 0:
            number_sum += int("".join(number))

    print(number_sum)


# first_solve()
