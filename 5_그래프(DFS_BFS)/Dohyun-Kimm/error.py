# BOJ_2644_촌수 계산하기
# 2022-08-26

def relation_map(v, w):  # v 시작점, w 도작첨
    global graph
    visited = [0] * (N+1)
    queue = list()
    queue.append(v)     # 시작점 큐에 추가
    distance = 0
    while queue:
        # print(queue)
        temp = queue.pop(0)
        distance += visited[temp]
        if not visited[temp]:
            # visited [temp] = 그전 노트의 visited + 1
            visited[temp] = distance + 1
            # print(visited)
            if temp == w:
                break
            for i in graph[temp]:       # 방문한 지점과 인접한노드 탐색

                queue.append(i)
    if visited[w] == 0:
        return -1
    else:
        return visited[w]


N = int(input())  # 사람수
start, end = map(int, input().split())  # start에서 시작해서 from 까지 가는 촌수계산
M = int(input())  # 부모자식 관계의 수
graph = [[] for _ in range(N + 1)]  # 그래프 선언

for m in range(M):
    a, b = map(int, input().split())  # 그래프 채우기
    graph[a].append(b)
    graph[b].append(a)

print(relation_map(start, end))