#  숫자카드2
# 10816

from bisect import bisect_left
from bisect import bisect_right


# 시간초과
# def binary_search(arr,target,start,end):
#     if start > end:
#         return 0
#     mid = (start+end) //2
#
#     if arr[mid] == target:
#         left, right = mid
#         # upper bound
#         up_mid = (mid +(N-1)) //2
#         down_mid = (0 + mid) //2
#         while left > -1:
#             if down_mid
#         # lower bound
#         while right < N:
#             pass
#
#
#
#
#     elif arr[mid] > target:
#         return binary_search(arr, target, start, mid-1)
#     else:
#         return binary_search(arr, target, mid+1,end)
# N = int(input())
# cards = list(map(int, input().split()))
# M = int(input())
# numbers = list(map(int, input().split()))
# cards.sort()
# # print(numbers)
# # print(cards)
# have = [0] * M
# for i in range(M):
#     have[i] = binary_search(cards,numbers[i],0,N-1)
#
#
# print(' '.join(map(str, have)))

# target 값을 찾은 뒤에 똑같은 값을 가진 것들을 하나씩 확인해가면, 똑같은 값이 매우 많은 테스트케이스에서 시간 초과가 난다
# target 값을 찾고나면 그 위치로부터 처음 으로 다른 값이 나오는 위치를 이진 탐색으로 확인하기


N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))
cards.sort()
have=list()
for i in range(M):
    have.append(bisect_right(cards,numbers[i])-bisect_left(cards, numbers[i]))
print(' '.join(map(str,have)))