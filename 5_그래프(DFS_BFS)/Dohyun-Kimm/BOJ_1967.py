# BOJ_1967 트리의 지름
# 입력 받기 + 데이터 저장
import sys

sys.setrecursionlimit(1000000) # 메모리먹음


def dfs(G, v, w, dist):
    global a  # node
    global b  # 가중치
    # print('v', v)
    visited[v] = 1  # 방문했을때 가중치 더해줘서 인덱스에 채우기
    # print(dist[v], end=' ')
    for i in G[v]:
        a, b = i  # a 자식 좌표 b 가중치
        if not visited[a]:
            dist[a] = w + b
            dfs(G, a, w + b, dist)  # w 갱신



N = int(input())
node = [[] for _ in range(N + 1)]
for n in range(N - 1):
    p, d, w = map(int, input().split())
    node[p].append([d, w])
    node[d].append([p, w])
#  0      1                2                3                          4
# [[], [[2, 3], [3, 2]], [[1, 3], [4, 5]], [[1, 2], [5, 11], [6, 9]], [[2, 5], [7, 1],[8, 7]],
#   5                            6                            7                    8
# [[3, 11], [9, 15], [10, 4]], [[3, 9], [11, 6], [12, 10]], [[4, 1]], [[4, 7]], [[5, 15]], [[5, 4]], [[6, 6]], [[6, 10]]]
# dfs 구현
visited = [0] * (N + 1)
distance = [0] * (N + 1)
a = b = 0



dfs(node, 1, 0, distance)
# print(distance)
largest1 = max(distance)
# print(largest1)
# print('====')
idx = distance.index(largest1)
# print(idx)
distance2 = [0] * (N + 1)
visited = [0] * (N + 1)
dfs(node, idx, 0, distance2)

print(max(distance2))

