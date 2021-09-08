# 문자열
# 백준 - 1152번
# 문자열이 띄어쓰기 하나인 경우 1로 세어지는 것을 처리해주기 

# 답안을 위한 후보실험
'''
string = (input().strip()).split(' ')
print(string)
print(len(string))

string.remove('')
print(string)
print(len(string))
'''

# 최소 답안: 2줄 답안
# 실행시간 - 100ms
# 메모리 - 37376 KB
'''
string = (input().strip()).split(' ')
print(0) if string == [''] else print(len(string))
'''

# sys 활용 답안
# 실행시간 - 104ms
# 메모리 - 37380 KB
import sys 
s = sys.stdin.readline().strip().split(' ')
if s == ['']:
    print(0)
else:
    print(len(s))

