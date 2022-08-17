#BOJ_1517_버블 소트
#2022-08-13

N = int(input())
num = list(map(int,input().split()))
count =0
# for i in range(len(num)):
#     for j in range( i+1, len(num)):
#         if num[i] > num[j]:
#             num[i], num[j] = num[j], num[i]
#             count +=1
# swap 횟수를 알아 내는 문제
# 버블 소트로 풀 문제가 아닌가
# 각 숫자마다 자신보다 앞에있는 숫자들중 자기보다 큰 숫자의 수만큼 카운트
# 54321이라고 하면
# 1은 앞에 큰숫자가 4개가 있으니까 4
# 2는 3, 3은 2, 4는 1, 따라서 10
# 1 3 2 5 4 를 예로 들면
# 4는 1, 2는 1, 2번?
#               4 3 2 1 0
for i in range(len(num)-1,-1,-1):
    #            i=0 3 2 1 0
    #print('i:',i)
    for j in range(len(num)-1-(len(num)-i),-1,-1):
        #print('j:', j, end=' ')
        if num[i] < num[j]:
            #print(f' i: {num[i]}, j: {num[j]}')
            count +=1 
print(count)
