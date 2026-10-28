n = int(input())

sum = 0

n = abs(n)

while n > 0:
    sum += n % 10
    n //= 10

print(sum)
