# 스택을 이용한 풀이!

import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))

# 입력받는 수만큼 기본값이 -1인 리스트를 생성한다.
result = [-1] * N
# 스택을 담을 리스트를 생성한다.
stack = []


# 루프를 돌면서 더 작은 수를 만나면 스택에 쌓는다. (위에 쌓는다는 느낌) (후입선출)
for idx, i in enumerate(A):
    # 더 큰 수를 만나면 스택 안에 있는 수를 비우고 그 수를 스택에 쌓는다.
    while stack and (stack[-1][1] < i):
        tmp_idx, tmp = stack.pop()
        result[tmp_idx] = i
    stack.append([idx, i])

print(*result)

# [입력] 3 2 4 1 8
# [출력] 4 4 8 8 -1





# 3은 처음값이니까 그냥 스택에 들어가고, 2는 3보다 작으니까 스택에 쌓여. 그리고 4는 스택에 있는
# 3, 2 보다 크니까 후입선출 개념으로 뒤에 쌓인 2부터 스택에서 제거하고 2의 오큰수로 4를 추가해.
# 그리고 3도 같은 방법으로 스택에서 제거하고, 스택에 4가 추가해.
# 이런식으로 문제를 풀었어.