# 1629 곱셈

import sys

# a : 곱하는 수, b : 곱하는 횟수
def f(a, b):
    if b == 1:
        return a % C

    # a = 2, b = 10, 11
    # 2^10 = 2^5 * 2^5, 2^11 = 2^5 * 2^5 * 2

    else:
        tmp = f(a, b // 2)
        print(a, b, tmp)

        # b가 짝수인 경우
        if b % 2 == 0:
            return (tmp * tmp) % C

        # b가 홀수인 경우
        else:
            return (tmp * tmp * a) % C

A, B, C = map(int, sys.stdin.readline().split())

print(f(A,B))