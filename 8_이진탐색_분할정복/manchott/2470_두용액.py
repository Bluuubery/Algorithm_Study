N = int(input())
L = sorted(list(map(int, input().split())))
print(L)

result = abs(L[0] + L[1])
one, two = 0, 0
for i in range(N - 1):
    print(i)
    index = i + 1
    before = abs(L[i] + L[index])
    while index < N:
        temp = abs(L[i] + L[index])
        if temp > before:
            break
        if temp < result:
            result = abs(L[i] + L[index])
            one, two = min(L[i], L[index]), max(L[i], L[index])
        before = temp
        index += 1
print(one, two)
# 보류