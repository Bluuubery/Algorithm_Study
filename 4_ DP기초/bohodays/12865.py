# 12865 평범한 배낭
# 4 7
# A 6 13
# B 4 8
# C 3 6
# D 5 12

# w  A  B  C  D
# 0  0  0  0  0
# 1  0  0  0  0
# 2  0  0  0  0
# 3  0  0  6  6
# 4  0  8  8  8
# 5  0  0  0 12
# 6 13 13 13 13
# 7  0  0 14 14
N, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

table = [0] * (K+1)

for w, v in arr:
    # 준서가 버틸 수 있는 무게보다 크면 무시
    if w > K:
        continue
    for i in range(K, 0, -1):
        if i + w <= K and table[i] != 0:
            table[i+w] = max(table[i+w], table[i] + v)
    table[w] = max(table[w], v)
print(max(table))

