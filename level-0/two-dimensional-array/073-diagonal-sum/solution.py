n, m, x, y = map(int, input().split())

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))


def solve():
    diagonal_sum = mat[x - 1][y - 1]

    x1, y1 = x - 1, y - 1

    # up-left
    while x1 - 1 >= 0 and y1 - 1 >= 0:
        x1 -= 1
        y1 -= 1
        diagonal_sum += mat[x1][y1]

    # down-right
    x1, y1 = x - 1, y - 1
    while x1 + 1 < n and y1 + 1 < m:
        x1 += 1
        y1 += 1
        diagonal_sum += mat[x1][y1]

    # up-right
    x2, y2 = x - 1, y - 1
    while x2 - 1 >= 0 and y2 + 1 < m:
        x2 -= 1
        y2 += 1
        diagonal_sum += mat[x2][y2]

    # down-left
    x2, y2 = x - 1, y - 1
    while x2 + 1 < n and y2 - 1 >= 0:
        x2 += 1
        y2 -= 1
        diagonal_sum += mat[x2][y2]

    print(diagonal_sum)


solve()


def first_solve():
    diagonal_sum = mat[x - 1][y - 1]

    x1, y1 = x - 1, y - 1

    while x1 >= 0 and y1 >= 0:
        x1 -= 1
        y1 -= 1

        if x1 < 0 or y1 < 0:
            break

        diagonal_sum += mat[x1][y1]

    x1, y1 = x - 1, y - 1

    while x1 < n and y1 < m:
        x1 += 1
        y1 += 1

        if x1 >= n or y1 >= m:
            break

        diagonal_sum += mat[x1][y1]

    x2, y2 = x - 1, y - 1

    while x2 >= 0 and y2 < m:
        x2 -= 1
        y2 += 1

        if x2 < 0 or y2 >= m:
            break

        diagonal_sum += mat[x2][y2]

    x2, y2 = x - 1, y - 1

    while x2 < n and y2 >= 0:
        x2 += 1
        y2 -= 1

        if x2 >= n or y2 < 0:
            break

        diagonal_sum += mat[x2][y2]

    print(diagonal_sum)


# first_solve()
