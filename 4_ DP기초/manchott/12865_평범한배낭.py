
N, K = map(int, input().split())
W = [0]
V = [0]
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
dp = [0] * (K + 1)
for i in range(1, N + 1):
    for j in range(K, 0, -1):
        if W[i] <= j:
            dp[j] = max(dp[j], dp[j - W[i]] + V[i])
print(dp[K])
