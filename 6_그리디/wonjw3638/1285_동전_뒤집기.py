import sys
input = sys.stdin.readline

coinFlip = {
    'T' : 'H',
    'H' : 'T',
}

N = int(input())
coins = [list(input()) for _ in range(N)]
answer = N ** 2

for i in range(1<<N):
    flip = [coins[r][:] for r in range(N)]
    for j in range(N):
        if i & (1<<j):
            for idx in range(N):
                flip[j][idx] = coinFlip.get(flip[j][idx])
    tmp = 0
    for col in range(N):
        t = 0
        for row in range(N):
            if flip[row][col] == 'T': t += 1

        tmp += min(t, N - t)

        if tmp >= answer:
            break
    else:
        answer = tmp

print(answer)