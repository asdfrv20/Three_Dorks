# 정렬
# 백준 - 10989번

'''
import sys 
import time

N = int(sys.stdin.readline())

# 파일 가져오기
f = open("D:/gmail_GoogleDrive/Python_Practice/python_graffiti/numbers.txt", 'r')
numbers_str = f.readlines()
f.close()

numbers = numbers_str[0].split(' ')
numbers = numbers[:-1]
numbers = list(map(int, numbers))
'''

import sys 
import time

# 0 리스트를 만드는 함수 
def zerolistMaker(n):
    listofzeros = [0] * n
    return listofzeros

N = int(sys.stdin.readline())

# 카운트 정렬(count sorting) - 한 줄씩 판단
counts = zerolistMaker(10001)
for i in range(N):                      # 한 줄 씩 숫자를 확인하고, 각 숫자 counting
    num = int(sys.stdin.readline())
    counts[num] += 1

for i in range(len(counts)):            # counts>> i: count된 숫자, counts에 저장된 내용: 각 숫자가 등장한 횟수
    for j in range(counts[i]):
        print(i)







