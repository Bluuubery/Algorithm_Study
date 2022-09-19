import sys
input = sys.stdin.readline

M, N = map(int, input().split())
L = sorted(list(map(int, input().split())))

s, e = 1, L[-1]
result = 0
while s <= e:
    mid = (s + e) // 2
    count = 0
    for i in range(N):
        if L[i] >= mid:
            count += L[i] // mid
    if count >= M:
        result = mid
        s = mid + 1
    else:
        e = mid - 1
print(result)
