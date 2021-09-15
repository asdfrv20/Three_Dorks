# 정렬
# 백준 - 1181번

N = int(input())

word_list = []
for i in range(N):
    word = input()
    word_len = len(word)
    word_list.append((word_len, word))

word_list = list(set(word_list))
word_list.sort()

for i in range(len(word_list)):
    print(word_list[i][1])


