#소수 판별기 함수
def isprime(a):
    for i in range(2,a):
        if a %i ==0:
            return False
    else:
        return True

# 실행 횟수 입력 받기
T = int(input())


prime_list = list() # 입력 받은 숫자들 리스트
prime_pair = list() # 소수 짝 
prime_filter = list() #소수짝들의 리스트


# 실행횟수 만큼 입력값 받기
for _ in range(T):
    i = int(input())
    prime_list.append(i)

# 소수 짝 찾기
for j in prime_list: #
    mid = j //2 
    while True:
        if isprime(mid) and isprime(j-mid): # 둘다 True라면 소수 짝 찾기 성공
            prime_pair = [mid,j-mid]
            break
        else:
            mid =mid-1
    prime_filter.append(prime_pair)
# 출력 형식 맞추기
for idx in range(len(prime_filter)):
    print(' '.join(map(str,prime_filter[idx])))




# for _ in range(T):
#     i = int(input())
#     for j in range(2,(i)//2+1):
#         if isprime(j) ==True:
#             remain = i -j
#             if isprime(remain) ==True:
#                 prime_pair=[j,remain]
#     prime_list.append(prime_pair)


# 소수의 합으로 구성되는지 확인 하는 반복문 + 차이가 적은 쌍을 업데이트
#출력 형식에 맞게 출력하기
# for idx in range(len(prime_list)):
#     print(' '.join(map(str,prime_list[idx])))





