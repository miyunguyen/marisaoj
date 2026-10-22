import math

n, m = map(int, input().split())

mat = []
for i in range(n):
    values = list(map(int, input().split()))
    mat.append([values[i : i + 3] for i in range(0, m * 3, 3)])


def solve():
    for row in range(0, n, 2):
        output_row = []

        for col in range(0, m, 2):
            red_sum = 0
            green_sum = 0
            blue_sum = 0

            for r in range(row, row + 2):
                for c in range(col, col + 2):
                    red_sum += mat[r][c][0]
                    green_sum += mat[r][c][1]
                    blue_sum += mat[r][c][2]

            pixel = [(red_sum + 2) // 4, (green_sum + 2) // 4, (blue_sum + 2) // 4]

            output_row.extend(pixel)

        print(*output_row)


solve()


def first_solve():
    ans = [[[] for _ in range(m // 2)] for _ in range(n // 2)]

    for i in range(0, n, 2):
        for j in range(0, m, 2):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            for r in range(i, i + 2):
                for c in range(j, j + 2):
                    r_sum += mat[r][c][0]
                    g_sum += mat[r][c][1]
                    b_sum += mat[r][c][2]

            new_r = math.floor(r_sum / 4 + 0.5)
            new_g = math.floor(g_sum / 4 + 0.5)
            new_b = math.floor(b_sum / 4 + 0.5)

            ans[i // 2][j // 2] = [new_r, new_g, new_b]

    for row in range(n // 2):
        for col in range(m // 2):
            print(*ans[row][col], end=" ")
        print()


# first_solve()
