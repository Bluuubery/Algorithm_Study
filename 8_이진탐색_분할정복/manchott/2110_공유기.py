N, C = map(int, input().split())
X = [int(input()) for _ in range(N)]
X.sort()

# 시작, 끝 = 최소거리, 최대거리
start, end = 1, X[-1] - X[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    current = X[0]
    temp = 1

    for i in range(1, N):
        if X[i] >= current + mid:
            temp += 1
            current = X[i]
    
    if temp >= C:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)

