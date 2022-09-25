# 220831 1931 회의실 배정

# 정답코드

import sys
input = sys.stdin.readline

# N: 회의의 수
N = int(input())

# time: 회의의 시간 정보를 담을 리스트
time = []
for _ in range(N):
    time.append(list(map(int, input().split())))

# 끝나는 시간 - 시작시간 순으로 정렬한다.
time.sort(key= lambda x: (x[1], x[0]))

# 끝나는 시간이 가장 짧은 회의가 먼저 회의실을 사용한다.
cnt = 1
use = time[0]
# 정렬된 시간의 리스트에서 회의 시작 시간이 현재 회의 종료 시간과 같거나 이후면 해당 회의가 회의실을 사용한다.
for i in range(1, len(time)):
    if time[i][0] >= use[1]:
        cnt += 1
        use = time[i]

print(cnt)