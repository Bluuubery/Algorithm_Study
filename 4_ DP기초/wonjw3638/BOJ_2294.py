# 2294 동전 2
'''
설계 
구현
'''

n, k = list(map(int, input().split()))
arr = list()
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse = True)

stack = []
cnt = [0] * n
top = -1
idx = tmp = cnt = 0

