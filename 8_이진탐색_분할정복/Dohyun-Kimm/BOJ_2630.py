# 분할정복 색종이 만들기
# N = 1, 2, 4, 8, 16, 32, 64, 128

def cut_paper(arr, rs, re, cs,ce):  # row_start, row end, col_start, col_end
    global blue
    global  white
    # 색종이의 모든 칸이 같은 색인지 확인
    print(f'blue:{blue}, white:{white}')
    if re >1:
        print(f'rs{rs} re:{re} cs:{cs} ce:{ce}')
        for j in range(rs, re):
            for k in range(cs, ce):
                # print(f'j{j} k:{k}  rs:{rs} cs:{cs}')
                # print(f'arrjk:{arr[j][k]} arr[rs][cs]:{arr[rs][cs]}')
                # print(f'arr2,0 {arr[2][0]}')
                if arr[j][k] != arr[rs][cs]:
                    # 같은색이 아니라면 n //2 해서 4개로 쪼갠다음 재귀 함수에 넣어야함.
                    print('next range',rs,re//2,re, cs,ce//2, ce)
                    for _ in range(4):
                        # 0,0
                        cut_paper(arr[rs: re//2][cs: ce//2],rs, re//2,cs, ce//2)
                        # 0,1
                        cut_paper(arr[re//2: re][cs : ce//2], re//2, re, cs, ce // 2)
                        # # 1,0
                        cut_paper(arr[rs: re//2][ce//2:ce],rs,re//2,ce//2,ce)
                        # # 1,1
                        cut_paper(arr[re//2: re][ce//2 : ce],re//2, re, ce//2, ce)
                        # 그리고 반복문 끝내기
                        break
        # for문을 통과하면 모든 색이 같음
        if arr[rs][cs] == 1:
            blue += (re-rs)**2
            return
        else:
            white += (re-rs)**2
            return
    elif rs-re ==1:
        if arr[rs][cs] ==1:
            blue += 1
            return
        else:
            white += 1
            return



N = int(input())
mat = [0] * N
for i in range(N):
    mat[i] = list(map(int, input().split()))
    print(mat[i])

blue = white = 0
cut_paper(mat,0,N,0,N)
print(blue)
print(white)
# print(mat)
