# 문자열
# 백준 - 2941번
# ※ 문자열 제어 명령어 공부에는 엄청 좋은 문제! 

# case1: 수정 전, .count() 사용 안했을 때.
'''
S = input()

count = 0
while True:
    # 크로아티아 알파뱃이 있는지 검사
    if not ((S.find('c=') != -1) or (S.find('c-') != -1) or \
    (S.find('dz=') != -1) or (S.find('d-') != -1) or \
    (S.find('lj') != -1) or (S.find('nj') != -1) or \
    (S.find('s=') != -1) or (S.find('z=') != -1)): 
        break

    # 크로아티아 알파벳 제외시키기
    if S.find('c=') != -1:
        print(S.find('c='))
        S = S.replace('c=', ' ')
        count += 1
        print(S)

    if S.find('c-') != -1:
        S = S.replace('c-', ' ')
        count += 1
        print(S)

    if S.find('dz=') != -1:
        S = S.replace('dz=', ' ')
        count += 1
        print(S)

    if S.find('d-') != -1:
        S = S.replace('d-', ' ')
        count += 1

    if S.find('lj') != -1:
        S = S.replace('lj', ' ')
        count += 1
        print(S)

    if S.find('nj') != -1:
        S = S.replace('nj', ' ')
        count += 1
        print(S)

    if S.find('s=') != -1:
        S = S.replace('s=', ' ')
        count += 1
        print(S)

    if S.find('z=') != -1:
        S = S.replace('z=', ' ')
        count += 1
        print(S)

S = S.replace(' ', '')
print('S:', S)
count += len(S)

print(count)

'''

# case 2: 수정, count 사용
S = input()
Croatia_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count  = 0
for alpha in Croatia_alpha:
    count += S.count(alpha)     # 크로아티아 알파벳 숫자 세기
    S = S.replace(alpha, ' ')   # 크로아티아 알파벳이 빠지고 난 후, 앞뒤 문자가 합쳐져 크로아티아 문자가 되는 것으 방지
S = S.replace(' ', '')
count += len(S)
print(count)
    


