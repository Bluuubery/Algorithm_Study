#BOJ_18870_좌표 압축
#2022-08-11

N = int(input())
nums = list(map(int,input().split())) 
# 입력받은 수를 정렬

sorted_nums = sorted(list(set(nums)))
#시간초과.................................


### 좌표 압축을 위해 좌표의 크기순서를 나타내는 딕셔너리 만들기
# 겹치는 수가 있으면 제거해준다
# for r in range(1,len(sorted_nums)):
#     if sorted_nums[r] == sorted_nums[r-1]:
#         sorted_nums.remove(sorted_nums[r])
#print(sorted_nums)
#중복 제거된 리스트 길이에 맞게 인덱스 리스트 생성
idx = range(len(sorted_nums))
# 실제좌표를 키로 가지고 압축 좌표를 값으로 가지는 딕셔너리 생성
ab_dict = dict()
for s in range(len(sorted_nums)):
    ab_dict[sorted_nums[s]] = idx[s]
# {-10: 0, -9:1, 2: 2, 4:3}
#print(ab_dict)
#출력형식에 맞게 출력하기위한 리스트 생성
ans_list = list()
# 입력받은 데이터 순서대로 순회 하면서 실제 좌표와 일치하는 압축좌표를 
# ans_list에 입력받은 순서로 추가
for num in nums:
    if num in sorted_nums:
        ans_list.append(ab_dict[num])
# 출력형식에 맞게 출력
print(' '.join(map(str,ans_list)))
