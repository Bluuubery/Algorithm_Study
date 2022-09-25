import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
sub_list = list()
tmp = int(input())
for _ in range(N-1):
    num = int(input())
    sub_list.append(num - tmp)
    tmp = num

n = N - K
sub_list.sort()
answer = sum(sub_list[:n]) + K

print(answer)