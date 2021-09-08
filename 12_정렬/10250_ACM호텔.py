# 기본수학1
# 백준 - 10250번 

# 1st try: 

import sys

T = int(input())

RN_list = []
for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    N = N-1
    if H == 1:          # H(층 수)가 1개일 경우
        room_number = '1' + (str(N+1) if N>10 else '0'+str(N+1))
    elif W == 1:        # W(층별 방 개수)가 1개일 경우
        room_number = str(N+1) + '01'
    else:               # 방 번호 = N을 H(층)으로 나눈 나머지 + N을 H(층)으로 나눈 몫
        room_number = str(N%H+1) + (str(0)+str(N//H+1) if N//H+1<10 else str(N//H+1))
    RN_list.append(room_number)

for room_number in RN_list: 
    print(room_number)

# 2nd try: 
'''
import sys 

H, W = map(int, sys.stdin.readline().split())

for N in range(1, H*W+1):
    if H == 1:          # H(층 수)가 1개일 경우
        room_number = '1' + (str(N) if N>=10 else '0'+str(N))
    elif W == 1:        # W(층별 방 개수)가 1개일 경우
        room_number = str(N) + '01'
    else:               # 방 번호 = N을 H(층)으로 나눈 나머지 + N을 H(층)으로 나눈 몫
        room_number = str(N%(H+1) if N%(H+1)!=0 else continue) + (str(0)+str(N//H+1) if N//H+1<10 else str(N//H+1))
    print(room_number)
'''

'''
import sys 

H, W = map(int, sys.stdin.readline().split())

for N in range(H*W+1):
    # 앞자리 Y 연산
    Y = str(N%H+1)
    
    # 뒷자리 X 연산
    if N//H+1 < 10:
        X = str(0)+str(N//H+1)
    else:
        X = str(N//H+1)

    room_number = f'{N}: ' +  Y + ' ' + X
    print(room_number)

'''