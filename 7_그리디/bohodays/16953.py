# 16953 A -> B

A, B = map(int, input().split())

# B를 A로 만들기

cnt = 1
while True:
    # B가 짝수면 2로 나눈다.
    if B % 2 == 0:
        B /= 2
    # B의 일의 자리가 1이면 10을 나눈 몫을 가진다(일의 자리가 1이면 제거)
    elif B % 10 == 1:
        B //= 10
    # B가 홀수면 오답 처리 (짝 * 2 = 짝, 홀 * 2 = 짝) (홀 * 홀 = 홀)
    # 1 15 -> 오답
    # 1 11 인 경우는 위의 조건에서 처리된다.
    elif B % 2 == 1:
        print(-1)
        break
    
    cnt += 1

    if A == B:
        print(cnt)
        break
    elif A > B:
        print(-1)
        break