# S(k) = S(k-1) + 'm'+'o'*(k+2) + S(k-1)
# moo 게임
# 메모리 초과가 났음
# 풀이: 입력 값보다 긴 문자열이 ㅇ나올떄 까지 moo게임진행
# moo게임 결과로 나온 문자열의 N-1인덱스 출력
import psutil


def moo(s, k):
    if k == 0:
        return s
    else:
        return moo(s, k - 1) + 'm' + 'o' * (k + 2) + moo(s, k - 1)


N = int(input())
start = "moo"
k = 0
while True:
    if len(start) > N:
        break
    else:
        k += 1
        start = moo(start, k)
print(start[N - 1])
p = psutil.Process()
print(p.memory_info().rss / 2 ** 20)

# 해볼만한 다른 풀이
# 길이에 대한 재귀식을 만들기
# ex) moo(k =1) = len(moo(0))*2 + len(m + o*(1+2))
# N 값이 주어졌을 떄 N-1 인덱스가 m이 아니라면 o르 출력
# m이 들어가는 위치만 뽑는 방법을 모르겠음.
