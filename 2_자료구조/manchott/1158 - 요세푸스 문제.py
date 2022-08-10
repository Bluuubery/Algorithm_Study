N, K = map(int, input().split())
circle = [i for i in range(1, N + 1)]
result = []
num = 0
while circle:
    num = (num + K - 1) % len(circle)
    result.append(circle.pop(num))
print("<" + str(result)[1:-1] + ">")
