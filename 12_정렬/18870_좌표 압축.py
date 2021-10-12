# 정렬
# 백준 - 18870번


# try1: sorted 사용해 보자 
# 예상대로 시간초과;;
'''
N = int(input())
num_list = list(map(int, input().split()))
zip_list = list(sorted(set(num_list)))

for num in num_list:
    print(zip_list.index(num), end=' ')
'''

# try2: counting sort 사용 

N = int(input())
num_list = list(map(int, input().split()))






