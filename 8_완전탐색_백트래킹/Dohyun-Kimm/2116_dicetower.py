# 2116_ dice tower
# design: 70?
# 인덱스 매칭 딕셔너리
import copy
pair_dict={
    0: 5,
    5: 0,
    1: 3,
    3: 1,
    2: 4,
    4: 2,
}
# 주사위 수
N = int(input())
# 주사위 입력받기
mat = list()
for _ in range(N):
    mat.append(list(map(int, input().split())))
# 짝 만들기
# (0-5), (1-3), (2-4)
dice = [0] * N

# 주사위 탑을 올라가면서, 바닥과 천장에 놓이는 주사위 면을 제거한다
# 6도 바닥이 될 수 있음
ans = 0
# 1층의 주사위면이 각각 바닥이될때
for w in range(6):
    # w일때 주사위탑의 합 저장
    total =0
    # 원본 배열 훼손되지않게 딥카피
    mat2 = copy.deepcopy(mat)
    ceiling = w

    ceiling_num = mat[0][ceiling]
    floor_num = mat[0][pair_dict.get(ceiling)]
    for f in range(N):
        # 바닥과 천장 인덱스 찾기
        floor = mat2[f].index(ceiling_num)
        ceiling = pair_dict.get(floor)

        # 다음층에서 활용해야하기 때문에 지우기전에 변수에 할당해놓기
        ceiling_num = mat2[f][ceiling]
        floor_num = mat2[f][floor]

        # 할당한뒤에 배열에서 그 값들 지워주기
        mat2[f].remove(ceiling_num)
        mat2[f].remove(floor_num)
    # 전체 총합중 최대값 찾기
    for m in range(N):
        total += max(mat2[m])
    if total > ans:
        ans = total
print(ans)