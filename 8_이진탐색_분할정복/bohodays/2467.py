# 2467 용액
import sys
from collections import deque

N = int(input())

mix = deque(map(int, input().split()))

minV = sys.maxsize
# 배열의 양 끝 pop
case1, case2 = mix.popleft(), mix.pop()

# 배열이 빌 때까지 반복
while mix:
    sumV = case1 + case2

    # 최솟값 찾기
    if abs(sumV) < minV:
        ans1, ans2 = case1, case2
        minV = abs(sumV)

    # 합이 양수면 더 작은 양수 pop (0에 가깝게 하기 위해)
    if sumV > 0:
        case2 = mix.pop()
    # 합이 음수면 더 작은 음수 pop (0에 가깝게 하기 위해)
    elif sumV < 0:
        case1 = mix.popleft()
    else:
        break

# 위의 while문에서 sumV가 0이었으면 minV는 0이다.
# 0이 아닌 경우, 마지막 연산을 수행해준다.
if minV:
    if abs(case1 + case2) < minV:
        ans1, ans2 = case1, case2

print(ans1, ans2)