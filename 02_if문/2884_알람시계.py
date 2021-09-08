# if문 - 연습문제
# 백준 2884번 문제

import sys

H, M = map(int, sys.stdin.readline().split(' '))

# H가 0인 경우
if H == 0:
    if M >= 45:
        print(H, M-45)
    # M<45일때
    else:
        print(23, M+15)
# H가 0이 아닌 경우
else:
    # M>=45일때
    if M >= 45:
        print(H, M-45)
    # M<45일때
    else:
        print(H-1, M+15)