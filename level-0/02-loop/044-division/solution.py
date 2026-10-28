a, b, k = map(int, input().split())

r = a % b
for i in range(k):
    digit = r * 10 // b
    r = r * 10 % b

print(digit)
