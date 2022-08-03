def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return
    move = 6-start-end
    hanoi(n-1, start, move)
    print(start, end)
    hanoi(n-1, move, end)


N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 3)
