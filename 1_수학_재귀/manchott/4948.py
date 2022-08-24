result = [False, False, True] + [True, False] * 123456
for number in range(3, 500, 2):
    if result[number]:
        result[number*2::number] = [False] * len(result[number*2::number])
while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n+1, 2*n+1):
        if result[i] == True:
            count += 1
    print(count)
