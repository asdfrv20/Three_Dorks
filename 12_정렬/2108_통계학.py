# 정렬 - 통계학
# 백준 - 2108번 


# try1: 시간초과
N = int(input())
numbers = []
for i in range(N):
    number = int(input())
    numbers.append(number)
numbers.sort()                         # 미리 오름차순을 정렬을 하여 뒤 연산을 편하게 하기

# 산술평균
print(round(sum(numbers)/N))

# 중앙값
print(numbers[int((N-1)/2)])            # 원소 개수가 5라면 인덱스는 0 1 2 3 4 이므로 2가 나오려면 (5-1)/2 이므로 (N-1)/2, 
                                        # 인덱스 번호는 정수이야 하기 때문에 형변환을 시켜준다. 
# 최빈값
count = 0
for num in set(numbers):                # step1) 각 숫자의 빈도수를 검사.
    if count <= numbers.count(num):     # 빈도수가 많은 숫자를 count로 넣는다. 
        count = numbers.count(num)
mode_numbers = []                       # step2) 빈도수가 count인 숫자들로 이루어진 수(최빈값)를 mode_number에 저장
for num in set(numbers):
    if count == numbers.count(num):
        mode_numbers.append(num)
mode_numbers.sort()                     # step3) 정렬을 통해 오름차순으로 정렬
# print(mode_numbers)
if len(mode_numbers)==1:                # step4) 최빈값이 1개 나올 경우, 여러개 나올 경우 나누어 출력
    print(mode_numbers[0])
else:
    print(mode_numbers[1])

# 범위
print(numbers[N-1] - numbers[0])
