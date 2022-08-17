#백준 2750 수 정렬하기
#2022-08-13
#버블 소트 / 카운트 소트 / 셀렉션 소트 풀이 만들기

# 버블 소트
def bubble(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i] , a[j] = a[j],  a[i]
    return a
# # 셀렉션 소트
# def selectionSort(b):
#     #pointer 
#     idx = 0
#     for i in range(len(b)-1):
#         idx =i
#         # find minimum
#         for j in range(i +1, len(b)): 
#             if b[j] < b[idx]:
#                 idx = j
#         b[idx] , b[i] = b[i] , b[idx]
#     return b
# # 삽입 소트 
# def insertSort(c):
#     for i in range(len(c)-1):
#         pointer = i
#         for j in range(i):
#             if c[j] < c[pointer]:
#                 c[j] , c[pointer] =c[pointer] < c[j]
#                 break
#     return c

# 입력받기
N = int(input())
nums = list()
for _ in range(N):
    nums.append(int(input()))

ans_list = bubble(nums)
for t in range(len(ans_list)):
    print(ans_list[t])
