t = float(input())
if t >= 9.0:
    print("VERY TOXIC")
elif t >= 5.0 and t <= 8.9:
    print("TOXIC")
else:
    print("SAFE")
