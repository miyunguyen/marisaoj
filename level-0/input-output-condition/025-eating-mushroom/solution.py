x, y = map(int, input().split())

x -= 1

weekends = (x + y - 1) // 7 * 2

if (x + y - 1) % 7 == 6:
    weekends += 1
if x == 7:
    weekends -= 1
print(y - weekends)
