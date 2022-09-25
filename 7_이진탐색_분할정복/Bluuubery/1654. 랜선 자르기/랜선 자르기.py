# 220910 1654 랜선자르기

# 정답코드

import sys
input = sys.stdin.readline

# N: 가지고 있는 랜선의 개수, K: 필요한 랜선의 개수
N, K = map(int, input().split())

# lan: 랜선의 길이를 담을 집합
lan = []
for _ in range(N):
    lan.append(int(input()))


# 랜선의 길이에 따른 랜선의 개수 이진탐색
def binary_search(arr, start, end):
    # 정답 반환
    if start > end:
        print(end)
        return 

    # mid: 현재 자를 랜선의 길이
    mid = (start + end) // 2

    # cnt: mid 길이로 잘랐을 때 랜선의 개수
    cnt = 0
    for i in range(N):
        cnt += lan[i] // mid
    
    # 필요 개수보다 더 많이 잘랐으면 더 길게 자르도록 탐색
    if cnt >= K:
        binary_search(arr, mid + 1, end)
    # 필요 개수보다 적게 잘랐으면 더 짧게 자르도록 탐색
    else:
        binary_search(arr, start, mid - 1)

# 이진탐색 실시 
binary_search(lan, 1, max(lan))