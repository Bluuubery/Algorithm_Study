def p(arr, n):
    result = []
    
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for j in p(arr[:i] + arr[i+1:], n - 1):
            result.append([elem] + j)
            # print(result)
    
    return result
N, M = map(int, input().split())
L = [i for i in range(1, N + 1)]
p(L, M)
for i in p(L, M):
    print(*i)