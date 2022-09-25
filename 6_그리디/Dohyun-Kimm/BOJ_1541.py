# BOJ_1541 잃어버린 괄호


equation = input()
stack = list()
sub = 0
total =0
temp = ''
for i in range(len(equation)-1, -1, -1):

    if equation[i].isnumeric():
        temp += equation[i]
    elif equation[i] == '+':
        # 숫자가 뒤집어져 있으니까 다시 원상태 만들고 정수화 시켜서 더하기
        sub += int(temp[::-1])
        # print('+', int(temp[::-1]))
        temp = ''
    elif equation[i] == '-':
        stack.append(-(sub+ int(temp[::-1])))
        # print('-', sub)
        temp = ''
        sub = 0
    if i ==0:
        total = sub + sum(stack) + int(temp[::-1])

print(total)
