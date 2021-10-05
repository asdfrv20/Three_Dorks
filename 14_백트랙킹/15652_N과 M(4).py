# 백트래킹
# 백준 - 15652번

# try1: 중복조합, promising 함수 없음
# 결과: 시간초과
'''
def nHm(i, seq):        # 중복조합(nHm): seq 원소들 사이에 중복을 확인할 필요가 없기 때문에 promising 필요 X 
    if i == M:
        seq = seq[1:]
        seq.sort()
        if seq not in seq_list:
            seq_list.append(seq)
    else:
        for j in range(1,N+1):
            seq[i+1] = j
            nHm(i+1, seq)

N, M = map(int, input().split())
seq_list = []
seq = [0] * (M+1)
nHm(0, seq)

# 결과 출력
for seq in seq_list:
    for i in seq:
        print(i, end=' ')
    print()
'''


# try2: promising 함수를 활용하여 seq 의 중복 확인
# 결과: 시간초과 
'''
def promising(seq):     # promising: seq_list에서 seq와의 중복이 있는지 검사하는 함수
    k = 0
    flag = True
    while (k<len(seq_list)-2 and flag):     # promising 조건: len(seq_list)보다 k에 대해서 seq 중복 여부 확인
        if seq in seq_list:                 # 주의: ※ k < (len(seq_list)-2) : index와 현재 seq의 후보 위치 고려
            flag = False
        k += 1
    return flag

def nHm(i, seq):        # nHm: 중복 조합 백트래킹 함수
    if i==M:
        seq = seq[1:]
        if promising(seq):          # promising 검사(seq 중복 검사)
            seq_list.append(seq)    
    else:
        for j in range(seq[i], N+1):
            seq[i+1] = j
            nHm(i+1, seq)

N, M = map(int, input().split())
seq_list = []
seq = [1] * (M+1)
nHm(0, seq)

# 결과 출력
for seq in seq_list:
    for i in seq:
        print(i, end=' ')
    print()
'''


# try3: promising을 좀더 먼저 걸어주기 
# 맞음(4트 맞춤)

def promising(i, seq):        # promising: seq가 seq_list 원소들과 중복이 있는지 확인 
    k = 0
    flag = True
    while (k<i and flag):     
        if seq in seq_list:                
            flag = False
        k += 1
    return flag

def nHm(i, seq):        # nHm: 중복 조합 백트래킹 함수
    if promising(i, seq):
        if i==M:
            seq_list.append(seq[1:])    
        else:
            for j in range(seq[i], N+1):    # range()의 start=seq[i]로 함으로써 중복 후보 제거
                seq[i+1] = j
                nHm(i+1, seq)

N, M = map(int, input().split())
seq_list = []
seq = [1] * (M+1)       # 원소는 모두 1로 초기화
nHm(0, seq)

# 결과 출력
for seq in seq_list:
    for i in seq:
        print(i, end=' ')
    print()