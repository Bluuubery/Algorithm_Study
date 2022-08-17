# 1946 신입 사원

import sys

T = int(input())

for _ in range(T):

    N = int(input())

    rank = []
    for _ in range(N):
        rank.append(list(map(int, sys.stdin.readline().split())))
    rank = sorted(rank)

    # 시간 초과
    # cnt = 0
    # for i in range(1,N):
    #     for j in range(i):
    #         if rank[i][1] > rank[j][1]:
    #             cnt += 1
    #             break
    # print(N-cnt)

    cnt = 1
    minV = rank[0][1]

    for i in range(1, N):
        if rank[i][1] < minV:
            minV = rank[i][1]
            cnt += 1
    print(cnt)
        
    # [[1, 4], [2, 5], [3, 6], [4, 2], [5, 7], [6, 1], [7, 3]]