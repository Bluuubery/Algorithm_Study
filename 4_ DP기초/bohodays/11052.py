# 11052 카드 구매하기

import sys

# dp[1] = 1
# dp[2] = 2 / 2번 카드 1개 or 1번 카드 2개 중 큰 수
# dp[3] = 3 / 3번 카드 1개 or 1과 dp[2] 중 큰 수
# dp[n] = n / n번 카드 1개 or 1과 dp[n-1] or dp[2]와 dp[n-2], ..., dp[i]와 dp[n-i] 
# 점화식 : dp[i] = cards[j] + dp[i-j]

# N = 4
N = int(input())

# 1 5 6 7
cards = list(map(int, sys.stdin.readline().split()))
# 인덱스와 카드 개수를 맞추기 위함. 1번 인덱스 -> 카드 1개 가격
cards.insert(0,0) 

dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], cards[j] + dp[i-j])

print(dp[i])


