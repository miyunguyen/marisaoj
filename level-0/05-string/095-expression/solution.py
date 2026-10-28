s = input()


def solve():

    total = 0
    digits = ""
    product = 0
    in_product = False

    for char in s + "+":
        if char.isdigit():
            digits += char
        elif char == "*":
            number = int(digits)
            product = product * number if in_product else number
            in_product = True
            digits = ""
        else:
            number = int(digits)
            total += product * number if in_product else number
            in_product = False
            digits = "-" if char == "-" else ""

    print(total)


solve()


def first_solve():
    current_number = 0
    tokens = []

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        else:
            tokens.append(current_number)
            tokens.append(char)
            current_number = 0

    tokens.append(current_number)

    result = []
    op = ""
    for term in reversed(tokens):

        if isinstance(term, int):
            match op:
                case "-":
                    current = result.pop()
                    result.append(-current)
                    result.append(term)
                    op = ""
                case "*":
                    current = result.pop()
                    result.append(current * term)
                    op = ""
                case _:
                    result.append(term)
        else:
            op = term

    print(sum(result))


# first_solve()
