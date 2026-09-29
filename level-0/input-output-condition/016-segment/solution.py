a, b, c, d = map(int, input().split())

if (c >= a and c <= b) or (d >= a and d <= b) or (c <= a and d >= b):
    print("YES")
else:
    print("NO")
