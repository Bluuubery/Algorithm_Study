# 220915 15664 N과 M (10)

# 정답코드

import sys
input = sys.stdin.readline

# N: 수열의 범위, M: 수열의 길이, numbers: 탐색할 수열
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

# sequence: 결과 수열을 담을 배열
# result: 결과 수열들을 담을 셋 (중복 방지)
sequence = []
result = set()


# 백트래킹 함수 구현
def back_tracking(current):

    # 수열의 길이가 M에 도달했을 때
    if len(sequence) == M:
        # 수열을 튜플로 변환해서 result에 넣어준다.
        # 튜플: hashable (list: unhashable, 객체 참조 과정에서 데이터 덮어쓰기 발생)
        result.add(tuple(sequence))
        return

    # 중복 방지 위해 범위 설정
    for i in range(current, N):

        # 선택한 수 수열에 삽입
        sequence.append(numbers[i])

        # 현재 선택한 수dml 인덱스부터 재귀적으로 반복
        back_tracking(i)

        # 백트래킹 위해 수열에서 수 빼주기
        sequence.pop()

    return 


# 백트래킹으로 수열 담아주기
back_tracking(0)

# 수열들을 하나씩 출력해준다.
for sub in sorted(list(result)):
    print(*sub)