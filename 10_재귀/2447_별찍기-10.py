# 재귀 
# 백준 - 2447번
# 어떤 느낌인지는 알겠는데 어떻게 풀어야할 지 모르겠네


# try1: 시간 초과 
# 729입력시 2.7초 소요 
'''
import time

def draw_star(N, i, j):
    if i//(N//3)==1 and j//(N//3)==1:
        print(" ", end="")
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
# 결과는 잘 나오지만 시간 초과;; 
'''
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
'''


# try5: 출력을 한줄씩 처리 - print() 호출 횟수를 /N으로 줄임
'''
import time

def draw_star(N, i, j):
    num = N//3
    if i//num==1 and j//num==1: 
        return ' '
    else:
        if N!=3: 
            return draw_star(N/3, i%num, j%num)
        else: 
            return '*'

N = int(input())
start = time.time()

for i in range(N):
    star_line = ''
    for j in range(N):
        star_line += draw_star(N, i, j)
    print(star_line)
            
print('time:',time.time()-start)
'''


# try6: 재귀 안쓰고 해보자. >> 이건 아닌거 같은데;;
'''
N = int(input())

board = ['*'*N for i in range(N)]
blank = []

n = N
while True:
    if n == 1:
        break
    n = n//3
    blank.extend([i for i in range(n, 2*n)])
print(blank)
print(board[0][0] + 'board')
print(len(board[0][0]))

for i in blank:
    for j in blank:
        board[i][j].replace("*", "1")

for i in range(N):
    print(board[i])

'''


'''
import time

def search_blank(N, i):
    num = N//3
    if i//num == 1:
        blank.append(i)
    else:
        if N!=3:
            return search_blank(num, i%num)

N = int(input())
start = time.time()

blank = []
for i in range(N):
    search_blank(N, i)

# 출력
for i in range(N):
    if i not in blank:
        print('*'*N)
        continue
    else:
        for j in range(N):
            if j not in blank: print('*',end='')
            else: print(' ', end='')
        print()
            
print('time:',time.time()-start)
'''


# 내가 짠 코드들 중 그 나마 '틀렸습니다'가 안나오게 바꾼 것.
# 729 입력시 2.2초
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

for i in range(N):
    stars=''
    for j in range(N):
        stars += draw_star(N, i, j)
    print(stars)
print('time:',time.time()-start)
'''


# 검색으로 찾은 1등 코드
# 이게 재귀지;;; 
'''
import time

def concatenate(r1, r2):
    return [''.join(x) for x in zip(r1, r2, r1)]
 
def star10(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star10(n)
    a = concatenate(x, x)
    b = concatenate(x, [' '*n]*n)
 
    return a + b + a

print('\n'.join(star10(int(input()))))
'''

# 위 코드를 참고로 코드 분석하면서 작성해보기..

def star10(n):
    if n == 1:
        return ['*']
    n //= 3
    X = star10(n)
    a = [''.join(x) for x in zip(X, X, X)]
    b = [''.join(x) for x in zip(X, [' '*n]*n, X)]

    return a + b + a

print('\n'.join(star10(int(input()))))



