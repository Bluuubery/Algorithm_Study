def check_square(x, y):
    nx, ny = (x // 3) * 3, (y // 3) * 3
    temp = []
    temp.append(grid[nx][ny:ny+3])
    temp.append(grid[nx + 1][ny:ny+3])
    temp.append(grid[nx + 2][ny:ny+3])
    temp_sum = 0
    print(temp)
    for i in temp:
        if 0 in i:
            return 0
        temp_sum += sum(i)

    return temp_sum

def check(x, y):
    if 0 not in grid[x] and 0 not in list(zip(*grid))[y] and not check_square(x, y):
        if sum(grid[x]) == 45 and sum(list(zip(*grid))[y]) == 45 and check_square == 45:
            return True
    return False
    
def sudoku(idx):
    if idx == count:
        return
    x, y = blank[idx]
    for i in range(1, 10):
        grid[x][y] = i
        if check(x, y):
            sudoku(idx + 1)

        
        


grid = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if not grid[i][j]:
            blank.append((i, j))
count = len(blank)
print(check_square(0,1))
print(check_square(1,4))
visited = [[0] * 9 for _ in range(9)]
for i in range(9):
    print(grid[i])


'''
0 3 5 4 6 9 2 7 8
7 8 2 1 4 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0

'''