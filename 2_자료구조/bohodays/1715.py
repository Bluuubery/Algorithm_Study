# 우선순위 큐를 활용한 문제
# 데이터 추가는 어떤 순서로 해도 상관이 없지만, 제거될 때는 가장 작은 값을 제거하는 독특한 특성을 지닌 자료구조

from queue import PriorityQueue
import sys

N = int(input())
# q를 우선순위 큐로 설정
q = PriorityQueue()
ans = 0

# 입력받는 수를 q에 추가
for _ in range(N):
    q.put(int(sys.stdin.readline()))

# q에 들어있는 정수가 1개면 멈추는 루프 생성
while q.qsize() >= 2:
    # get()을 써서 q에서 가장 작은 값을 제거
    A = q.get()
    B = q.get()
    # 가장 작은 두 값을 더해서 다시 q에 넣어준다.
    ans += A+B
    q.put(A+B)

print(ans)