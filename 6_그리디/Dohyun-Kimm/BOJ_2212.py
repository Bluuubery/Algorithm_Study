# 센서 BOJ_2212

N = int(input())
K = int(input())
coors = list(map(int, input().split()))
coors.sort()

# 각 좌표들 사이의 거리 구하기
distance_list = list()
for i in range(1, N):
    distance_list.append(coors[i] - coors[i-1])
distance_list.sort()
# 거리들이 들어있는 리스트는 N-1 큰 값 부터 k-1개 빼고 합 더하기
# print(len(distance_list) - (K-1))
# print(distance_list)
ans = sum(distance_list[:len(distance_list) -(K-1)])
print(ans)
