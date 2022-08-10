
def climb(T, n, N):
    if n == N:
        return
    if T[n + 1] > T[n]:
        return T[n], climb(T, n + 1, N)
    post = climb(T, n + 1, N)
    post += T[n]
    return post
