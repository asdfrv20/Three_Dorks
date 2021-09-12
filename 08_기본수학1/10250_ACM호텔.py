# 기본수학1
# 백준 - 10250번 문제 

T = int(input())

H = []
W = []
N = []
for i in range(T):
    temp_H, temp_W, temp_N = map(int, input().split())
    H.append(temp_H)
    W.append(temp_W)
    N.append(temp_N)

# 방번호 계산
# N%H == 0로 딱 떨어지는 경우의 예외처리가 중요
for i in range(T):
    # Y: 층수
    Y = N[i]%H[i]
    if Y == 0:      # 나머지가 0일때 = H층 배정일때 
        Y = H[i]    # 따라서, 꼭대기 층으로 배정
    Y = str(Y)

    # X: 호수
    if N[i]%H[i]==0:        # N이 H의 배수일 때,
        X = N[i]//H[i]      # 계산시, 호수의 증가 X이므로 그대로
    else:
        X = N[i]//H[i] + 1  # 호수가 하나 증가되어 표현되야 함.(0호는 존재X)

    # X(호수) 문자열 처리
    if X<10:
        X = '0' + str(X)
    else:
        X = str(X)

    room_num = Y + X
    print(room_num)