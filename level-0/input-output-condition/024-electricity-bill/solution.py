x, a, b, c, d = map(int, input().split())

if x <= 50:
    print(x * a)
elif x <= 100:
    print(50 * a + (x - 50) * b)
elif x <= 150:
    print(50 * a + 50 * b + (x - 100) * c)
else:
    print(50 * a + 50 * b + 50 * c + (x - 150) * d)
