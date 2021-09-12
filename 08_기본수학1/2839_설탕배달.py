# 기본 수학1
# 백준 - 2839번

N = int(input())

five_sugar = N//5   # 5kg 짜리 설탕봉지
three_sugar = 0     # 3kg 짜리 설탕봉지
least_sugar = N - (five_sugar*5)    # 전체 - 5kg 짜리 설탕량

sugar_num=[]    # 설탕 봉지 수의 합을 저장하는 list
while True:
    if least_sugar%3 == 0:      # 잔여 설탕이 3kg으로 나누어 떨어질 경우
        three_sugar = least_sugar//3
        sugar_num.append(five_sugar+three_sugar)
    five_sugar -= 1             # 5kg 짜리를 더해가며 검사하기 
    least_sugar += 5            # 5kg이 줄어듦으에 따라 나머지 설탕은 늘어남
    if five_sugar == -1:
        break
# print("sugar_num:",sugar_num)

if len(sugar_num) == 0:
    print(-1)
else:
    print(min(sugar_num))


