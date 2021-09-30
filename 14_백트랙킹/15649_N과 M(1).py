# 백트랙킹
# 백준 - 15649번

'''
<백트래킹(backtracking)이란?>
※ 참고 - https://chanhuiseok.github.io/posts/algo-23/
○ 정의: 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 다시 해를 찾아가는 기법
○ 적용 문제: 최적화 문제, 결정 문제 
○ DFS vs 백트래킹
  - DFS(깊이 우선 탐색): 가능한 모든 경로(후보)를 탐색한다.
    >> 불피요할 것 같은 경로를 사전에 차단하거나 하는 행동이 없음!(경우의 수 줄이지 못함, N! 경우의 수 문제 해결 X)
  - backtracking(백트래킹): 해를 찾아가는 도중, 지금의 경로가 해가 될 것 같지 않으면 그 경로를 더이상 가지 않고 되돌아 가는 방법
    == "가지 치기"(불필요한 부분을 고쳐내고 최대한 올바른 쪽으로 간다는 의미)
    >> 반복문의 횟수 줄이기 효율적! 핵심은 가지치기를 얼마나 잘할 것인가...?
○ 백트래킹 특징
  * 특정 조건을 만족하는 경우만 살펴본다
  * 정리: "답이 될만한지 판단하고 그렇지 않으면 그 부분까지 탐색하는 것을 하지 않고 가지치기 하는 것"이 백트래킹
  * 방법: DFS 등으로 모든 경우의 수 탐색 >> 그 과정 중 절대 안될거 같은 상황을 if문으로 정의(이 경우 탐색 중지) >> 이전으로 돌아가 다른 경우 탐색
○ 백트래킹 유망성 판단
  * 해가 될 가능성이 있다 = "유망하다(promising)"
  * 유망하지 않은 노드에 가지 않는다 = "가지치기(pruning) 한다"
'''

# try1: 뭔가 복잡... 정보를 찾아보고 다시 해보자
# 'in'을 써보도록 하자.
'''
import time

N, M = map(int, input().split())

start = time.time()
N_list = list(range(1,N+1))   # N_list: 1~N까지의 자연수를 나타냄
index_list = list(range(M))   # index_list: 출력되는 각 자리가 가리키는 N_list의 인덱스 번호
key = M-1                     # key: 현재 변경대상이 되는 index 번호
end_seq = N_list[N-M:N]       # end_list: 가장 마지막 수열(끝내기 위한 조건으로 걸기)
end_seq.reverse()
seqs = []                      # seq: 현재 수열 저장

while True:
  # seq 추가하기 
  seq_temp = []
  for index in index_list:
    seq_temp.append(N_list[index])
  seqs.append(seq_temp)

  # break 조건 걸기
  if seqs[-1] == end_seq:
    break
  
  # 다음 seq 생성을 위한 index_list 만들기
  # 각 인덱스별로 0~M까지를 지나다가 M에 도달하면 다시 0으로 돌아가야 한다. 이때, 바로 아래 인덱스의 숫자가 1 증가
  index_list[key] += 1
  while True:
    if index_list[key] == N:     # <index_list[key]가 N의 범위를 넘어간 경우 예외처리>
      key -= 1
      index_list[key] += 1       # >>index_list[현재 key]를 0으로 초기화 (key값 변화는 중복 발생 시 설정)
      key += 1
      index_list[key] = 0
  
    # 최빈값 검사 및 중복 검사(※ seq 생성 조건(seq생성 while문 break 조건): 모든 인덱스 숫자에 중복이 없다.)
    mode = 0                          # 1) 최빈값 검사
    for index in set(index_list):   
      if index_list.count(index) > index_list.count(mode):
        mode = index
        break
    # 
    if index_list.count(mode) != 1:    # 2-1) index_list에 중복이 존재할 때, (존재하지 않을 때까지 반복)
      # 중복 처리 잘 해주기
      index_list[key] += 1 
    else:                              # 2-2) 중복이 존재하지 않을 때, seq 확정
      break                             
  key = M-1

# 결과 출력
for seq in seqs:
  for i in seq:
    print(i, end=' ')
  print()
print("time:", time.time()-start)
'''



# try2: while문 + key개념으로 seq([1]*M 리스트)를 높은 인덱스 원소부터 1~N으로 뺑뺑이 돌리고
# 핵심개념: 각 인덱스별로 0~M까지를 지나다가 M에 도달하면 다시 0으로 돌아가야 한다. 이때, 바로 아래 인덱스의 숫자가 1 증가

# 하나더? 인덱스별로 N_list에서 하나씩 고르게하면서 그 원소를 set에서 빼는 형태로 계속 진행한 후, 
'''
N, M = map(int, input().split())

N_list = [i for i in range(1,N+1)]
seq = [i for i in range(1,M+1)] 

selects = set(seq[:-1])
key = M-1
while True:
  candidates = set(N_list) - selects
  for cad in candidates:
    for select in selects:
      print(select, end=' ')
    print(cad)

  candidates
'''


# math.permutations 활용하기 
'''
import math

N, M = map(int, input().split())

N_list = [i for i in range(1,N+1)]
perm = math.permutations(N_list ,M)
False
'''


# try3: 중복이 발생할 경우, 바로 이전으로 돌리기 
# DFS(깊이 우선 탐색)으로 한 거라고 생각함. '중복'을 피하도록만 설정한 것. O(N*N)
# 중복 판단 기준: 대상리스트를 set으로 변화시킨 자료를 민들고 만들고, 둘의 len()을 비교했을 때 같지 않으면 중복 
# 시간초과... ㅠㅜ
'''
import time

def check_overN(seq, N):
  index = str("".join(str(_) for _ in seq)).find(str(N+1))
  return index

N, M = map(int, input().split())

start = time.time()
num_list = [i for i in range(1, N+1)]
seq_list = []
seq = num_list[:M]
if N == M:
  end = [i for i in range(N, 0, -1)]
else:
  end = num_list[N:N-M-1:-1]

while True:
  check_N = check_overN(seq, N)   # M개의 숫자중 어떤 숫자든 N에 도달했을 때
  if check_N != -1:
    seq[check_N-1] += 1
    seq[check_N] = 1

  if len(set(seq)) == M and check_overN(seq, N) == -1:  # 중복된 숫자가 없이 길이가 M인 seq를 seq_list에 저장 
    seq_list.append(''.join((str(_)+' ') for _ in seq)[:-1])

  if seq == end:                   # 무한루프 탈출 조건: 마지막 수열인 end와 같을 떄  
    break
  
  seq[M-1]+=1                      # seq[M-1]이 계속 움직이도록 설정
print('time:', time.time()-start)  
print(seq_list)

# 결과 출력
for seq in seq_list:
  print(seq)
'''


# try4: 하나의 숫자가 선택 될 때마다 후보에서 그 숫자를 지우고 다음 숫자의 후보군을 작성한다.
# whilea문을 활용하여 위 조건 실행
'''
N, M = map(int, input().split())

N_list = [_ for _ in range(1,N+1)]
N_set = set(N_list)   # 1. set(N_list)을 만든다. 
seq_list= []
seq = []
key = 0

while True:           # 2. seq를 하나씩 선택
  seq = 
  key += 1
  if key == M-1:
    break
'''

# 백트래킹이고 나발이고 그냥 풀어보자 

from itertools import permutations
import time

N, M = map(int, input().split())
start = time.time()
N_list = [str(_) for _ in range(1, N+1)]
seq_list = list(map(" ".join, permutations(N_list, M)))
for seq in seq_list:
  print(seq)
print('time:', time.time()-start)
