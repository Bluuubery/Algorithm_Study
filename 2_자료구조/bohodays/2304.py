# 2304 창고 다각형

import sys

N = int(input())

w = [0] * 1001
for _ in range(N):
    L, H = map(int, sys.stdin.readline().split())
    w[L] = H

# 최대값의 인덱스를 저장한다.
maxvalueIdx = w.index(max(w))

result1 = [w[0]]
for i in range(maxvalueIdx-1):
    if w[i+1] > result1[-1]:
        result1.append(w[i+1])
    else:
        result1.append(result1[-1])


result2 = [w[-1]]
for i in range(len(w)-1, maxvalueIdx, -1):
    if w[i-1] > result2[-1]:
        result2.append(w[i-1])
    else:
        result2.append(result2[-1])

print(sum(result1) + sum(result2))