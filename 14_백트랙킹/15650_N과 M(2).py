# 백트래킹 
# 백준 - 15650번


# try1: sort 를 활용하여 중복 검사 
'''
def promising(i, seq):      # promising: 유망성 판단
    k = 1                   # 조건: M개 중 중복이 없는가?를 판단 
    flag = True
    while (k<i and flag):    
        if seq[i]==seq[k]:
            flag = False
        k += 1
    return flag

def nCm(i, seq):
    if promising(i, seq):       # step1) 유망성 판단 
        if i==M:                # step2-1) i번째 seq 요소 == M 일때(수열 길이 충족)
            seq = seq[1:]               # 1번째~M번째 요소들만 가져온 후, 정렬(sort)
            seq.sort()          
            if seq not in seq_list:     # seq_list에 중복이 없다면 추가하기
                seq_list.append(seq)
        else:                   # step2-2) i번째 seq요소 != M 일때, 
            for j in range(1,N+1):      
                seq[i+1] = j            # 1) 다음 수열의 숫자를 1~N까지 넣기
                nCm(i+1, seq)           # 2) seq의 i+1번째로 nCm 재귀호출

N, M = map(int, input().split())
seq_list = []
seq = [0]*(M+1)
nCm(0, seq)

# 결과 출력
for seq in seq_list:
    for i in seq:
        print(i, end=' ')
    print()
'''

# try2: sort를 안쓰고 실행해보기
# 결과: try1 보다 시간이 훨씬 짧아지고 코드 길이 단축 

def promising(i, seq):      # promising: 유망성 판단
    k = 1                   # 조건: M개 중 중복이 없는가?를 판단 
    flag = True
    while (k<i and flag):    
        if seq[i]==seq[k]:
            flag = False
        k += 1
    return flag

def nCm(i, seq):
    if promising(i, seq):       # step1) 유망성 판단 
        if i==M:                # step2-1) i번째 seq 요소 == M 일때(수열 길이 충족)         
            seq_list.append(seq[1:])
        else:                   # step2-2) i번째 seq요소 != M 일때, 
            for j in range(seq[i],N+1):      
                seq[i+1] = j            # 1) 다음 수열의 숫자를 seq[i]~N까지 넣기
                nCm(i+1, seq)           # 2) seq의 i+1번째로 nCm 재귀호출

N, M = map(int, input().split())
seq_list = []
seq = [1]*(M+1)     # seq를 1로 초기화
nCm(0, seq)

# 결과 출력
for seq in seq_list:
    for i in seq:
        print(i, end=' ')
    print()