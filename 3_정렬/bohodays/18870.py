import sys

# 테스트 케이스 개수를 입력받는다.
N = int(input())

# 좌표 압축할 값들을 입력받아 numbers 리스트에 담는다.
numbers = list(map(int,sys.stdin.readline().split()))

# numbers_set라는 새로운 세트를 생성하고 값들을 넣어 중복을 제거한다.
numbers_set = set(numbers)

# 중복을 제거하고 다시 임시 리스트에 담아 정렬한다.
tmp = list(numbers_set)
tmp.sort()

# 시간초과를 방지하기 위해 딕셔너리 형태로 데이터와 인덱스를 저장한다.
numbers_dict = {}
for idx, val in enumerate(tmp):
    numbers_dict[val] = idx

# 결과를 출력한다.
for i in numbers:
    print(numbers_dict[i], end=" ")
