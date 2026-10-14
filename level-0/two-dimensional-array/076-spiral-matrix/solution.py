n, m = map(int, input().split())

mat = [[0 for _ in range(m)] for _ in range(n)]


def solve():
    pass


solve()


def first_solve():
    top, right, bottom, left = 0, m - 1, n - 1, 0
    value = 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            mat[top][j] = value
            value += 1

        top += 1

        for i in range(top, bottom + 1):
            mat[i][right] = value
            value += 1

        right -= 1

        if top <= bottom:
            for j in range(right, left - 1, -1):
                mat[bottom][j] = value
                value += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                mat[i][left] = value
                value += 1
            left += 1

    for row in mat:
        print(*row)


first_solve()
