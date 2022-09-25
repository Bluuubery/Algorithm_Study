# BOJ_11047 동전 0
# N 종류 동전들(개수 제한 없음)
# K 원 만들기
N, K = map(int, input().split())
coins = list()

for _ in range(N):
    coins.append(int(input()))
cnt = 0
i = -1
while K > 0:
    if K >= coins[i]:
        cnt += K // coins[i]
        K = K % coins[i]
    i -= 1

print(cnt)