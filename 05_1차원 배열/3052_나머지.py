# 1차원 배열
# 백준 - 3052번

import sys 

rests = set([])
for i in range(10):
    number = int(sys.stdin.readline())
    number %= 42
    rests.add(number)
# print(rests)
print(len(rests))