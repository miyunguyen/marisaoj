a, b, c = map(int, input().split())

result = 1
for i in range(b):
    result *= a % c

print(a**b % c)
print(result % c)
