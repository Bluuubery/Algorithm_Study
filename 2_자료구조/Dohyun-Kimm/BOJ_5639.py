#BOJ_5639_이진검색트리
#2022-08-09

# input값들 리스트에 저장

# 후위 순회 함수 구현
def postorder(a):
    #left - > right -> print
    if a != '.':
        postorder(tree[a][0])
    #right
        postorder(tree[a][1])
    #print
        print(a,end='')
'''
dict형태로 만들기
temp[0]은 루트 노드
그다음 부터는 이진 탐색트리의 삽입 처럼 구현이 아니라
전위 순회하는 것처럼 노드 삽입

후위 순회 함수 구현

트리의 루트노드 입력

'''
num = list()

#num.append(int(input()))
temp =[50,30,24,5,28,45,98,52,60]
tree = dict()
# {node: (left,right), ---,}

#print(tree)
# preorder 순서로 트리 만들어야 되나
tree[50] = ('.','.')
# 두번째 부터 
'''
for i in temp:
    if temp[i] < tree[0]:
        if tree[0][0] == '.'
            tree[0][0] = temp[i]
            temp[i] = ['.','.']
        else:
            if temp[i] < tree[0][0]:
                if tree
    if temp[i] > tree[0]:
        if tree[0][1] =='.' # 노드가 비어있으면 
            tree[0][1] = temp[i] #그자리에 넣기
            temp[i] = ['.','.']
'''

# 위에 적은 거 함수로 되나
'''
def insert(t): (temp원소)
    if t !='.':
        if t > temp[0] #딕셔너리 키만 가져와서 비교하는 방법 없나....
          insert(tree[])
'''

for i in temp:
    pass
    if i not in tree.keys(): # 노드가 비어있으면
        tree[i] = ['.','.']


# 위의 리스트 가지고 트리 만들기

postorder(temp[0])
#print(num)