# 정렬 - 좌표 정렬하기 
# 백준 - 11650번 

import sys 

N = int(sys.stdin.readline())
spot_list = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split(' '))
    spot_list.append((x, y))
spot_list.sort()

for i in range(N):
    print(spot_list[i][0], spot_list[i][1])