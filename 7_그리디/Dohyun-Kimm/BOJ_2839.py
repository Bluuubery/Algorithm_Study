# BOJ_2839
# 5, 3 짜리 봉지.  Nkg을 최소한의 봉지를 사용해서 담기
# 조건: 나머지가 없어야함,
# 5를 최대한 쓰고 3의 배수 만큼 남겨서 나머지를 3키로짜리 봉지로 채우기
# 풀이방식 5씩 뺄때마다 카운트 +1,
total = int(input())
i = 0
# N 옮겨 담기
tot = total
while total > 0:
    total -= 5
    i += 1
    if total <5 :
        break
flag =0
# 남은수를 3으로 나눔
# 3으로 안나눠지면 카운트 1개 취소 하고, total에 5 돌려놓기
# 안되면 나눠담을수 없는것으로 -1 출력
while total < tot+1 :
    if total % 3 ==0:
        i += total //3
        print(i)
        flag = 1
        break
    else:
        total += 5
        i -= 1
if flag == 0:
    print(-1)

