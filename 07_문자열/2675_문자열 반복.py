# 문자열
# 백준 - 2675번

import sys 

# 입력 및 R, S 분할 
T = int(sys.stdin.readline())
R = []
S = []
for i in range(T):
    temp = sys.stdin.readline().split(' ')
    R.append(int(temp[0]))
    S.append(temp[1][:-1])

# 새로운 문장 P 만들어 출력
for i in range(T):
    P = ""
    for j in range(len(S[i])):
        P += S[i][j]*R[i]
    print(P)