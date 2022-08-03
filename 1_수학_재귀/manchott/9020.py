import math

T = int(input())

result = [False, False, True] + [True, False] * 5000
for number in range(3, 101, 2):
    if result[number]:
        result[number*2::number] = [False] * len(result[number*2::number])
for i in range(T):
    N = int(input())
    if N == 4:
        print('2 2')
        continue
    half_N = N // 2
    if not half_N % 2:
        half_N += 1

    for i in range(half_N, N, 2):
        if result[i] and result[N - i]:
            print(N - i, i)
            break
