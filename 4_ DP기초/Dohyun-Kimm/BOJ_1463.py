# BOJ_1463_1로 만들기
# 2022-08-20

# %3 ==0 이면 3으로 나눈다
# % 2 == 0 이면 2로 나눈다
# 1을 뺀다.

# n % 6 == 0 인지 확인
# if dp[n-1]: dp[n-1] + 1 , append dp[n]


N = int(input())
dp = [0] * (N + 1)
for n in range(2,N+1):
    dp[n] = dp[n - 1] + 1
    if n % 2 == 0:
        dp[n] = min(dp[n//2] + 1, dp[n])
    if n % 3 == 0:
        dp[n] = min(dp[n//3] + 1, dp[n])


print(dp[N])

'''
N = int(input())
dp = [0] * (N + 1)
for n in range(2,N+1):
    
    if n % 2 == 0:
        dp[n] = min(dp[n//2] + 1, dp[n-1] + 1)
    if n % 3 == 0:
        dp[n] = min(dp[n//3] + 1, dp[n-1] + 1)
    else:
        dp[n] = dp[n - 1] + 1

print(dp[N])




'''
# dp = [0,1,1,1] +[0] * (N-3)

# def tp(n):
#     global dp
#     if dp[n]:
#         return dp[n]
#     else:
#         if n % 3 == 0 and n > 3:
#             # print(f'n={n} {min(tp(n // 3) + 1, tp(n - 1) + 1)}')
#             dp[n] = min(tp(n // 3), tp(n - 1) )  + 1
#             return dp[n]
#         elif n % 2 == 0 and n > 3:
#             # print(f'n={n} {tp(n // 2)} {tp(n - 1)}')
#             dp[n] = min(tp(n // 2), tp(n - 1) ) + 1
#             return dp[n]
#
#         else:
#             # print(dp[n-1] + 1)
#             dp[n] = (tp(n - 1) + 1)
#
#     return dp[n]
#
# print(tp(N))

# dp = [0,1,1,1]
# for n in range(4,N+1):
#     # print(n,end=' ')
#     if n in dp:
#         continue
#     elif n % 2 ==0:
#         dp.append(min( dp[n // 2] + 1, dp[n - 1] + 1))
#     elif n % 3 ==0:
#         dp.append(min(dp[n//3] + 1,dp[n-1] +1))
#     else:
#         # print(dp[n-1] + 1)
#         dp.append(dp[n-1] +1)
#     # print(f'n{n}, append{dp[-1]}')
# print(dp[N])