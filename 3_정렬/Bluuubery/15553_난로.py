# 220813 15553 난로

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

# 친구들의 도착시간과 떠나는 시간을 담은 리스트
friends = []
for _ in range(N):
    arrive = int(input())
    friends.append([arrive, arrive + 1])

# 친구의 떠나는 시간과 다음 친구의 방문 시간까지의 차이를 계산한다.
gap = []
for i in range(1, N):
    gap.append(friends[i][0] - friends[i - 1][1])

# 내림차순으로 정렬한다.
gap.sort(reverse=True)

# 가장 긴 시간 공백 (K - 1)개를 더한다.
total_gap = sum(gap[:K - 1])

# 전체 시간에서 공백을 빼준다.
time = friends[-1][1] - friends[0][0] - total_gap

print(time)