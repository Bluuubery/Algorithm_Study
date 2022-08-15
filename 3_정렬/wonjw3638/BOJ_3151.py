# 3151_합이 0
# 시간초과 

N = int(input())
students = list(map(int, input().split()))
answer = tmp = tp = 0

for i in range(N-2):
    tmp = students[i]
    for j in range(i+1, N-1):
        tmp += students[j]
        tp = tmp * (-1)
        for k in range(j+1, N):
            if students[k] == tp:
                answer += 1
        tmp -= students[j]

print(answer)