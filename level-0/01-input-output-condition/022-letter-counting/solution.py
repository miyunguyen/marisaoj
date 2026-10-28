a, b = input().split()

a, b = str.lower(a), str.lower(b)

print(ord(b) - ord(a) - 1)
