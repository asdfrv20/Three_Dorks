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

import time

N, M = map(int, input().split())

start = time.time()
N_list = list(range(1,N+1))   # N_list: 1~N까지의 자연수를 나타냄
index_list = list(range(M))   # index_list: 출력되는 각 자리가 가리키는 N_list의 인덱스 번호
key = M-1                     # key: 현재 변경대상이 되는 index 번호
end_seq = N_list[N-M:N]      # end_list: 가장 마지막 수열(끝내기 위한 조건으로 걸기)
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
  index_list[key] += 1
  while True:
    if index_list[key] == N:    # <index_list[key]가 N의 범위를 넘어간 경우 예외처리>
      index_list[key] = 0       # 1) index_list[현재 key]를 0으로 초기화
      key -= 1                  # 2) 바로 위 우선순위의 index를 key로 지정(key값 1 감소)
      index_list[key] += 1      # 3) 우선 순위가 하나 높은 index를 1 증가시키기
      key += 1
      index_list[key] += 1
    

    # 최빈값 검사
    mode = 0
    for index in set(index_list):   
      if index_list.count(index) > index_list.count(mode):
        mode = index
        break

    if index_list.count(mode) == 1:    # seq 생성 조건(seq생성 while문 break 조건): 모든 인덱스 숫자에 중복이 없다.
      break
    else:                              # <중복이 있을 경우 예외처리>
      key += 1

    if index_list.count(key) != 1: # 중복되는 index가 존재할 경우, 
      index_list[key] += 1         # index_list[key]를 1만큼 옮기기
  key = M-1

# 결과 출력
for seq in seqs:
  for i in seq:
    print(i, end=' ')
  print()
print("time:", time.time()-start)



  