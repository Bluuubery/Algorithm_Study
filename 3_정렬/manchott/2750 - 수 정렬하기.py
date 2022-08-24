N = int(input())
L = [int(input()) for _ in range(N)]

# 버블 정렬
def bubble(N, L):
    for i in range(N-1):
        if L[i] > L[i + 1]:
            L[i], L[i + 1] = L[i + 1], L[i]
    return L
# result = bubble(N, L)

# 선택 정렬
def select(N, L):
    for i in range(N):
        temp = i
        for j in range(i + 1, N):
            if L[temp] > L[j]:
                temp = j
        L[i], L[temp] = L[temp], L[i]
    return L
# result = select(N, L)

# 삽입 정렬
def insertion(N, L):
    for i in range(N):
        for j in range(i, 0, -1):
            if L[j - 1] > L[j]:
                L[j - 1], L[j] = L[j], L[j - 1]
    return L
result = insertion(N, L)
for i in result:
    print(i)