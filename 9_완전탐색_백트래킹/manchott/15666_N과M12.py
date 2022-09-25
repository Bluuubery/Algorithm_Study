def cr(arr, n):
    global answer
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for j in cr(arr[i:], n - 1):
            temp = [elem] + j
            result.append([elem] + j)
    return result


N, M = map(int, input().split())
L = sorted(list(map(int, input().split())))
answer = set()
a = cr(L, M)
b = set((list(map(tuple, a))))
for i in sorted(list(b)):
    print(*i)