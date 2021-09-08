# 문자열
# 백준 - 1316번

N = int(input())

words = []
for i in range(N):
    word = input()
    words.append(word)

# 그룹 단어 체크
# 단어 숫자 count -> count된 숫자만큼 그 문자 곱해주어 연속된 문자열 생성 -> .find()로 생성된 문자열 찾기
cnt_GW = 0
for word in words:
    check_GW = True             # check_GW: word가 group word 일 때 True, 아니면 False 
    alpha_set = set(word) 

    for alpha in alpha_set:     # 그룹 단어 검사
        if word.find(alpha*word.count(alpha)) == -1:    # 그룹단어가 아닐 때, 
            check_GW = False
            break
        # print(alpha*word.count(alpha))
    if check_GW:                                        # 그룹단어 일 때, cnt_GW를 1 더해주기 
        cnt_GW += 1
print(cnt_GW)



        

    

