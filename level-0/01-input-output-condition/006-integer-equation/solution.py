a, b = map(int, input().split())

if a == 0 and b == 0:
    print("INFINITE SOLUTIONS")
elif a != 0 and b % a == 0:
    print(-b // a)
else:
    print("NO SOLUTION")
