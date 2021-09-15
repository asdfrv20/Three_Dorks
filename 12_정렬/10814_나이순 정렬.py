# 정렬
# 백준 - 10814번

N = int(input())

user_list = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    user_list.append((age, i, name))

user_list.sort()

for user in user_list:
    print(user[0], user[2])

