# 함수 
# 백준 - 4673번()
# ※ 연산시간 줄이기 
# >> num에서 num에서 가까운 수~{num-(자릿수)*9-1}까지만 생성자 검사하기  

import copy
import time

def self_number():
    for num in range(1, 10001):
        count = 0
        for i in range(num+1, 0, -1):
            # 자리나누기 
            dummy = copy.copy(i)
            i_list = []
            while dummy>=10:
                i_list.append(dummy%10)
                dummy //= 10
            i_list.append(dummy)
            count += 1

            # 생성자가 있을 경우 다음 num 검사
            if (sum(i_list)+i) == num:
                break
            # self_num 판단, 자리수에 따라 연산 수 줄이기 
            if i == 1 or count == len(i_list)*9+1:
                print(num)
                break

            # 검사 
            # print("")
            # print("num: ", num)
            # print("i_list:", i_list)
            # print(self_num)

    # for i in range(len(self_num)):
    #     print(self_num[i])
start = time.time()
self_number()
print("time: ", time.time()-start)
