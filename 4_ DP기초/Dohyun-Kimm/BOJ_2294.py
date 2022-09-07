# BOJ_2294_동전 2
#2022-08-20

# 점화식 세우기
# dp[i] = min(dp[i-1], dp[i])
# 제한사항도 고려하기

N, K = input().split()
N = int(N)
K = int(K)
coinType = list()
for _ in range(N):
    coinType.append((int(input())))

# min 값 구할 거니까 큰 값으로 초기값 설정
dp = [10001] * (K+1)
# 첫번째 인덱스 0으로 설정
dp[0] = 0

for coin in coinType:                       # 코인의 종류 만큼 반복 1 5 12
    for i in range(coin, K+1):              # 각 코인으로  만들수 있는 k원의 조합 구하기 (개수)
        dp[i] = min(dp[i], dp[i-coin] + 1)  # 예제에서 5 , 10, 12 때 dp min값 갱신되는거 확인

# 불가능한 경우에는 -1 출력
if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])

