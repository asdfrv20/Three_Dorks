# 기본수학 2
# 백준 - 3053번 

# 유클리드 기하학 vs 택시 기하학
'''
1. 유클리드 기하학
  : 초중고를 통틀어서 우리가 배운 기하학
  >> 두 점 사이의 거리 d = sqrt((x1-x2)**2 + (y1+y2)**2)
2. 택시 기하학
   : 비유클리드 기하학 중 하나
   >> 두 점 사이의 거리 d = |x2-x1|+|y2-y1|

위 정의에 대해서 궁금해서 찾아본 결과 읽어본 글에서 정답에 나와버림;; 
재밋는 부분 뺏겼네
'''
import math
R = int(input())

Euclid_circle = math.pi*R**2
taxi_circle = float(2*R**2)

print("%0.6f" %Euclid_circle)
print("%0.6f" %taxi_circle)