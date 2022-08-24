#BOJ_1991_트리순회 
#2022-08-09

# 클래스 없이 트리 구현
# list/ dic
#list node 구현이 어려움
# node.left/ node.right를 구현하지 않아도 되는 풀이
# 

N = int(input()) #노드 개수
node = dict()
for _ in range(N):
    root, left, right = map(str,input().split(' '))
    node[root] = left, right


def preorder(a):
    #print -> left ->right
    #left
    if a != '.': # 노드가 비어있는게 아니라면 
        print(a,end='')
        preorder(node[a][0])
    #right
        preorder(node[a][1])
    
def inorder(a):
    #left->print->right
    #left
    if a != '.':
        inorder(node[a][0])
        #print
        print(a,end='')
        #right
        inorder(node[a][1])
    
def postorder(a):
    #left - > right -> print
    if a != '.':
        postorder(node[a][0])
    #right
        postorder(node[a][1])
    #print
        print(a,end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')