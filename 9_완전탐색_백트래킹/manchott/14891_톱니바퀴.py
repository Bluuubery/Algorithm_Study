import sys
input = sys.stdin.readline

def change_gear(num, direction):
    # 해당 기어는 돌았다고 표시
    changed[num] = 1
    # 좌, 우의 기어를 먼저 재귀로 바꾼다
    l_gear, r_gear = gears[num][6], gears[num][2]
    # 해당 기어가 왼쪽 끝 기어가 아니고, 다음 기어가 아직 돌지 않았고, 맞물려있는 극이 다르다면
    if num != 0 and not changed[num - 1] and l_gear != gears[num - 1][2]:
        change_gear(num - 1, 0 - direction)
    # 해당 기어가 오른쪽 끝 기어가 아니고, 다음 기어가 아직 돌지 않았고, 맞물려있는 극이 다르다면
    if num != 3 and not changed[(num + 1) % 4] and r_gear != gears[(num + 1) % 4][6]:
        change_gear((num + 1) % 4, 0 - direction)
    # 방향에 맞춰 기어를 돌린다
    if direction == 1:
        gears[num].insert(0, gears[num].pop())
    else:
        gears[num].append(gears[num].pop(0))


gears = [list(input().rstrip()) for _ in range(4)]
N = int(input())
# 기어를 N번 돌린다
for i in range(N):
    # 기어가 이미 돌았는지 확인을 위한 리스트
    changed = [0] * 4
    num, direction = map(int, input().split())
    num -= 1
    change_gear(num, direction)
result = 0
for i in range(4):
    if int(gears[i][0]):
        result += 2 ** i
print(result)
