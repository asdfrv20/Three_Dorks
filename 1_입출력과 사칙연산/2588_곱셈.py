# 사칙연산
# 백준 2588번 문제

import sys 
import copy

num1 = int(input(""))
num2 = int(input(""))

# num2 자리수 별로 나누어 list에 저장 
num2_list = []
dummy = copy.copy(num2)
while dummy>10:
    temp = dummy%10
    num2_list.append(temp)
    dummy //= 10
num2_list.append(dummy)
# print(num2_list)

# 결과 출력 
for i in range(len(num2_list)):
    print(num1*num2_list[i])
print(num1*num2)
