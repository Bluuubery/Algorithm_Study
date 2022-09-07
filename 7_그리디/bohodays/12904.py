# 12904 A와 B

S = list(input())
T = list(input())

while True:
    # S의 뒤에 A를 추가한다 -> T의 뒤에 A를 제거한다, 
    if T[-1] == 'A':
        T.pop()
    # S를 뒤집고 뒤에 B를 추가한다 -> T의 마지막 요소를 제거하고 뒤집는다.
    else:
        T.pop()
        T = T[::-1]
    
    if len(S) == len(T):
        if S == T:
            print(1)
        else:
            print(0)
        break

