# 재귀
# 백준 - 10872번
'''
def factorial(N):
    result = 1
    if N == 0:
        return 1
    else:
        result *= N*factorial(N-1)
        return result

N = int(input())
print(factorial(N))
'''

# 재귀로 해본 숏코딩 
def factorial(N):
    return 1 if N==0 else N*factorial(N-1)
print(factorial(int(input())))