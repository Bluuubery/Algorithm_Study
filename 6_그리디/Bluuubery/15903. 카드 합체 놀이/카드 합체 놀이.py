# 220905 15903 카드 합체 놀이

# 정답코드

import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))

# 최소힙큐를 이용하여 구현 
heapq.heapify(card)

# 최소 힙에서 최솟값 두 개를 빼서 둘을 더한 값으로 바꿔주고 다시 힙에 넣는다.
for _ in range(M):
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    heapq.heappush(card, a + b)
    heapq.heappush(card, a + b)

# 힙의 합계 출력
print(sum(card))