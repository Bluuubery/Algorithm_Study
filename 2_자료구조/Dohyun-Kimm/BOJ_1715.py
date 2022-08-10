#백준 1715 카드 정렬하기 
# 20220805
#공통문제
# 두 묶음의 카드를 비교: 두 묶음의 합
# 고르는 순서: 갯수가 가장 적은 묶음을 먼저 고르기.

#리스트안에서 가장 작은수 두개를 pop
# 더한값을 다시 리스트에 넣고
# sort
# def sort(a):
#     for i in range(len(a)):
#         for j in range(i+1,len(a)):
#             if a[i] > a[j]:
#                 a[i],a[j] = a[j],a[i]
#     return a

T= int(input())
num= list()
for _ in range(T):
    num.append(int(input()))
total = 0
#sorting

# find minimum sum
while len(num) >1:
    num = sorted(num)
    #print(num)
    a = num.pop(0) + num.pop(0)
    total.append(a)
    sum += a
    
    if len(num) ==1:
        break
print(total)
    



























# from queue import PriorityQueue
# N=int(input())
# card = PriorityQueue()
# for i in range(N):
#     card.put(int(input()))
# total=0
# for i in range(N):
#     a= card.get()+card.get()
#     print(a)
#     card.put(a)
#     total += a

#print(total)



# # 두 묶음의 합이 최소가 되는 조합을 리스트에 추가
# # 두 묶음을 고를때 최소인것 끼리 비교해야함.
# card.sort()
# #print(card)
# total_stack = list()
# total_stack.append(card[0]+card[1])
# card.pop(0)
# card.pop(0)
# while len(card) != 0:
#     i=0
#     #print(card)
#     #card에 하나 남았을때
#     if len(card) ==1:
#         total_stack.append(total_stack[-1]+card[0])
#         break
#     elif card[i+1] <= total_stack[-1]:
#         total_stack.append(card[i]+ card[i+1])
#         card.pop(i)
#         card.pop(i)
#     else:
#         total_stack.append(total_stack[len(total_stack)-1]+card[i])
#         card.pop(i)
# print(sum(total_stack))

# priorityQueue()


