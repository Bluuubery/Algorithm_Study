n = 10000

prime_list = [True] * (n+1)

for i in range(2, int(n**0.5 + 1)):
    if prime_list[i]:
        j = 2
        while i * j <= n:
            prime_list[i*j] = False
            j += 1

T = int(input())

for _ in range(T):
    N = int(input())
    M = N // 2
    for i in range(M,1,-1):
        if prime_list[N - i] and prime_list[i]:
            print(i, N-i)
            break

