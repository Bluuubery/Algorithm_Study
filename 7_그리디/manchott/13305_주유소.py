N = int(input())
D = list(map(int, input().split()))
O = list(map(int, input().split()))
idx = result = flag = 0
while idx < N:
    flag = 0
    for next_idx in range(idx + 1, N):
        if O[next_idx] < O[idx] or next_idx == N - 1:
            for d in D[idx:next_idx]:
                result += O[idx] * d
            idx = next_idx
            flag = 1
            break
    if flag:
        continue
    idx += 1
print(result)
# 보류