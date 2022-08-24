# BOJ_11052 카드구매하기
# 2022-08-23

# DP. 주어진 카드 수로 최대한 호구 잡히기
# 각 카드 수에 대한 최적해 구하기
# 모든 경우의 수를 비교해서 최적해 판별
# 최적해를 리스트에 저장
# 다음 최적해 구할때 필요하면 사용
# 테뷸레이션 구현하기

N = int(input())        # number of cards
nums = list(map(int, input().split()))  # list of price

# Tabulation
dp = [0] * (N + 1)              # 인덱스 0은 더미로 사용

for i in range(1, N+1):           # 길이가 1 일때 부터 N일때 까지
    max_hogu = -float('inf')    # 최대 값을 구하기위해 최소값으로 초기화
    # 길이별 최적해 구하기
    for j in range(1, i+1):
        # print(f'i:{i} j:{j}')
        # nums 의 인덱스 값과 dp의 인덱스 값이 구하려고하는 카드수와 일치해야함.
        # p 1 5 6 7
        # i =1 카드 개수가 1일때 j =0
        # i =2 일때 num[1] dp[0], num[0] + dp[1]
        # i =3 일때 num[2] dp[0], num[1] + dp[1] , num[0] + dp[2]
        max_hogu = max(max_hogu, nums[i-j] + dp[j-1])
    dp[i] = max_hogu

print(dp[-1])