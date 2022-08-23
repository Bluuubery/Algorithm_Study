import math
import sys
from collections import Counter

def roundUp(num):
    if num >= 0:
        return int(num) + 1 if (num - int(num)) >= 0.5 else int(num)
    else:
        return int(num) - 1 if (abs(num) - abs(int(num))) >= 0.5 else int(num)


N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

# 산술평균
print(int(roundUp(sum(numbers)/len(numbers))))

# 중앙값
print(sorted(numbers)[math.floor(len(numbers)/2)])

# 최빈값
def modefinder(numbers):
    # collections의 Counter를 쓰면 해당 인자가 몇 개 있는지 딕셔너리 형태로 반환한다.
    c = Counter(numbers)
    # most_common()을 하면 최빈값이 큰 순으로 정렬된다. (최반값이 같을 수도 있음)
    order = c.most_common()
    # 최빈값의 최대값을 저장한다.
    maximum = order[0][1]

    # 최빈값이 최대값인 인자만 리스트에 추가한다.
    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])

    # 최빈값이 여러 개라면 문제의 조건에 따라 두 번째로 큰 인자를 출력한다.
    if len(modes) != 1:
        modes = sorted(modes)
        return modes[1]
    # 최빈값이 하나라면 바로 출력한다.
    else:
        return modes[0]

print(modefinder(numbers))

# 범위
print(max(numbers) - min(numbers))

