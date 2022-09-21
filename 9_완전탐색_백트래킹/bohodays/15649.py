# 15649 N과 M (1)

# 순열
def my_permutaion(arr, n):
    result = []
    
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for j in my_permutaion(arr[:i] + arr[i+1:], n - 1):
            result.append([elem] + j)
    
    return result

N, M = map(int, input().split())

for i in my_permutaion(list(range(1,N+1)), M):
    print(*i)