# 14729_칠무해

# sol 1
import sys
input = sys.stdin.readline

N = int(input())
num_list = list()

for _ in range(N):
    num_list.append(float(input()))

for i in range(7):
    minIdx = i
    for j in range(i+1,N):
        if num_list[minIdx] > num_list[j]:
            minIdx = j
    num_list[minIdx], num_list[i] = num_list[i], num_list[minIdx]

for i in range(7):
    print('{:.3f}'.format(num_list[i]))

# sol 2

import sys
input = sys.stdin.readline

N = int(input())
num_list = list()

for _ in range(N):
    num_list.append(float(input()))

min_seven = num_list[:7]

for i in range(7):
    minIdx = i
    for j in range(i+1,7):
        if min_seven[minIdx] > min_seven[j]:
            minIdx = j
    min_seven[minIdx], min_seven[i] = min_seven[i], min_seven[minIdx]

for num in num_list[7:]:
    if num >= min_seven[6]:
        continue
    else:
        min_seven[6] = 101
        for i in range(7):
            if num < min_seven[i]:
                min_seven.insert(i, num)
                break
            else: continue

for i in range(7):
    print('{:.3f}'.format(min_seven[i]))