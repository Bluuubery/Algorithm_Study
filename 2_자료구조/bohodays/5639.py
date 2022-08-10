# 이진 검색 트리
# 후위 순회 // (왼쪽 자식) (오른쪽 자식) (루트)
# BAEKJOON 5639 
# 2022 08 09
import sys
sys.setrecursionlimit(10 ** 6)
 
def postOrder(start, end):
    if start > end:
        return
    
    root = preOrder[start]
    idx = start + 1
 
    while idx <= end:
        if preOrder[idx] > root:
            break
        idx += 1
    
    postOrder(start +1 , idx-1)
    postOrder(idx, end)
    print(root)
 
preOrder = []
while True:
    try:
        preOrder.append(int(sys.stdin.readline()))
    except:
        break
postOrder(0, len(preOrder) - 1)

