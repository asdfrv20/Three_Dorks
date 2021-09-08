# 기본 수학 1
# 백준 - 2292번, 벌집
# ※ 부등호 하나 차이가 반례 하나를 놓친다.

N = int(input())

room_num = 1
while True:
    An = 3*room_num*(room_num-1) + 1
    if An >= N: 
        break
    room_num += 1
print(room_num)


