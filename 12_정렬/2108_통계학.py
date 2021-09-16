# 정렬 - 통계학
# 백준 - 2108번 

import time

# try1: 시간초과
'''
N = int(input())
numbers = []
for i in range(N):
    number = int(input())
    numbers.append(number)
numbers.sort()                         # 미리 오름차순을 정렬을 하여 뒤 연산을 편하게 하기

start = time.time()

# 산술평균
print(round(sum(numbers)/N))

# 중앙값
print(numbers[int((N-1)/2)])            # 원소 개수가 5라면 인덱스는 0 1 2 3 4 이므로 2가 나오려면 (5-1)/2 이므로 (N-1)/2, 
                                        # 인덱스 번호는 정수이야 하기 때문에 형변환을 시켜준다. 
# 최빈값
count = 0
numbers_set = set(numbers)
for num in numbers_set:                # step1) 각 숫자의 빈도수를 검사. 최빈값의 count 수 확정하기
    temp = numbers.count(num)                
    if count <= temp:                   # 최빈값이 등장 횟수를 count로 넣는다. 
        count = temp

mode_numbers = []                       # step2) 빈도수가 count인 숫자들로 이루어진 수(최빈값)를 mode_number에 저장, 중복 허용
for num in numbers_set:
    if count == numbers.count(num):
        mode_numbers.append(num)
mode_numbers.sort()                     # step3) 정렬을 통해 오름차순으로 정렬
if len(mode_numbers)==1:                # step4) 최빈값이 1개 나올 경우, 여러개 나올 경우 나누어 출력
    print(mode_numbers[0])
else:
    print(mode_numbers[1])

# 범위
print(numbers[N-1] - numbers[0])
print('time:', time.time()-start)
'''

# try2: 최빈값에 카운팅 정렬 대입

import time

N = int(input())
numbers = []
for i in range(N):
    number = int(input())
    numbers.append(number)
numbers.sort()                         # 미리 오름차순을 정렬을 하여 뒤 연산을 편하게 하기

start = time.time()

# 산술평균
print(round(sum(numbers)/N))

# 중앙값
print(numbers[int((N-1)/2)])           

# 최빈값: counting sort(시간 단축)
counting_sort = [0]*8001             # 입력 정수 범위: -4000 ~ 4000 // index 범위(입력 정수 범위+4000): 0 ~ 8000

for num in set(numbers):             # counting sort: set(numbers)와 numbers.count(num)으로 for문의 연산횟수 줄이기
    counting_sort[num+4000] += numbers.count(num)

mode_check = counting_sort.count(max(counting_sort))        # mode_check: 최빈값의 갯수
mode_index = counting_sort.index(max(counting_sort))        # mode_index: counting_sort의 인덱스 값-4000 = 해당 숫자 이용
# print('mode_check:', mode_check)
# print('mode_index:', mode_index)
if mode_check == 1:
    print(mode_index-4000)
else: 
    print(counting_sort[mode_index+1:].index(max(counting_sort)) + mode_index - 3999)   # 두번째로 작은 최빈값 찾기(슬라이싱 이용)

# 범위
print(numbers[N-1] - numbers[0])
print('time:', time.time()-start)



# try3: try2에서 중간에 있는 numbers.sort()를 카운팅 정렬로 바꾸어보자
import time

N = int(input())
numbers = []
for i in range(N):
    number = int(input())
    numbers.append(number)
start = time.time()

# counting sort(카운팅 정렬) 실행
counting_sort = [0]*8001             # 입력 정수 범위: -4000 ~ 4000 // index 범위(입력 정수 범위+4000): 0 ~ 8000
for num in set(numbers):             # counting sort: set(numbers)와 numbers.count(num)으로 for문의 연산횟수 줄이기
    counting_sort[num+4000] += numbers.count(num)

# 산술평균
print(round(sum(numbers)/N))

# 중앙값: 이 부분 for 문 없애기 
count = 0
for i in range(len(counting_sort)):
    if counting_sort[i] != 0:
        count += counting_sort[i]
        if count >= (len(numbers)+1)/2:
            median = i-4000
            break
print(median)

# 최빈값: counting_sort 활용하여 for문 없앰
mode_check = counting_sort.count(max(counting_sort))        # mode_check: 최빈값의 갯수
mode_index = counting_sort.index(max(counting_sort))        # mode_index: counting_sort의 인덱스 값-4000 = 해당 숫자 이용
if mode_check == 1:                                         # 출력
    print(mode_index-4000)
else: 
    print(counting_sort[mode_index+1:].index(max(counting_sort)) + mode_index - 3999)   # 두번째로 작은 최빈값 찾기(슬라이싱 이용)

# 범위
print(max(numbers) - min(numbers))
print('time:', time.time()-start)





