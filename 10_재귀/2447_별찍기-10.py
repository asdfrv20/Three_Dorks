# 재귀 
# 백준 - 2447번
# 어떤 느낌인지는 알겠는데 어떻게 풀어야할 지 모르겠네


# try1: 시간 초과 
# 729입력시 2.7초 소요 
'''
import time

def draw_star(N, i, j):
    if i//(N//3)==1 and j//(N//3)==1:
        print("1", end="")
    else:
        if N!=3:
            draw_star(N/3, i%(N//3), j%(N//3))
        else:
            print("*", end="")

N = int(input())
start = time.time()
count = 0

for i in range(N):
    for j in range(N):
        draw_star(N, i, j)
    print("")
print('time:',time.time()-start)
'''

# try2: return을 "*", " "으로 해보자.>> 큰 효과 없음.
#       + draw_star에서 if 문에 걸리는 N//3 을 num 이라는 변수로 대체해보자.  
# 729 입력시,  time - 1.6 초
# 
'''
import time

def draw_star(N, i, j):
    num = N//3
    if i//num==1 and j//num==1: 
        return ' '
    else:
        if N!=3: 
            return draw_star(num, i%num, j%num)
        else: 
            return '*'

N = int(input())
start = time.time()
for i in range(N): 
    for j in range(N): 
        print(f"{draw_star(N, i, j)}", end='')
    print("")

print('time:',time.time()-start)
'''

# try3: 전부 문자열로 만든 후, 한번에 출력
# 729 입력 시, 1.47초
'''
import time

def draw_star(N, i, j):
    num = N//3
    if i//num==1 and j//num==1: 
        return " "
    else:
        if N!=3: 
            return draw_star(N/3, i%num, j%num)
        else: 
            return "*"

N = int(input())
start = time.time()
count = 0

stars=''
for i in range(N):
    for j in range(N):
        stars += draw_star(N, i, j)
    stars += "\n"
print(stars[:-1])
print('time:',time.time()-start)
'''


# try4: 불필요한 재귀 경우 없애기, 97번째 줄 if N==3: return "*"; else: return draw_star() 로 변경
# 729 입력 시, 1.12초

import time

def draw_star(N, i, j):
    num = N//3
    if i//num==1 and j//num==1: 
        return " "
    else:
        if N==3: 
            return "*"
        else: 
            return draw_star(N/3, i%num, j%num)

N = int(input())
start = time.time()
count = 0

stars=''
for i in range(N):
    for j in range(N):
        stars += draw_star(N, i, j)
    stars += "\n"
print(stars[:-1])
print('time:',time.time()-start)

