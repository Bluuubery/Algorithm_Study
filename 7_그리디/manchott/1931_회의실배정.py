T = [list(map(int, input().split())) for _ in range(int(input()))]
T.sort(key = lambda x:(x[1], x[0]))
end = count = 0
for s, e in T:
    if s >= end:
        count += 1
        end = e
print(count)

