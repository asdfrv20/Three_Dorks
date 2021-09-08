# 1차원 배열 
# 백준 - 2577번

import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

prod_num = A * B * C

# 한 자리씩 분할하여 list에 저장
num_list = []
while prod_num>10:
    temp = prod_num % 10
    prod_num //= 10
    num_list.append(temp)
num_list.append(prod_num)
# print(num_list)

# 등장한 숫자들의 갯수 출력
for i in range(10):
    print(num_list.count(i))
