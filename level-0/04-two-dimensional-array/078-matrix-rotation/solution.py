n = int(input())

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))


def solve():
    pass


solve()


def first_solve():
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    for row in mat:
        row.reverse()

    for row in mat:
        print(*row)


first_solve()
