a, operator, b = input().split()

a, b = float(a), float(b)
if operator == "+":
    print(f"{a + b:.3f}")
elif operator == "-":
    print(f"{a - b:.3f}")
elif operator == "*":
    print(f"{a * b:.3f}")
else:
    if b != 0:
        print(f"{a / b:.3f}")
    else:
        print("ze")
