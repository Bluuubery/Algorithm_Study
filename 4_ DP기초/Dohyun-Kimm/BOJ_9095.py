# BOJ_9095_1,2,3더하기
# 2022-08-21

# 설계 : 0820 - 0842
# 작성 : 0842 - 0921
# 6까지 노가다 하니까 찾음
# 식: bp[n] = bp[n-1] + bp[n-2] + bp[n-3]
# 입력받기
T = int(input())

for t in range(T):
    num = int(input())

    # memoization list
    dp = [1] * (11)
    dp[2] = 2
    dp[3] = 4

    # Bottom-up
    if num > 3:
        for n in range(4, num+1):
            dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
    print(dp[num])
