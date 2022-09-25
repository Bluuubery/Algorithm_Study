def cr(arr, n):
    global answer
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for j in cr(arr[i + 1:], n - 1):
            temp = [elem] + j
            result.append([elem] + j)
            if len(temp) == M:
                answer.add(tuple(temp))
    return result


N, M = map(int, input().split())
L = sorted(list(map(int, input().split())))
answer = set()
cr(L, M)
for i in sorted(list(answer)):
    print(*i)