N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
count = 0
while K > 0:
    for coin in coins:
        if K // coin:
            count += K // coin
            K %= coin
print(count)
