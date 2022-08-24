N, K = map(int, input().split())
coins = list({int(input()) for _ in range(N)})
coins.sort()
dp = [float('inf')] * (K + 1)
count = 0
for i in range(1, K + 1):
    for coin in coins:
        if coin == i:
            dp[i] = 1
        elif coin < i:
            dp[i] = min(dp[i - coin] + 1, dp[i])
        else:
            continue
if dp[K] == float('inf'):
    result = -1
else:
    result = dp[K]
print(result)
