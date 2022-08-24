price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
N = int(input())


def cut(p, n):
    r = [0] * (n + 1)
    for i in range(n + 1):
        r[i] = -float('inf')
    return cal(p, n, r)


def cal(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -float('inf')
        for i in range(1, n+1):
            # print(q, p[i] + cal(p, n-i, r))
            q = max(q, p[i] + cal(p, n-i, r))
    r[n] = q
    return q


print(cut(price, N))
