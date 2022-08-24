#BOJ_2108_통계학
#2022-08-15
#설계시작 2137
# 산술평균, 중앙값, 최빈값, 범위 구하기

# 산술 평균 : 다더해서 length 로 나누기
# 중앙값: length//2 값
# 최빈값: 빈 리스트만들고 하나씩 카운트
# 최대 값 최소 값

N = int(input())
nums = list()
for _ in range(N):
    nums.append(int(input()))

num2 = sorted(nums)
# 평균 구하기

avg = round(sum(num2)/len(num2))
#중앙값 구하기
med = num2[len(num2)//2]
#범위 구하기
num_range = num2[-1] - num2[0]

#최빈값 구하기
num_mod = num2[0]
#최빈값 카운트 할 딕셔너리 선언
mod_dict = dict()
#모든 숫자들을 리스트에 등록
for k in num2:
    if k in mod_dict.keys():
        mod_dict[k] += 1
    else:
        mod_dict[k] =1

max_v = 0
max_k = list()
for v in mod_dict.values():
    if v > max_v:
        max_v = int(v)
for k,val in mod_dict.items():
    if val == max_v:
        max_k.append(k)
if len(max_k) > 1:
    num_mod = max_k[1]
else:
    num_mod = max_k[0]
    
        
# 최빈값 구하기 최빈값 여러개면 두번쨰로 작은 값 출력.

print(avg)
print(med)
print(num_mod)
print(num_range)
