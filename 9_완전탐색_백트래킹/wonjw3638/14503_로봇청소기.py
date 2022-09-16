# 14503 로봇청소기
# 220916
import sys
input = sys.stdin.readline

# 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def clean(i, j, d):
    global cnt
    cnt += 1
    d = (d + 1)%4
    ###### 여기서부터 구현~~~~~~~~~~


N, M = list(map(int, input().split()))
r, c, d = list(map(int, input().split()))
arr = [ list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
cnt = 0

clean(r, c, d)

print(cnt)