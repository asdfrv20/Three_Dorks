# 기본 수학2
# 백준 - 3009번

x_list = []; y_list = []    # 입력받기
for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for x in set(x_list):       # 입력 받은 x값들 중 홀수인 x값
    if x_list.count(x)%2==1:
        print(x, end=' ')
for y in set(y_list):       # 입력 받은 y값들 중 홀수인 y값
    if y_list.count(y)%2==1:
        print(y)


