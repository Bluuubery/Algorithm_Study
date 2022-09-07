def dfs(x):
	global visited
	global count
	visited[x] = 1
	count += 1
	for i in grid[x]:
		if not visited[i]:
			dfs(i)


V = int(input())
E = int(input())
grid = [[] for _ in range(V + 1)]
for i in range(E):
	s, e = map(int, input().split())
	grid[s].append(e)
	grid[e].append(s)
visited = [0] * (V + 1)
count = -1
dfs(1)
print(count)
