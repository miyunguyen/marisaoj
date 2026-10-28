a, b = map(int, input().split())

sum = a + b

while sum % 10 == 0:
    sum //= 10

while sum > 0:
    print(sum % 10, end="")
    sum //= 10
