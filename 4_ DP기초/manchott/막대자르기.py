price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
N = int(input())


def cut(p, n):
    dp = [0] * (n + 1)
    for i in range(n + 1):
        dp[i] = -float('inf')
    return cal(p, n, dp)


def cal(p, n, dp):
    if dp[n] >= 0:
        return dp[n]
    if n == 0:
        temp_min = 0
    else:
        temp_min = -float('inf')
        for i in range(1, n+1):
            # print(q, p[i] + cal(p, n-i, r))
            temp_min = max(temp_min, p[i] + cal(p, n-i, dp))
    dp[n] = temp_min
    return temp_min


print(cut(price, N))
