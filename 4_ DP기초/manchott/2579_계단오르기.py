N = int(input())
stairs = [0] * (N + 2)
for i in range(1, N + 1):
    stairs[i] = int(input())
count = [0] * (N + 2)
count[1], count[2] = stairs[1], stairs[1] + stairs[2]
for i in range(3, N + 1):
    count[i] = max(count[i - 2], count[i - 3] + stairs[i-1]) + stairs[i]
print(count[N])

# 거의 한시간 넘게 고민하다 겨우 풀었음.. 이거도 패턴찾기네
