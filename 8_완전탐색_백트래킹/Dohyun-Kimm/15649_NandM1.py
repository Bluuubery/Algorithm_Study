# 15469_  N 과 M

# 1부터 N 까지 자연수 중에서 중복 없이 M개를 고른 수열
# permutation
def permutation(arr,n):
    # n:뽑아야할 수열 자리수
    result = []
    if n ==0:
        return [[]]
    else:
        for i in range(len(arr)):
            elem = arr[i]
            for j in permutation(arr[:i]+arr[i+1:],n-1):    # 방금 고른  arr[i] 빼고 나머지 중에서
                result.append([elem] + j)
        return result

a, N = map(int, input().split())
arrr = list(range(1,a+1))
ans = permutation(arrr,N)
for k in range(len(ans)):
    print(' '.join(map(str,ans[k])))
