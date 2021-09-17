# 기본수학2
# 백준 - 1085번 

import math

x, y, w, h = map(int, input().split())

# 아래 조건의 기준은 1사분면을 (w,h)를 중심으로 나눈 영역들이다. 
if (x==w and 0<y<=h) or (0<x<=w and y==h):
    dist = 0
elif x>w and y>h:
    dist = math.sqrt((w-x)**2 + (h-y)**2)
elif (0< x <=w) and y>h :
    dist = y-h
elif x>w and (0<y<=h):
    dist = x-w
else: 
    dist = min(x, y, w-x, h-y)

print(dist)
