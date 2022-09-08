import heapq
T = int(input())

for tc in range(T):
    N = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    
    answer = 0

    while N > 1:
        tmp = heapq.heappop(files) + heapq.heappop(files) 
        answer += tmp
        heapq.heappush(files, tmp)
        N -= 1
    
    print(answer)