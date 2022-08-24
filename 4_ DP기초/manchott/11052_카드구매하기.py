def cal(P, N, cost):
    if cost[N] > 0:
        return cost[N]
    q = 0
    if N:
        for i in range(1, N+1):
            q = max(q, P[i] + cal(P, N-i, cost))
    cost[N] = q
    return q


N = int(input())
P = [0] + list(map(int, input().split()))
cost = [0] * (N + 1)

print(cal(P, N, cost))
