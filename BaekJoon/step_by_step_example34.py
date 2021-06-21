'''

 Backjoon _ exampels #

  "Baek 3009 - 네번쨰 점"   by Jinwoo Lee


 # Algorithm 

  0. 직사각형을 만들기 위해 3개의 점이 주어진다면 3개의 점에 대한 x,y좌표에 대하여 적은 수만큼 중복된 좌표가 4번쨰 수의 좌표가 된다 

 # Attention for Implementation



'''

x_list = [] 
y_list = []

for _ in range(3):
    x, y = list(map(int,input().split()))

    x_list.append(x)
    y_list.append(y)

set_x = set(x_list)
set_y = set(y_list)

answer_x, answer_y = 0, 0

if x_list.count(list(set(x_list))[0]) > x_list.count(list(set(x_list))[1]) : answer_x = list(set(x_list))[1]
else: answer_x = list(set(x_list))[0]

if y_list.count(list(set(y_list))[0]) > y_list.count(list(set(y_list))[1]) : answer_y = list(set(y_list))[1]
else: answer_y = list(set(y_list))[0]

print(answer_x, answer_y)