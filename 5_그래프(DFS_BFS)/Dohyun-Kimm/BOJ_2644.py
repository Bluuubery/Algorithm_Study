# BOJ_2644_촌수 계산하기
# 2022-08-26

def relation_map(v, w):         # v= start, w= end
    global graph
    visited = [0] * (N + 1)     # 방문 정보 기록
    queue = list()              # 방문 순서
    queue.append(v)
    while queue:                # 큐에 노드가 있다면 실행
        t = queue.pop()         #
        for node in graph[t]:           # 인접 노드들 중에
            if not visited[node]:       # 방문 안한 노드가 있다면
                queue.append(node)      # 인큐 해주고
                visited[node] = visited[t] + 1      # 그전 노드의 거리 + 1 (촌수 + 1)
                # print(visited)

    if visited[w]:
        return visited[w]
    else:
        return -1


N = int(input())  # 사람수
start, end = map(int, input().split())  # start에서 시작해서 from 까지 가는 촌수계산
M = int(input())  # 부모자식 관계의 수
graph = [[] for _ in range(N + 1)]  # 그래프 선언
for m in range(M):
    a, b = map(int, input().split())  # 그래프 채우기
    graph[a].append(b)
    graph[b].append(a)

print(relation_map(start, end))

# 반례
'''
12
7 6
11
1 2
1 3
2 7
2 8
2 9
4 5
4 6
8 10
10 11
11 12
12 4

def relation_map(v, w):  # v 시작점, w 도작첨
    global graph
    visited = [0] * (N+1)
    queue = list()
    queue.append(v)     # 시작점 큐에 추가
    distance = [0] * (N+1)
    past_node = v
    while queue:
        print(distance)
        temp = queue.pop(0)
        if not visited[temp]:
            # visited [temp] = 그전 노트의 visited + 1
            visited[temp] = 1
            distance[temp] = distance[past_node] + 1
            # print(visited)
            if temp == w:
                break
            for i in graph[temp]:       # 방문한 지점과 인접한노드 탐색
                past_node = temp
                queue.append(i)

    if visited[w] == 0:
        return -1
    else:
        return visited[w]


'''