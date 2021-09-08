# 문자열
# 백준 - 5622번
# 참고로, 1과 0에는 해당되는 문자가 없기 때문에 고려하지 않아도 된다. 

import math

word = input()

spend_time = 0
for i in range(len(word)):
    string_num = ord(word[i])-65

    if string_num<18:
        dial_num = math.floor((ord(word[i])-65)/3)+2
    elif string_num == 18:
        dial_num = 7
    elif 19<= string_num <=21:
        dial_num = 8
    else:
        dial_num = 9
    
    spend_time += (dial_num+1)

print(spend_time)
