# 문자열
# 백준 - 2908번
# ※ 슬라이싱 응용을 활용하여, 한 줄로 A,B 역정렬 하기

import sys 

A, B = sys.stdin.readline().split(' ')

A = int(A[::-1])
B = int(B[::-1])
# print(A)
# print(B)

print(A) if A>B else print(B)