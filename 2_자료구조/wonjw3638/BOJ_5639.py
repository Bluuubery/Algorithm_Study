num_list = []

while True:
    try : num_list.append(list(map(int, input().split())))
    except : break

# 입력 받은걸로 대소 비교, Tree 만들어가기
# 작으면 left, 크면 right // left, right 애들한테는 root값, root_left, root_right (같은 단계) 추가하기 

class Node:
    def __init__(self, num):
        self.num = num
        self.root = None
        self.left = None
        self.right = None

top_node = num_list[0]
pre_num = top_node

for num in num_list[1:]:
    Node(num)
    if num < pre_num: # 이전에 나온 값보다 작은 경우
        pre_num.left = num
        num.root = pre_num
        pre_num = num
    else: # 이전에 나온 값보다 큰 경우
        if pre_num.root.right:  # 윗단 노드의 오른쪽값이 존재하면
            


##### ??????????????? 모르겠다





# 가장 작은 값 -> 가장 왼쪽 node 
# 가장 작은 값부터 , root_right, root, root_right, <제일 상단노드 나올때에> 오른쪽node의 가장 왼쪽 node부터 다시.. 

