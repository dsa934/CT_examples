'''

 Backjoon _ exampels #

  "Baek 14503 - 로봇 청소기 (구현)"   by Jinwoo Lee


 # Attention for Implementation

  1. 영역에 대한 변수 입력 받을때 str /int type 구분 잘해놓기 => for 시간 줄이기

  2. 4방위 관련 문제 풀때 좌표 혼동하지말기 -> 북쪽 이동의 경우 [ -1,0]  -1임 


'''

def is_block(row,col):

    if area[row-1][col] != 0 and area[row+1][col] != 0 and area[row][col-1] != 0 and area[row][col+1] != 0 : return True

    else: return False



N,M = list(map(int,input().split()))
row, col, direction = list(map(int,input().split()))
area = [list(map(int,input().split())) for _ in range(N)]
move = { 0 : [-1,0], 1: [0,1], 2: [1,0], 3: [0,-1]}

cnt = 0

while True:


    if area[row][col] == 0 : 
        area[row][col] = 2
        cnt +=1

    else:
        # 4방향이 막혀있음 
        if is_block(row,col) : 

            # condition 2-3
            if area[ row + move[(direction+2)%4][0]][ col + move[(direction+2)%4][1]] != 1 :

                row, col = row + move[(direction+2)%4][0], col + move[(direction+2)%4][1]
                #direction = (direction+2)%4
                

            # condition 2-4 
            else: 

                break

        else:

            if area[row + move[(direction+3)%4][0] ][col + move[(direction+3)%4][1] ] == 0 :

                row, col = row + move[(direction+3)%4][0], col + move[(direction+3)%4][1]
                direction = (direction+3)%4

            else:
                direction = (direction+3)%4



print(cnt)