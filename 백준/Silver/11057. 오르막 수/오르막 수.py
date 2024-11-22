n = int(input())
dp = [[1] * 10 for _ in range(n)]
result = 0

for i in range(1, n):
    for j in range(10):
        result = 0
        for k in range(j, 10):
            result += dp[i-1][k]
        dp[i][j] = result

print(sum(max(dp))%10007)