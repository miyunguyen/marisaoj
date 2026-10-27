input_compressed_string = input()
input_decoded_string = input()


def solve():
    pass


solve()


def first_solve():
    def compress(text):
        result = []
        current_char = text[0]
        count = 0

        for char in text:
            if char == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1

        result.append(f"{count}{current_char}")

        return "".join(result)

    def decode(text):
        result = []
        current_count = 0

        for char in text:
            if char.isdigit():
                current_count = current_count * 10 + int(char)
            else:
                result.append(current_count * char)
                current_count = 0

        return "".join(result)

    print(compress(input_compressed_string))
    print(decode(input_decoded_string))


first_solve()
