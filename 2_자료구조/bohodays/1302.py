# 1302 베스트셀러

import collections

T = int(input())

books = []
for _ in range(T):
    books.append(input())

b = collections.Counter(books).most_common(1)
maxV = b[0][1]
ans = []
for k,v in collections.Counter(books).items():
    if v == maxV:
        ans.append(k)

ans = sorted(ans)
print(ans[0])
    
