# 2294 동전 2
# 못 풀 었 음 !

n, k = list(map(int, input().split()))
arr = list()
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse = True)

stack = []
top = -1
cnt = [0] * n
idx = tmp = 0
answer = 987654321

while True:
    if idx > n:
        if stack:
            cnt, idx = stack.pop()
            top -= 1
            idx += 1
            continue
        else:
            break

    if tmp + arr[idx] == k:
        cnt[idx] += 1
        if sum(cnt) < answer:
            answer = sum(cnt)
            if stack:
                cnt, idx = stack.pop()
                top -= 1
                idx += 1
                continue
            else:
                break
    elif tmp + arr[idx] < k:
        top += 1
        stack.append([cnt, idx])
        cnt[idx] += 1
        tmp += arr[idx]
    else:
        idx += 1

print(answer)