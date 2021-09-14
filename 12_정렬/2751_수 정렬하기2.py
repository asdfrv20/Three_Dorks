# 정렬 - 수 정렬하기2
# 백준 - 2751번 

import sys 

N = int(sys.stdin.readline())
numbers = set([])
for i in range(N):
    number = int(sys.stdin.readline())
    numbers.add(number)

numbers = list(numbers)
numbers.sort()

for i in range(len(numbers)):
    print(numbers[i])