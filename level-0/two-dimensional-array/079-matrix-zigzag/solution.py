n, m = map(int, input().split())

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))


def solve():
    pass


solve()


def first_solve():
    ans = []

    for s in range(n + m - 1):
        diagonal = []

        for i in range(n):
            j = s - i

            if 0 <= j < m:
                diagonal.append(mat[i][j])

        if s % 2 == 0:
            diagonal.reverse()

        ans.extend(diagonal)

    print(*ans)


first_solve()
