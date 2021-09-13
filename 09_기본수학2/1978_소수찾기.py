# 기본 수학2
# 백준 - 1978번

N = int(input())
num_list = list(map(int, input().split()))

count = 0
for num in num_list:                # num: 소수인지 검사할 수
    if num != 1:                    # 1은 소수가 아니므로 제외 
        for i in range(2, num+1):
            if num%i == 0:          # num%i 나머지가 0일 때,
                if num == i:        # num == i 이면, 인수가 자기자신만 존재 >> 소수
                    count += 1
                    break
                else:               # num != i 이면, 소수 X
                    break
print(count)

        