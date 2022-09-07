# BOj_12904 a와 B

# def a_and_b(s, t):
#     # print(M)
#     j = 0
#     # 문자열 두개 길이가 같아질때 까지 반복
#     while len(s) != len(t):
#         j -= 1
#         sub_t = t[j::]
#         # print(len(s))
#         # print(f'sub_t= {sub_t} s= {s}')
#         # 비교하는 문자열이 서로 길이가 다를 때
#         if len(s) != len(sub_t):
#             # print(sub_t[0])
#             # 비교 문자열의 맨앞(새로 추가된 값) 과 s의 마지막 문자 비교
#             if sub_t[0] != s[-1]:
#                 if sub_t[0] == 'B':
#                     # reverse insert
#                     s = s[::-1]
#                     s += 'B'
#                 elif sub_t[0] == 'A':
#                     # insert
#                     s += 'A'
#         # 비교하는 문자열이 길이가 같을때
#         else:
#             if sub_t[0] != s[-1]:
#                 if sub_t[0] == 'B':
#                     s = s[::-1]
#                     s += 'B'
#                 elif sub_t[0] == 'A':
#                     # insert
#                     s += 'A'
#     # print(f's:{s}')
#     if s ==t:
#         return 1
#     else:
#         return 0


# 역으로 연산 해서 풀기
def t_to_s(s, t):
    while t:
        if s == t:
            return 1
        else:
            if t[-1] == 'A':
                t = t[:-1]
            else:
                t = t[:-1]
                t = t[::-1]
    return 0

S = input()
T = input()
# print(S,T)
# print(a_and_b(S, T))
print(t_to_s(S, T))

