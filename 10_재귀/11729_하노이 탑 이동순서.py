# 재귀
# 백준 - 11729번
'''
[내가 내 손으로 하노이 탑을 하는 방법의 기준]
- start: 판들이 초기에 놓여있는 pole
- temp: start, dest가 아닌 나머지 pole
- dest: 가고자 하는 목적지 pole
※ n = 1일때는 start->dest로 한 번만 이동하면 됨. 
>> 판의 개수가 'n개'일 때, 모든 판들이 start->dest로 가기 위해선 가장 아래 판을 제외한 'n-1개'의 판들이 
   start->temp로 이동하고, 가장 아래 판이 목적 pole로 이동한 후 다시 n-1개의 판들은 temp->dest로 이동해야함. 
step1) (가장 아래 판을 제외한) n-1개의 판들이 start->temp로 pole이동
step2) 가장 아래 판이 start->dest로 이동 
step3) (temp에 위치한) n-1개의 판들이 temp->dest로 pole이동
'''

# try1 기본개념만으로 짠 코드 >> 위 개념들을 활용하여 count 없이 그냥 출력하도록 설정 
# 아무 생각없이 위 개념대로 출력하도록만 했는데 되는게 너무 신기하네;;; 
'''
def hanoi(start, dest, temp, n):
    global count 
    if n == 1:
        print(start, dest)
        count += 1
    else: 
        hanoi(start, temp, dest, n-1)   # step1
        print(start, dest)              # step2
        hanoi(temp, dest, start, n-1)   # step3
N = int(input())
hanoi(1,3,2, N)
'''



# try2: 내용 정리 및 count & 이동 순서 출력
def hanoi(start, dest, temp, n):
    global count 
    if n == 1:
        move_list.append((start, dest))
        count += 1
    else: 
        hanoi(start, temp, dest, n-1)   # step1
        move_list.append((start, dest)) # step2              
        count += 1
        hanoi(temp, dest, start, n-1)   # step3

N = int(input())
count = 0
move_list = []
hanoi(1,3,2, N)

print(count)
for idx, i in enumerate(range(len(move_list))):
    print(idx+1, ':', move_list[i][0], move_list[i][1])


