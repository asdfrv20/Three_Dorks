# 정렬 - 좌표 정렬하기 2
# 백준 - 11651번 

import sys 

N = int(sys.stdin.readline())
spot_list = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split(' '))
    spot_list.append((y, x))
spot_list.sort()

for i in range(N):
    print(spot_list[i][1], spot_list[i][0])