import math
N, S = map(int, input().split())
L = list(map(int, input().split()))
temp = []
for i in L:
    temp.append(abs(i - S))
for i in range(1, N):
    a = temp[i - 1]
    b = temp[i]
    while b != 0:
        a, b = b, a % b
    temp[i] = a
print(temp[-1])

'''
미쳤다 이거!
import math

s = int(input().split()[1])
print(math.gcd(*(int(v) - s for v in input().split())))
'''
