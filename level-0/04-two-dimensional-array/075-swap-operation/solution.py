n, m, q = map(int, input().split())

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))


def solve():
    for _ in range(q):
        op, i, j = map(int, input().split())
        i -= 1
        j -= 1

        if op == 1:
            mat[i], mat[j] = mat[j], mat[i]
        else:
            for row in mat:
                row[i], row[j] = row[j], row[i]

    for row in mat:
        print(*row)


solve()


def first_solve():
    for _ in range(q):
        op, i, j = map(int, input().split())
        i -= 1
        j -= 1
        if op == 1:
            mat[i], mat[j] = mat[j], mat[i]

        elif op == 2:
            for rows in range(n):
                mat[rows][i], mat[rows][j] = mat[rows][j], mat[rows][i]

    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")
        print()


# first_solve()
