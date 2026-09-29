a, b, c, d = map(int, input().split())

if a == c or b == d or a == d or b == c:
    print("YES")
else:
    print("NO")
