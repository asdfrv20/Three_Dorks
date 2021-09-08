# 1차원 배열
# 백준 - 4344번
'''
import sys 

C = int(sys.stdin.readline())
N = []
scores = []
for i in range(C):
    temp = list(map(int, sys.stdin.readline().split(' ')))
    N.append(temp[0])
    scores.append(temp[1:])
# print(N)
# print(scores)

# 평균 및 평균 넘는 학생 비율 계산
for i in range(C):
    average = sum(scores[i])/N[i]
    count = 0
    for score in scores[i]:
        # print(score)
        if score>average:
            count += 1
    print("%0.3f%%" %(count/N[i]*100))
'''

# 보녕's 코드 수정해서 풀어보기
'''
a = int(input())    # N: case의 수
b = []              # average_over_percent

for i in range(a):
    list1 = list(map(int, input().split(' ')))
    avg = sum(list1[1:]) / list1[0]     # 여기는 - 연산 굳이 안하고 sum(list1)-list1[0]를 list1[1:]로 수정함. 
    # <확인용 코드 >
    # print(list1)
    # print(avg)
    
    # 평균을 넘는 학생 수 세기 
    student = 0
    for k in list1[1:]:
        if k > avg :
            student += 1

    # 평균을 넘는 학생의 %를 구해서 b 리스트에 추가하기 
    b.append(student/list1[0]*100)      
    """
    1. b.append()만 실행하면 됨.(b=b.append() 로 할 필요 X)
    2. 평균 넘는 사람들 계산해서 append 하는 시점은 "평균을 넘는 학생 수 세기"를 마친 후이어야 한다. 
    3. 변수들은 변수의 기능에 맞게 이름 붙여주세요 ㅠㅜ 가독성이 떨어져서 읽기 힘들어;;
    """

# 결과 출력: 소수점 3자리까지만 나타내기 
for i in range(a):
    print('%0.3f%%' %b[i])
'''

# 보녕 코드 깔끔하게 정리 
'''
a = int(input())
b = []
for i in range(a):
    list1 = list(map(int,input().split()))
    avg = (sum(list1)-list1[0])/list1[0]
    student = 0
    for k in (list1[1:]):
        if k > avg :
            student += 1
    b.append(student/list1[0]*100)
for i in range(a):
    print('%0.3f%%' %b[i])
'''

# 세준이형 코드 
'''
import sys
case = int(input())
percent = [0.000] * case
for i in range(case):
    line = list(map(int, sys.stdin.readline().split())) # 받은 line을 공백 단위로 split해서 list 형태로 저장. + int형태로 전환.
    mean_line = sum(line[1:])/line[0]
    new_line = sorted(line[1:])
    for j, value in enumerate(new_line):
        if value > mean_line:
            percent[i] = ((len(new_line)-j)/len(new_line))
            break
 
for k in range(len(percent)):
    print('%.3f%%' % (percent[k]*100))
'''