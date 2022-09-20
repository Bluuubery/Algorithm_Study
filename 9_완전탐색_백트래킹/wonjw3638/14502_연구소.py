# 14502 연구소
# 220920

import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

# 연구소 0의 i, j 위치 받아놓기
# 그 중에 3개 조합 사용해서 고르기
# 바이러스 번식 bfs 진행, answer 보다 작아지면 그냥 다음으로 넘어가기
# 바이러스 갯수 세서 더 영역이 더 작으면 answer 값 update
