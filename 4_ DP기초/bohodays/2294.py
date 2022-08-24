# 2294 동전2
# 3 15
# 1
# 5
# 12

n, k = map(int, input().split())

# arr = [1, 5, 12]
arr = []
for _ in range(n):
    arr.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
# d = [10001, 10001, 10001, 10001, 10001, 10001, 10001, 10001, 10001, 10001, 10001, 10001, 10001, 10001, 10001, 10001]
d = [10001] * (k + 1)

d[0] = 0
for i in range(n):
    for j in range(arr[i], k+1):
        if d[j - arr[i]] != 10001:
            d[j] = min(d[j], d[j - arr[i]] + 1)
        # 보면서 이해하기
        # print(d)

if d[k] == 10001:
    print(-1)
else:
    print(d[k])