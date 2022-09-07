# 2437 저울
# 입력 예시 : 30 7 6 3 2 1 1


N = int(input())
weight = list(map(int, input().split()))
weight.sort(reverse=True)

# 4 5 7 같은 케이스 방지
ans = 1
while weight:
    tmp = weight.pop()
    if ans < tmp:
        print(ans)
        break
    else:
        ans += tmp
# 1 1 1 1 같은 케이스 방지
else:
    print(ans)

