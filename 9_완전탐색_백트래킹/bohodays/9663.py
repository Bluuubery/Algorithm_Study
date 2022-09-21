# 9663 N-Queen

# https://www.youtube.com/watch?v=z4wKvYdd6wM

# 방법 1 (시간초과)
# 같은 열, 대각선 체크
# def promising(col, i):
#     k = 1
#     flag = True
#     while (k < i and flag):
#         if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
#             flag = False
#         k += 1
#     return flag

# def n_queens(col, i):
#     global ans
#     n = len(col) - 1
#     if promising(col, i):
#         if i == n:
#             ans += 1
#             return
#         else:
#             for j in range(1, n + 1):
#                 col[i + 1] = j
#                 n_queens(col, i + 1)

# n = int(input())
# col = [0] * (n + 1)
# ans = 0
# n_queens(col, 0)
# print(ans)



# 방법 2

def promising(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[x] - col[i]) == x - i:
            return False
    return True

def dfs(x):
    global cnt

    if x == n:
        cnt += 1
        return

    for i in range(n):
        if visited[i]: 
            continue

        col[x] = i
        if promising(x):
            visited[i] = True
            dfs(x+1)
            visited[i] = False

n = int(input())
col = [0] * n
visited = [False] * n
cnt = 0

dfs(0)
print(cnt)