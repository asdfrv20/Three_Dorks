# 기본 수학 1
# 백준 - 1193번, 분수찾기
# ※ 제한시간 0.5초 고려해서 점화식 세우려니 매우 어려움

# 1st try - 연산시간 고려 X
'''
import time

X = int(input())

start = time.time()
line_num = 1        # 각 대각선에 1부터 차례로 숫자를 붙인다고 생각한다. 
A = 1               # A: 분자
B = 1               # B: 분모
while True:
    X -= 1

    if X == 0:
        break

    if line_num % 2 == 0:      # 대각선 번호가 짝수 일때,
        if B == 1:
            A += 1
            line_num += 1
        else:
            A += 1
            B -= 1
    else:
        if A == 1:
            B += 1
            line_num += 1
        else:
            A -= 1
            B += 1
    
print(str(A)+'/'+str(B))
print('time: ', time.time()-start)
'''

# 2nd try: 
# 1) 1행의 홀수번째 위치한 분수들이 순서(번째 수)를 An으로 수열식을 생성하여 풀이
# 2) An을 기준으로 X까지 찾아가도록 알고리즘 구현
# ※ An = n*(2n-1)

import time

X = int(input())

start = time.time()
n = 1                   # An 식의 제어 문자
stop = False            # X == An이 되었을 때, loop를 벗어나기 위한 bool 변수
while True: 
    An = n*(2*n-1)          # 1) 기준이 되는 An항 찾기
    if An < X:
        n += 1 
        continue
    else:
        line_num = 2*n-1    # 2) line_num: 몇번째 대각줄에 위치한 경우인지 구하기
        A = 1               #    이 경우, An번째 배열의 분수는 1/line_num
        B = line_num

    while True:             # 3) X번째 분수 구하기
        if An == X:         #    : An번째에서 X번째까지 순번을 줄여가며 X번째 분수 구하기
            stop=True
            break
        if line_num%2 == 1:
            if B == 1:
                line_num -= 1
                A -= 1
            else:
                A += 1
                B -= 1
        else:
            A -= 1
            B += 1
        An -= 1
        # print('An: ', An)
        # print(str(A)+'/'+str(B))
        # print()
    
    if stop:
        break
# print('line_num: ', line_num)
# print('An: ', An)
print('%d/%d' %(A,B))
print('time:', time.time()-start)



