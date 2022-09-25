# 220910 2295 세 수의 합

# 정답코드

import sys
input = sys.stdin.readline


# 이진탐색 함수 구현
def binary_search(target, arr, left, right):
    if left > right:
        return False
    
    mid = (left + right) // 2
    if target == arr[mid]:
        return True
    elif target > arr[mid]:
        return binary_search(target, arr, mid + 1, right)
    else:
        return binary_search(target, arr, left, mid - 1)


# N: 수의 개수, numbers: 수열
N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

# two_sum: numbers 리스트의 두 원소의 합들을 담은 배열
two_sum = []

for i in range(N):
    for j in range(N):
        two_sum.append(numbers[i] + numbers[j])

# 두 리스트를 정렬해준다.
two_sum.sort()
# 최댓값을 찾아야 하므로 numbers는 내림차순으로 정렬
numbers.sort(reverse=True)

# target: 찾고자 하는 수
# 이진탐색을 통해 target - numbers[j]가 two_sum 리스트에 존재하는지 탐색한다.
for i in range(N):
    target = numbers[i]
    for j in range(N):
        if binary_search(target - numbers[j], two_sum, 0, len(two_sum) - 1):
            print(target)
            exit(0)
