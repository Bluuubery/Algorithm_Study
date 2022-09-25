# 220831 11047 동전 0

# 정답코드

import sys
input = sys.stdin.readline

# N: 동전 개수, K: 목표 금액
N, K = map(int, input().split())

# coins: 동전
coins = []
for _ in range(N):
    coins.append(int(input()))

# 동전을 내림차순으로 정렬한다.
coins.sort(reverse=True)

# cnt: 동전의 개수
cnt = 0
for coin in coins:
    # 몫만큼 동전의 개수를 더해주고 목표 금액은 나머지가 된다.
    cnt += K // coin
    K = K % coin
    # 목표 금액에 도달하면(K == 0) 중단
    if K == 0:
        break

# 동전의 개수 출력
print(cnt)
