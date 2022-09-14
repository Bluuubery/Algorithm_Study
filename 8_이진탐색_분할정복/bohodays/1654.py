# 1654 랜선 자르기

def divide(n):
    return n//mid

K, N = map(int, input().split())

lines = []
for _ in range(K):
    lines.append(int(input()))
tmp = lines[::]
start, end = 1, sum(lines)

while start <= end:
    mid = (start + end) // 2
    lines = list(map(divide, lines))
    check = sum(lines)
    lines = tmp[::]
    # 개수가 모자르면 나누는 값을 줄인다.
    if check < N:
        end = mid - 1
    # 개수가 남는다면 나누는 값을 크게 한다.
    elif check >= N:
        start = mid + 1

print(end)


# start: 0, mid: 1270, end: 2541, check: 0
# start: 0, mid: 634, end: 1269, check: 2 
# start: 0, mid: 316, end: 633, check: 6  
# start: 0, mid: 157, end: 315, check: 14
# start: 158, mid: 236, end: 315, check: 9
# start: 158, mid: 196, end: 235, check: 11
# start: 197, mid: 216, end: 235, check: 10
# start: 197, mid: 206, end: 215, check: 10
# start: 197, mid: 201, end: 205, check: 10
# start: 197, mid: 198, end: 200, check: 11
# start: 199, mid: 199, end: 200, check: 11
# start: 200, mid: 200, end: 200, check: 11