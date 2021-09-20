# 재귀 
# 백준 -  10870번

def fibo(n):
    if n== 0:       # 0번째 피보나치 수열
        return 0
    elif n==1:      # 1번째 피보나치 수열 
        return 1
    else:
        return fibo(n-1)+fibo(n-2)      # 0, 1 번째 피보나치 수열이 아닌 경우, 재귀함수를 호출하여 점화식 계산
print(fibo(int(input())))               # 결과 출력

