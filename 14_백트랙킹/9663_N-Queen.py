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
print('time:', time.time()-start)
