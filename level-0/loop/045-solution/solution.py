n = int(input())

ans = 0
for a in range((n - 10) // 4 + 1):
    for b in range((n - 10 - 4 * a) // 3 + 1):
        for c in range((n - 10 - 4 * a - 3 * b) // 2 + 1):
            ans += 1

print(ans)
