# 기본수학 
# 백준 - 4948번

# 입력 받기
n_list = []
while True:
    n = int(input())
    if n == 0:
        break
    n_list.append(n)

# 소수 판단하기(0~246912 까지 소수 판단하기)
primes = [False, False] + [True]*246911
for i in range(2, len(primes)):
    if primes[i]:
        for j in range(2*i, len(primes), i):
            primes[j] = False

# n보다 크고 2n보다 작거나 같은 소수 출력
for n in n_list:
    count = 0
    for i in range(n+1 , 2*n+1):
        if primes[i]:
            count += 1
    print(count)
