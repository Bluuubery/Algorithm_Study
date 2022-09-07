# 220903 11399 ATM

# 정답코드

import sys
input = sys.stdin.readline

# N: 사람의 수, people: 사람들이 돈을 인출할 떄 걸리는 시간
N = int(input())
people = list(map(int, input().split()))

# 오름차순 정렬
people.sort()

# 각 원소의 누적합을 구한다
for i in range(1, N):
    people[i] = people[i] + people[i - 1]

# 누적합의 합 출력
print(sum(people))