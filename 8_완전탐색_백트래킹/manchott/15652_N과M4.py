def cr(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for j in cr(arr[i:], n - 1):
            result.append([elem] + j)
    return result


N, M = map(int, input().split())
L = [i for i in range(1, N + 1)]
for i in cr(L, M):
    print(*i)