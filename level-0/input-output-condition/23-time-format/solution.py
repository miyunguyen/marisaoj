seconds = int(input())

hour = seconds // 3600

seconds %= 3600

minute = seconds // 60

seconds %= 60

print(hour, minute, seconds)
