n = int(input())

time = [0]
pay = [0]
for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    money = dp[i-1] + pay[i]
    start = i+time[i]-1

    for j in range(start, n+1):
        if money > dp[j]:
            dp[j] = money

print(dp[n])