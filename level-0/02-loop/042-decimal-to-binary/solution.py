n = int(input())

binary = []
while n > 0:
    binary.append(n % 2)
    n //= 2

binary.reverse()
print("".join(map(str, binary)))
