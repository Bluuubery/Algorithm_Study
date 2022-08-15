# 버블소트
# 시간 초과!

N = int(input())
arr = list(map(int, input().split()))

cnt = 0
idx = N-1

while idx > 0:
    if idx != arr.index(max(arr)):
        cnt += idx - arr.index(max(arr))
        arr.remove(max(arr))
    else:
        arr.remove(max(arr))
    idx -= 1

print(cnt)