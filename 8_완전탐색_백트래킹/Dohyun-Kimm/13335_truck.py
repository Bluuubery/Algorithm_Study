# 백준 13335 트럭

#n: 트럭수,w: 다리의 길이,l: 다리가 버틸수 있는 무게
# 예제: 트럭4대, 다리길이:2 버틸수있는 무게:10
# 풀이 방법
''' 가상의 다리를 리스트로 만들었다.
 다리위의 트럭무게의 총 합이 L이하이고 길이가 w이하가 되도록 유지

 1. 트럭들 리스트에서 deque해오기
    위 조건을 만족하면, append
    다리위에 올라갔으니까 time +=1

    만약 데큐해온 값이 다리의 조건을 하나라도 만족 못하면
    append 0, time+=1
 2. 다리 리스트의 길이가 L과 같아지면
    pop()
    pop한 값이 0이 아니면 시간 +=1
    0이라면 무시
'''
from collections import deque
def count_truck(arr):
    count = 0
    for i in arr:
        if i >0:
            count +=1
    return count
n, w, L = map(int,input().split())
trucks = deque(map(int,input().split()))
bridge = [0]*w
cnt = 0
flag = 1
truck = 0
while flag:
    # 이미 데큐한 값이 트럭에 들어가있으면 데큐 안하고, 0일땐 함
    if not truck and trucks:
        truck = trucks.popleft()
    # print(f'bridge: {bridge[:-1]}')
    # print(f'trucks:{trucks}')

    # 다리의 길이와 무게 조건이 맞다면
    if sum(bridge[:-1]) + truck <= L and len(bridge)<= w:
        bridge.insert(0,truck)
        cnt += 1
        truck = 0
    # 트럭에 있는 값이 0 이고 다리의 길이가 w보다 짧다면
    else:
        bridge.insert(0,0)
        # print(bridge)
        cnt += 1
    print(bridge[:-1])
    # 트럭이 다리를 다 건넜을때
    if len(bridge) > w:
        bridge.pop()
        # 트럭이 완전히 지나간것
    # 건널 트럭이 없고, 다리위에 트럭이 없을떄 까지
    if not trucks and count_truck(bridge) ==0 and not truck:
        flag =0
print(cnt)