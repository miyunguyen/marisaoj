n = int(input())
nums = list(map(int, input().split()))

negative = []
positive = []

for x in nums:
    if x < 0:
        negative.append(x)
    else:
        positive.append(x)

result = []

i = 0
j = 0

while i < len(negative) and j < len(positive):
    result.append(negative[i])
    result.append(positive[j])
    i += 1
    j += 1

while i < len(negative):
    result.append(negative[i])
    i += 1

while j < len(positive):
    result.append(positive[j])
    j += 1

print(*result)
