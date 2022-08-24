#  220807 17298 오큰수

import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

# 오큰수를 담을 리스트와 빈 스택을 만들어준다.
nge = [-1] * n
stack = []


for i in range(n):
    # 다음에 오는 수가 스택 최상단에 있는 수보다 크면 스택을 비워주고 해당 수는 스택에 있던 모든 수의 오큰수가 된다.
    while stack and numbers[stack[-1]] < numbers[i]:
        nge[stack.pop()] = numbers[i]
    # 스택이 비어있거나 스택 최상단에 있는 수(인덱스로 접근)보다 작으면 스택에 넣어준다(인덱스를 넣어줌)
    stack.append(i)

print(*nge)

'''
스택에 수 자체를 안 넣고(stack.append(nge[i])) 인덱스를 넣은 이유(stack.append(i))
- 처리 속도도 느려지고 스택에 있던 수를 빼서 오큰수 리스트에 넣어주는 게 복잡해서 인덱스로 접근
'''
