# 백트래킹
# 백준 - 9663번

# try1 : 
# 결과 - 시간초과 

import time

def promising(i, col):
    k = 1
    flag = True
    while(k<i and flag):            # 아래 조건: 세로&대각선 방향으로 i보다 작은 k행에 Queen이 있는지 조사 
        if (col[i]==col[k] or col[i]+abs(i-k)==col[k] or col[i]-abs(i-k)==col[k]):
            flag = False
        k+=1
    return flag

def n_queen(i, col):
    if promising(i, col):
        if i==N:     # 현재 설정하고 있는 행i가 N일때, cols에 경우의 수 추가 
            cols.append(col[1:])
        else:
            for j in range(1, N+1):
                col[i+1] = j
                n_queen(i+1, col)
N = int(input())

start = time.time()
cols = []
col = [0]*(N+1)
n_queen(0, col)

print(len(cols))
print(cols)
print('time:', time.time()-start)


'''
import time

def promising(i, col):
    k = 0
    flag = True
    while(k<i):            # 아래 조건: 세로&대각선 방향으로 i보다 작은 k행에 Queen이 있는지 조사 
        if (col[i]==col[k] or col[i]+abs(i-k)==col[k] or col[i]-abs(i-k)==col[k]):
            flag = False
        k+=1
    return flag

def n_queen(i, col):
    if promising(i, col):
        if i==N-1:     # 현재 설정하고 있는 행i가 N일때, cols에 경우의 수 추가 
            cols.append(col)
        else:
            for j in range(1, N+1):
                col[i+1] = j
                n_queen(i+1, col)
N = int(input())
4
start = time.time()
cols = []
col = [1]*N
n_queen(0, col)

print(len(cols))
print(cols)
print('time:', time.time()-start)
'''


# try2: 연산시간 줄여보기, board 시각화 자료를 포함시켜보자.
'''
import time

def setBoard(col):
    """
    현재 board 상태를 업데이트하는 함수
    1. Queen의 위치: Q
    2. board에서 놓을수 있는자리와 없는 자리: 가능:O, 불가능: X
    """


def promising(i, col):
    """
    1. 세로줄, 대각선줄의 유망성 여부 판단(promising)
    2. 다음 줄에 놓은 공간이 있는지 판단
    """
    pass

def n_queen(i, col):
    


N = int(input())

start = time.time()
col = [0]*(N+1)
cols = []

n_queen(0, col)

print(count)
print('time:', time.time()-start)
'''
