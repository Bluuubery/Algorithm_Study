import sys
sys.setrecursionlimit(10**7)

N = int(input())
idx = 1
S = 3
while S < N:
    S = 2 * S + 3 + idx
    idx += 1
def findmoo(s, n, index):
    # print(s, n, index)
    half = (s - index) // 2 - 1
    # S(0) 탈출
    if n == 2 or n == 3:
        return 'o'
    elif n == 1 or n == half:
        return 'm'
    # 앞
    if n < half:
        return findmoo(half, n, index - 1)
    # 정중앙
    if n == half + 1:
        return 'm'
    # 재귀에 들어가지 않는 moo
    elif n < half + index + 3:
        return 'o'
    # 뒤
    else:
        return findmoo(half, n - (half + index + 2), index - 1 )
print(findmoo(S, N, idx))
# N = 17
# 25, 24, 3
# 10, 9, 2
# 3, 2, 1
# 1 3 
# 2 10
# 3 25
# 4 56
# 5 119