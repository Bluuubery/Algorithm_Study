N = int(input())
L = sorted(list(map(int, input().split())))
start , end = 0, N - 1
result = float('inf')


while start < end:
    temp = L[start] + L[end]
    if abs(temp) < result:
        result = abs(temp)
        answer = [L[start], L[end]]
    if temp < 0:
        start += 1
    else:
        end -= 1
print(*answer)
    