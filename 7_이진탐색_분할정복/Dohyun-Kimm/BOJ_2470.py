# 두용액 2470
# 1 2 3 4 5 6
# -5 -4 -3 -2 -1
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

start = 0
end = N-1
add = 0
min_pair = [0, 0]
mini = float("inf")
# 이진 탐색
while start < end:
    add = numbers[start] + numbers[end]
    # 새로 계산된 값이 기존 ㄱ최소 값보다 작으면 갱신하기
    if abs(add) < mini:
        mini = abs(add)
        min_pair = [numbers[start], numbers[end]]
    # 차의 절대 값이 0일때 가장 작은 경우우
    if add == 0:
        break
    # 두수의 합이 0보다 작을 경우 작은 쪽 인덱스를 한칸 옮기기
    elif add < 0:
        start += 1
    # 합이 0보다 크다면 큰쪽의 인덱스를 앞으로 당기기
    else:
        end -= 1


print(min_pair[0], min_pair[1])