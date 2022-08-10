## 요세 푸스 문제
# 2022-08-05

## N명이 원 모양으로 앉아있고 k번째 사람을 제거
# 7 3 -> 3 6 2 7 5 1 4
# 1 2 3 4 5 6 7
# 3 -> 6 -> 2 -> 7
n=input().split(' ')
Q = list(range(1,int(n[0])+1))
point = int(n[1]) # 몇 번째 사람 제거 할지

#print(Q,point)
# 3 칸마다 출력 +3이 인덱스 넘어가면 len만큼 빼줌 pop사용
#pop해주기 때문에 i가 2씩 증가해야함
ans = list()
i =point-1 # 인덱스에 맞춰주기
while len(Q)!=0: # Q에 있는 값들 다 pop할때까지
    ans.append(Q.pop(i)) # 3 out
    # print(ans)
    # print(Q)
    i += point-1 #pop 하면서 한번 카운트 한게 됨
    
    #리스트 끝까지 갔을때 처음으로 가져오기
    if i >len(Q)-1 and len(Q)!=0: # if i is out of range, prevent 0 divisor
        i =i %len(Q)


str_ans = ', '.join(map(str,ans))
print('<'+str_ans+'>')

# 인덱스 오류 예상을 못함.
# 


    
