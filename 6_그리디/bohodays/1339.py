# 1339 단어 수학

N = int(input())

key = 0
words = []
for _ in range(N):
    words.append(list(input()))

check_dict = {}

for word in words:
    # 1의 자리까지 계산하기 위해 -1을 빼준다.
    sr_num = len(word) - 1
    for alphabet in word:
        if alphabet not in check_dict:
            check_dict[alphabet] = 10 ** sr_num
        else:
            check_dict[alphabet] += 10 ** sr_num
        sr_num -= 1
        # print(check_dict)
# BAAA
# AAAA

resultList = sorted(check_dict.values(), reverse=True)
# print(resultList)

ans = 0
max_number = 9
for i in resultList:
    ans += i * max_number
    max_number -= 1 

print(ans)


