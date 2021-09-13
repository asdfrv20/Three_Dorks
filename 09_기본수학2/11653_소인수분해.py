# 기본 수학2
# 백준 - 11653번

N = int(input())

while True:
    if N == 1:                      # N이 1일 경우, while문을 나가도록 설정 
        break
    else:                           # N != 1 일경우
        for i in range(2, N+1):     # 2부터 작은 순서대로 N을 나누고, 나머지가 0이면 소인수 출력
            if N % i == 0:          # 주의! range()의 범위는 (2, N)이 아닌 (2, N+1이어야 한다.)
                print(i)
                N //= i             # N//i 값을 다시 N에 대입
                break
