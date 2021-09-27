# 기본수학2
# 백준 - 9020번

import time

T = int(input())
N_list = []
for i in range(T):
    N = int(input())
    N_list.append(N)

start = time.time()

# 소수 저장하기(에라토스테네스의 체 알고리즘 적용)
primes = [False, False] + [True]*9999
for i in range(2, len(primes)):
    if primes[i]:
        for j in range(2*i, len(primes), i):
            primes[j] = False

# 골드바흐 파티션 선별 및 출력
for N in N_list:
    G_partition1 = N//2         # N//2 인 지점에서 시작해서 그 수에 가장 가까운 숫자들이 골드바흐 파티션이 된다.
    while True:
        G_partition2 = N - G_partition1
        if primes[G_partition1] and primes[G_partition2]:
            print(G_partition1, G_partition2)
            break
        else:
            G_partition1 -= 1
print("time:", time.time()-start)


