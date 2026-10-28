n = input()

decimal = 0

for i in range(len(n)):
    decimal += int(n[i]) * (2 ** (len(n) - i - 1))

print(decimal)
