import math
brt_list= list()
while True:
    T = int(input())
    if T ==0:
        break
    else:
        brt_list.append(T)


#에라토스테네스의 체
def brt(n):
    count =0
    m = 2*n #n 
    prime = [0,0] + ([1] * (m-1)) # 2n까지의 수를 담은 리스트
    
    for i in range(2,int(math.sqrt(m)+1)):
        if prime[i]:
            for j in range(i*2,len(prime),i):
                prime[j]=0
    #n초과 2n이하 소수 개수 카운트
    for k in range(n+1,m+1):
        #print(prime)
        if prime[k] ==1:
            count +=1
    return count


for t in brt_list:
    print(brt(t))

