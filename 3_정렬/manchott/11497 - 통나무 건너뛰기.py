def merge_sort(arr):
    # 분할된 배열의 길이가 2보다 작아질 때까지
    if len(arr) < 2:
        return arr

        # 배열을 분할한다.
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    # 정렬한(병합한) 배열들을 담을 임시 배열
    merged_arr = []
    # 분할된 배열들을 정렬하기 위한 인덱스
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        # 작은 값을 배열에 먼저 넣어준다.
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    L = list(map(int, input().split()))
    L = merge_sort(L)
    sort_L = []
    result = 0
    for i in range(N // 2):
        sort_L.append(L.pop(i))
    for i in range(len(L) - 1, -1, -1):
        sort_L.append(L[i])
    for i in range(N):
        temp = abs(sort_L[i] - sort_L[i - 1])
        if temp > result:
            result = temp
    print(result)
