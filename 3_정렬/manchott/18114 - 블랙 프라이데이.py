N, C = map(int, input().split())
W = list(map(int, input().split()))
def find():
    for i in range(N):
        if i == C:
            return 1
        for j in range(i + 1, N):
            if i + j == C:
                return 1
            elif i + j < C:
                if C - (i + j) in W[j+1:]:
                    return 1
    return 0
print(find())