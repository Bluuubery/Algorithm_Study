# 5904 Moo 게임
# 3등분으로 나눠서 생각하기
# ex) S(2) = moo mooo moo / moooo / moo mooo moo
# 나누기 위해서는 나누는 경계값을 알아야 한다.

# (16, 2, 25), (1, 1, 10), (1, 0, 3)
def moo(N, n, length):
    b1 = (length - (n + 3)) // 2    # 10 3 0
    b2 = b1 + n + 3     # 15 7 3

    if 1 <= N <= b1:
        print(1)
        return moo(N, n - 1, length - b2)
    elif b1 + 1 <= N <= b2:
        print(2)
        if N == b1 + 1:
            return 'm'
        else:
            return 'o'
    else:
        print(3)
        return moo(N - b2, n - 1, length - b2)

N = int(input())

# n -> 몇번째 수열까지 확인해야 되는지
# length -> n번째 수열의 길이
# S(0) : moo -> 0 + 3 + 0
# S(1) : moo / mooo / moo -> 3 + 4 + 3
# S(2) : moo mooo moo / moooo / moo mooo moo -> 10 + 5 + 10

n = 0
length = 3
while length < N:
    n += 1
    length = length * 2 + (n + 3)
# N = 11 인 경우, n = 2, length = 25

print(moo(N, n, length))








# 메모리 초과
# k = 1
# while len(moo) < N:
#     moo = moo + 'm' + ('o' * (k+2)) + moo
#     k += 1

