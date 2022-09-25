def cr(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for j in cr(arr[:i] + arr[i+1:], n - 1):
            result.append([elem] + j)
    return result


N, M = map(int, input().split())
L = sorted(list(map(int, input().split())))
for i in cr(L, M):
    print(*i)