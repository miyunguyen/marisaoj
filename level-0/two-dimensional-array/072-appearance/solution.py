n, m, x, y = map(int, input().split())

matrix_A = []
matrix_B = []

for _ in range(n):
    matrix_A.append(list(map(int, input().split())))

for _ in range(x):
    matrix_B.append(list(map(int, input().split())))


def solve():
    if x > n or y > m:
        print("NO")
        return

    for i in range(n - x + 1):
        for j in range(m - y + 1):
            if all(matrix_A[i + r][j : j + y] == matrix_B[r] for r in range(x)):
                print("YES")
                return

    print("NO")


solve()


def first_solve():
    is_appear = False

    for i in range(n - x + 1):
        for j in range(m - y + 1):
            is_valid = True
            for a in range(i, i + x):
                for b in range(j, j + y):
                    if matrix_A[a][b] != matrix_B[a - i][b - j]:
                        is_valid = False
                if not is_valid:
                    continue

            if is_valid:
                is_appear = True
                break

        if is_appear:
            break

    print("YES" if is_appear else "NO")


# first_solve()
