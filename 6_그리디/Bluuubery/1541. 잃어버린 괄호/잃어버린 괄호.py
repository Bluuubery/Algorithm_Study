# 220904 1541 잃어버린 괄호

# 정답코드

import sys
input = sys.stdin.readline

# formula: 연산식
formula = list(input().strip())

# stack: 숫자를 담을 스택, operator 연산자를 담을 리스트
stack = []
operator = []

# temp: 문자열로 된 숫자를 담기 위한 임시 변수
temp = str()
for i in formula:
    # 숫자일 경우 temp에 이어 붙인다.
    if i.isdigit():
        temp += i
    # 연산자일 경우에 temp를 숫자로 바꾸어서 스택에 넣고 초기화 시켜준다.
    # 연산자는 리스트에 담아준다.
    else:
        stack.append(int(temp))
        temp = str()
        operator.append(i)
# 마지막으로 temp에 있던 숫자를 스택에 담아준다.
stack.append(int(temp))

# ans: 정답
ans = 0
# 후위 표기식을 이용해서 '+'일 경우 계속 더해주다가 '-'가 나오면 ans에서 누적된 값을 빼준다.
while operator:
    op = operator.pop()
    # '+'일 경우 계속 더해주기
    if op == '+':
        num_1 = stack.pop()
        num_2 = stack.pop()
        stack.append(num_1 + num_2)
    # '-'일 경우 지금까지 누적된 값을 빼준다.
    else:
        ans -= stack.pop()

# 스택에 남아있는 숫자를 더해준다.
for number in stack:
    ans += number

# 정답 출력
print(ans)