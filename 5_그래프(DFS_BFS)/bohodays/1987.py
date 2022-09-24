# 1987 알파벳

import sys
sys.setrecursionlimit(10**4)

def DFS(x, y, cnt):
    global ans
    checkList.add(bord[x][y])

    # 백트래킹하려면 중간에 결과를 저장해야 됨
    ans = max(ans, cnt)    

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if bord[nx][ny] not in checkList:
                DFS(nx, ny, cnt+1)
    # 백트래킹을 위해 마지막에 넣은 요소 제거하기
    checkList.remove(bord[x][y])
            
R, C = map(int, sys.stdin.readline().split())

bord = []
for _ in range(R):
    bord.append(list(sys.stdin.readline()))

checkList = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0

DFS(0, 0, 1)

print(ans)