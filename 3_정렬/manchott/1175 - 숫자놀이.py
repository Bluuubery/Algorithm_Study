M, N = map(int, input().split())
alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
sort_alpha = []
for i in range(M, N + 1):
    num = str(i)
    temp = []
    for j in num:
        temp.append(alpha[int(j)])
    sort_alpha.append(temp)
result = []
for i in sorted(sort_alpha):
    temp = ''
    for j in i:
        temp += str(alpha.index(j))
    result.append(temp)
idx = 0
while idx < len(result):
    print(' '.join(result[idx:idx+10]))
    idx += 10