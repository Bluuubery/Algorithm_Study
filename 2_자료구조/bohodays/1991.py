import sys

N = int(sys.stdin.readline())
tree = {}

# 반복문을 통해 트리 생성
for i in range(N):
    root, left, right = sys.stdin.readline().split()
    tree[root] = left, right


# 전위 순회 // (루트) (왼쪽 자식) (오른쪽 자식)
def preOrder(v):
    if v != '.': # 자식이 있다면
        print(v, end="") # 루트 노드 출력
        preOrder(tree[v][0]) # 재귀적으로 왼쪽 노드 탐색
        preOrder(tree[v][1]) # 재귀적으로 오른쪽 노트 탐색


# 중위 순회 // (왼쪽 자식) (루트) (오른쪽 자식)
def inOrder(v):
    if v != '.':
        inOrder(tree[v][0]) # 재귀적으로 왼쪽 노드 탐색
        print(v, end="") # 루트 노드 출력
        inOrder(tree[v][1]) # 재귀적으로 오른쪽 노트 탐색


# 후위 순회 // (왼쪽 자식) (오른쪽 자식) (루트)
def postOrder(v):
    if v != '.':
        postOrder(tree[v][0]) # 재귀적으로 왼쪽 노드 탐색
        postOrder(tree[v][1]) # 재귀적으로 오른쪽 노트 탐색
        print(v, end="") # 루트 노드 출력


preOrder('A')
print()
inOrder('A')
print()
postOrder('A')