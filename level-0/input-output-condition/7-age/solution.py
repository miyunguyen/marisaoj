a, b, c, x, y, z = map(int, input().split())

older = 1

if c > z:
    older = 2
elif c == z and b > y:
    older = 2
elif c == z and b == y and a > x:
    older = 2

print(older)
