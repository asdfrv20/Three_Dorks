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

# 에리스토스테네스의 체 알고리즘으로 구현
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