import math

a, b, c, d = map(int, input().split())

distance = math.sqrt((a - c) ** 2 + (b - d) ** 2)
print(f"{distance:.2f}")
