# 평범한 배낭

N, K = list(map(int, input().split()))
cargo = list()

for _ in range(N):
    cargo.append(list(map(int, input().split())))
    

dp = []

for i in range(1, N + 1):
    dp.append([])
    for c in range(1, K + 1):
        if W[i-1] <= c:
            dp[i] = max( W[i-1] + dp[i-1][c - V[i-1]], dp[i-1][c] )
        else:
            dp[i].append(dp[i-1][c])

print(dp[-1][-1])