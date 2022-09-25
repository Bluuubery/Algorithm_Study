N = int(input())
L = sorted(list(map(int, input().split())), reverse=True)
count = 0
if N < 3:
    print(0)
    exit(0)
for i in range(N):
    s, e = 0, N - 1
    if i == 0:
        s += 1
    if i == N - 1:
        e -= 1
    while s < e:
        if L[s] + L[e] == L[i]:
            count += 1
            break
        elif L[s] + L[e] < L[i]:
            e -= 1
            if e == i:
                e -= 1
        else:
            s += 1
            if s == i:
                s += 1

print(count)
