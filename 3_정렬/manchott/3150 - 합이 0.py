N = int(input())
A = list(map(int, input().split()))
result = 0

count = 0
for i in range(1 << len(A)):
    sum_arr = count = 0
    for j in range(len(A)):
        if i & (1 << j):
            sum_arr += A[j]
            count += 1
        if count == 3 and sum_arr == 0:
            result += 1
            break
print(result)
