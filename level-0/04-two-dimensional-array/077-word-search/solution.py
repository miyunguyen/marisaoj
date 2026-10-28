n, m = map(int, input().split())

mat = []
for i in range(n):
    mat.append(input())

word = input()
word_length = len(word)


def solve():
    reversed_word = word[::-1]

    # Horizontal
    if m >= word_length:
        for row in mat:
            for c in range(m - word_length + 1):
                segment = row[c : c + word_length]
                if segment == word or segment == reversed_word:
                    print("YES")
                    return

    # Vertical
    if n >= word_length:
        for c in range(m):
            for r in range(n - word_length + 1):
                segment = "".join(mat[r + k][c] for k in range(word_length))

                if segment == word or segment == reversed_word:
                    print("YES")
                    return

    print("NO")


solve()


def first_solve():
    found = False
    # find word from rows
    if m >= word_length:
        for row in mat:
            for c in range(m - word_length + 1):
                candidate_1 = row[c : c + word_length]  # left to right
                candidate_2 = row[c : c + word_length][::-1]  # right to left
                if candidate_1 == word or candidate_2 == word:
                    found = True
                    break
            if found:
                break

    # find word from cols
    if n >= word_length:
        for col in range(m):
            col_str = "".join(mat[row][col] for row in range(n))

            for i in range(n - word_length + 1):
                candidate_1 = col_str[i : i + word_length]  # top to bottom
                candidate_2 = col_str[i : i + word_length][::-1]  # bottom to top
                if candidate_1 == word or candidate_2 == word:
                    found = True
                    break
            if found:
                break

    print("YES" if found else "NO")


# first_solve()
