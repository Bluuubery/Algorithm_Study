kg = int(input())

cnt = 0
for i in range(1667):
    if cnt == 1:
        break
    for j in range(5001):
        if 3*i + 5*j == kg:
            cnt = 1
            print(i + j)
            break
if cnt == 0:
    print(-1)


# N = int(input())
# quotient = N//5
# found = False
# 
# while quotient >= 0:
#     subtracted = N - 5*quotient
#     if subtracted % 3 == 0:
#         num = subtracted//3
#         print(quotient + num)
#         found = True
#         break
#     else:
#         quotient -= 1
# 
# if not found:
#     print(-1)