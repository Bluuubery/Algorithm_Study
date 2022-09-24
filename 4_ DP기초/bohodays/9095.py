# 9095 1,2,3 더하기

T = int(input())

for _ in range(T):
    n = int(input())
    
    arr = [0, 1, 2, 4]
    ans = 0
    for i in range(n+1):
        if i < 4:
            ans += arr[i]
        else:
            tmp = arr[i-3] + arr[i-2] + arr[i-1]
            arr.append(tmp)
    print(arr[n])