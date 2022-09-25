# BOJ_2805.py

N, M = map(int, input().split())
trees = list(map(int,input().split()))
H = list()
start = 0
end = max(trees) + 1
mid = 0
while start < end:
    cut = 0  # 자른 나무의 길이
    # mid = 설정한 톱날의 높이
    mid = (start + end) // 2
    for i in trees:
        if i > mid:
            cut += i - mid
    if cut == M:
        H.append(mid)
        break
    elif cut > M:
        start = mid + 1
        H.append(mid)
    else:
        end = mid-1
print(f'이분탐색으로 찾은 가능한 톱날 높이의 집합: {H}')
flag = 0
height = max(H)
saw = list()
# M을 만족할때 까지 1 씩 늘려가기
while flag == 0:
    cut = 0
    for j in trees:
        if j > height:
            cut += j - height
    if cut < M:
        flag = 1
    else:
        saw.append(height)
        height += 1
print(f'조건을 만족하는 톱날 높이의 집합. {saw}')
print(saw.pop())
