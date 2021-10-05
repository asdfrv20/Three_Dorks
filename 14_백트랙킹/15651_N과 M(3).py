# 백트래킹
# 백준 - 15651번


def nPim(i, seq):        # 중복순열(nPim): seq의 원소들의 중복을 검사하는 promising은 필요 X
    if i == M:
        seq_list.append(seq[1:])
    else:
        for j in range(1, N+1):
            seq[i+1] = j
            nPim(i+1, seq)

N, M = map(int, input().split())
seq_list=[]
seq = [0] * (M+1)
nPim(0, seq)

# 결과 출력
for seq in seq_list:
    for i in seq:
        print(i, end=' ')
    print()
