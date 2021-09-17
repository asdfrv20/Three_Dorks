# 기본 수학2
# 백준 - 4153번

answer = []
while True:
    sides = list(map(int, input().split()))     # 입력받기 
    for i in range(3):
        sides[i] = sides[i]**2
    if sum(sides)==0:                           # 입력이 0 0 0 이면, 반복문 종료 
        break
    # 직각삼각형 판단
    if (sides[0]+sides[1] == sides[2]) or (sides[1]+sides[2] == sides[0]) or (sides[2]+sides[0] == sides[1]):
        answer.append("right")
    else:
        answer.append("wrong")
# 결과 출력
for i in answer:
    print(i)

    