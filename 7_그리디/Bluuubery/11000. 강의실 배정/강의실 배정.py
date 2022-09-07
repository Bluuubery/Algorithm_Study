# 220905 11000 강의실 배정

# 정답코드

import heapq
import sys
input = sys.stdin.readline

# N: 강의 개수, lecture: 수업 시간
N = int(input())
lecture = []
for _ in range(N):
    temp = list(map(int, input().split()))
    lecture.append(temp)

# 수업 시간을 오름차순으로 정렬한다.
lecture.sort()

# queue:현재 진행 중인 수업(강의실)을 담을 우선순위큐(힙큐)
queue = []
# 첫 강의의 종료 시간을 넣어준다.
heapq.heappush(queue, lecture[0][1])

for i in range(1, N):
    # 현재 진행 중인 강의의 종료 시간이 다음 강의의 시작시간 이후면 새로운 강의실을 배정한다.
    if queue[0] > lecture[i][0]:
        heapq.heappush(queue, lecture[i][1])
    # 강의실을 이어 사용할 수 있으면 큐에서 해당 강의를 빼고 다음 강의를 넣어준다.
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, lecture[i][1])

# 강의실의 개수 출력
print(len(queue))