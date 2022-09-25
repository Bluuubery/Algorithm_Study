# 2212 센서

N = int(input())
K = int(input())

sensor = list(map(int, input().split()))
sensor.sort()

result = []
for i in range(len(sensor)-1):
    result.append(sensor[i+1] - sensor[i])
    
result.sort()

if K >= N:
    print(0)
else:
    print(sum(result[:len(result)-K+1]))
