# 10816 숫자카드2

# 풀이 1

from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards.sort()

M = int(input())
check = list(map(int, input().split()))

ans = [0] * M
for i in range(len(check)):
    ans[i] = bisect_right(cards, check[i]) - bisect_left(cards, check[i])

print(*ans)




# 풀이 2

from collections import Counter

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

count = Counter(cards)
# Counter({10: 3, 3: 2, -10: 2, 6: 1, 2: 1, 7: 1})

for i in range(len(check)):
    if check[i] in count:
        print(count[check[i]], end=' ')
    else:
        print(0, end=' ')

