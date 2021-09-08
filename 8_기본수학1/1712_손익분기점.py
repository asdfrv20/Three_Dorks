# 기본 수학 1
# 백준 - 1712번

# 1st try
'''
import time

A, B, C = map(int, input().split(' '))

start = time.time()
if C-B < 0:
    num = -1
else:
    num = 0
    while True:
        if (A + num*B) < num*C:
            break
        num += 1

print(num)
print('time: ', time.time()-start)

'''

# 2nd try

import math

A, B, C = map(int, input().split(' '))

if C-B <= 0:
    num = -1
else:
    num = math.ceil(A/(C-B))
    if A == num*(C-B):
        num += 1

print(num)
