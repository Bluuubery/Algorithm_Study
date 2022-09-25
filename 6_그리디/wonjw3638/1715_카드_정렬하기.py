import sys, heapq
input = sys.stdin.readline

N = int(input())
cards = list()
for _ in range(N):
    heapq.heappush(cards, int(input()))

answer = 0

while N > 1:
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    answer += tmp
    heapq.heappush(cards, tmp)
    N -= 1
    
print(answer)