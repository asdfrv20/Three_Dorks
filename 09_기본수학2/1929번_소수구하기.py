# 기본수학2
# 백준 - 1929번

# 핵심 알고리즘: 에라토스테네스의 체 - 대표적인 소수 판별 알고리즘
'''
* 참고: https://blog.naver.com/PostView.naver?blogId=ndb796&logNo=221233595886&redirect=Dlog&widgetTypeCall=true&directAccess=false
<에라토스테네스의 체>
- 가장 대표적인 "소수(Prime Number) 판별 알고리즘"
- 
'''

# try1
'''
import time

M, N = map(int, input().split())

# 에라스토스테네스의 체 알고리즘으로 구현
start = time.time()

# step1 - M~N 사이의 모든 자연수를 포함하는 list 생성
num_list = list(range(M,N+1))

# step2 - 아래부터 차래로 특정 숫자의 배수 배제하기 
for i in range(2, N+1):
    for num in num_list:
        if num == -1:
            continue
        if num%i == 0 and num != i:
            num_list[num_list.index(num)] = -1      # 리스트.index(찾을 문자)

# step3 - 출력
for num in num_list:
    if num == 1:
        pass
    elif num != -1:
        print(num)

print('time:', time.time()-start)
'''

# 2nd try: 
'''
import time

M, N = map(int, input().split())

# 에리스토스테네스의 체 알고리즘으로 구현
start = time.time()

# step1 - M~N 사이의 모든 자연수를 포함하는 list 생성
num_list = list(range(M,N+1))
prime_list = list(range(2,N+1))

# step2 - 아래부터 차래로 특정 숫자의 배수 배제하기 
## 1) 1 제외시키기 
# del prime_list[prime_list.index(1)]

## 2) 2부터 시작하여 배수들 제외시키기
for prime in prime_list:
    for num in num_list:
        if num%prime == 0 and num!=prime:
            try:
                del num_list[num_list.index(num)]
            except:
                pass
    # print('i:', num_list)

# step3 - 출력
for num in num_list:
    if M <= num <= N:
        print(num)

print('time:', time.time()-start)
'''

# try3 - count 개념을 넣음 >> count:2에서부터 올라가면서 배수인지 아닌지 검사하는 기준
'''
M, N = map(int, input().split())
num_list = list(range(M,N+1))

count = 1
while True:
    count += 1
    if count == N:
        break
    for num in num_list:
        if num%count == 0 and num!=count:
            if num!=count:
                del num_list[num_list.index(num)]
'''


# try4 - count & prime 개념 도임 
# count: num_list[count]=현재 검사하고 있는 소수.(count보다 인덱스 수가 작으면 전부 소수임, del로 전부 삭제했기 때문)
# prime: 위의 수들을 검사하기 위한 기준 소수는 저장해두는 변수
'''
import time

M, N = map(int, input().split())    # 입력
num_list = list(range(2,N+1))       # M~N까지의 숫자를 가진 list

# 에라토스테네스의 체 알고리즘을 활용한 소수 골라내기
start = time.time()
count = -1                          # prime의 인덱스 초기화
while True:
    count += 1
    if count == len(num_list):      # 인덱스 수 == num_list의미: num_list[:count]가 전부 소수로 이루어져 있음.
        break
    prime = num_list[count]         # 기준 소수인 prime 설정
    
    # num_list에서 소수의 배수들을 배제시키는 과정
    for num in num_list:
        if num%prime == 0 and num!=prime:
            if num!=prime:
                del num_list[num_list.index(num)]

# 결과 출력
for num in num_list:
    print(num)
print('time:', time.time()-start)
'''

# try5: 해당 소수의 "배수를 계산" 후 그 수만 제외시켜, 다른 변수를 검사하는 연산 줄이기 
'''
import time

M, N = map(int, input().split())    
num_list = list(range(2,N+1))       

start = time.time()
count = -1                          
while True:
    count += 1
    if count == len(num_list):
        break
    prime = num_list[count]
    
    # num_list에서 소수의 배수들을 배제시키는 과정
    i = 1
    while True:
        i += 1
        check_num = prime*i
        if check_num > N:
            break
        try:
            del num_list[num_list.index(check_num)]
        except:
            pass

# 결과 출력
for num in num_list:
    print(num)
print('time:', time.time()-start)
'''


# try6: 리스트에 삭제하는 것이 아닌 "소수를 리스트에 추가"하는 형식으로 진행 
'''
import time

M, N = map(int, input().split())

start = time.time()

prime_list = [2]
check_num = 2
while True:
    check_num += 1
    if check_num > N:
        break

    is_prime = True
    for prime in prime_list:
        if check_num%prime == 0: 
            is_prime = False
            break
    if is_prime:
        prime_list.append(check_num)

for num in prime_list:
    print(num)

print('time:', time.time()-start)
'''
    

# try7: try6에서 while문이 아닌 for문을 사용 (check_num)
import time

M, N = map(int, input().split())

# start = time.time()

prime_list = [2]
for check_num in range(3,N+1):
    is_prime = True
    for prime in prime_list:
        if check_num%prime == 0: 
            is_prime = False
            break
    if is_prime:
        prime_list.append(check_num)

for num in prime_list:
    print(num)

# print('time:', time.time()-start)
