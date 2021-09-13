# 기본 수학2
# 백준 - 2581번

M = int(input())
N = int(input())

# 소수 찾기 
prime_number = []
for num in range(M, N+1):
    if num != 1:
        for i in range(2, num+1):
            if num%i == 0:
                if num == i:
                    prime_number.append(num)
                    break
                else:
                    break

# 결과 출력: 소수들의 합 & 최솟값
if prime_number == []:
    print(-1)
else:
    print(sum(prime_number))
    print(min(prime_number))
