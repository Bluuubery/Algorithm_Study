N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))

def search(s, e, b):
    if s > e:
        return 0
    middle = (e + s) // 2
    if A[middle] == b:
        return 1
    elif A[middle] > b:
        return search(s, middle - 1, b)
    else:
        return search(middle + 1, e, b)


for i in B:
    print(search(0, N - 1, i))
