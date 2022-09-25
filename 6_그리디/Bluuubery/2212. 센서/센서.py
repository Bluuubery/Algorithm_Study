# 220903 2212 센서

# 정답코드

import sys
input = sys.stdin.readline

# N: 센서의 개수, K: 집중국의 개수 sensor: 센서의 좌표
N = int(input())
K = int(input())
sensor = list(map(int, input().split()))

# 센서 좌표 중복 제거 후 정렬
sensor = list(set(sensor))
sensor.sort()

# 집중국 개수가 정렬된 센서 개수보다 많거나 같으면 수신 가능 영역은 0이다.(각 센서마다 설치)
if K >= len(sensor):
    print(0)
# 센서 개수가 더 많을 때
else:        
    # 각 센서 간의 거리를 구한다.
    distance = [0]
    for i in range(1, len(sensor)):
        distance.append(sensor[i] - sensor[i-1])

    # 센서 거리 내림차순으로 정렬
    distance.sort(reverse=True)

    # total_distance: 센서 간 거리의 합
    total_distance = sum(distance)

    # 센서 간 거리가 가장 큰 영역 K-1개를 거리 총합에서 빼준다.
    for i in range(K - 1):
        total_distance -= distance[i]

    print(total_distance)
