# 기본수학1
# 백준 - 2775번

import copy

def sum_layer(k, n):
    up_layer = list(range(1, n+1))
    # print('up_layer:', up_layer)
    
    for j in range(k-1):                            # j for 반복문: k-1층 까지 더해서 올라오는 과정을 반복 
        down_layer = copy.copy(up_layer)            # 다음 up_layer를 구하기 위해 down_layer로 값 내리기 
        for i in range(n):                  
            up_layer[i] = sum(down_layer[:i+1])     # i for 반복문: j층에서 1부터 n호까지의 사람서 더해주기 
        # print(f'{j}번째')
        # print('up_layer:', up_layer)
        # print('down_layer: ', down_layer)
        
    return sum(up_layer)

# 입력 받기 
T = int(input())

k = []
n = []
for i in range(T):
    temp_k = int(input())
    k.append(temp_k)
    temp_n = int(input())
    n.append(temp_n)

# 계산 및 결과출력
for i in range(T):
    print(sum_layer(k[i], n[i]))
