# 기본수학1
# 백준 - 1011번

T = int(input())
x = []
y = []
for i in range(T):
    temp_x, temp_y = map(int, input().split())
    x.append(temp_x)
    y.append(temp_y)

number = []
for i in range(T):
    length = y[i] - x[i]
    
    # 대략적인 범위 구하기 
    count = 1
    sum_count = 0
    while True:
        sum_count += (count*2)
        if sum_count >= length:
            break
        count += 1

    # 이동장치 동작 횟수 구하기 
    if (sum_count-length) < count:
        num = count*2
    else:
        num = count*2-1
    number.append(num)

# 결과 출력 
for i in range(T):
    print(number[i])


    