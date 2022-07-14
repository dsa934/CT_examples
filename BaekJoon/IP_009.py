

'''

 Backjoon _ exampels 1730

  "판화"   by Jinwoo Lee

  < algorithm >


  1. garo, sero status table

     => orders 에서 뽑아낸 명령이 각각 U,D // L,R에 속하는 경우 각각의 좌표에 해당하는 sero, garo status 을 True로 변경


  2. 현재의 좌표 (cur_x, cur_y) 에서 direction 만큼 이동 한 새로운 좌표 (n_x, n_y)가 field 범위를 넘어가는지 체크 

     => garo, sero 표기가 현재의 좌표와, 미래좌표에 중복으로 영향을 주기 떄문



  * 최초 시도에서 bfs 구조를 사용해서 풀이했으나 AC 판정 받지 못함

   => U,D,L,R 여부를 하나의 field_status로 처리 했는데 여기서 문제가 발생한것으로 생각됨 

   => 구현 문제에 해당하는 경우 조건을 일일히 세부적으로 나눠서 판별하는것이 좋을 것으로 생각 됨
 
'''

from collections import deque

def bfs(boundary, garo, sero):

    orders = deque(list(input()))

    cur_x, cur_y = 0 , 0


    # move 
    directions = {'D':[1,0], 'U':[-1,0], 'L':[0,-1], 'R':[0,1]}


    while orders:

        way = orders.popleft()


        if cur_x + directions[way][0] < 0 or cur_y + directions[way][1] < 0 or cur_x + directions[way][0] >= boundary or cur_y + directions[way][1] >= boundary : continue

        n_x = cur_x + directions[way][0]

        n_y = cur_y + directions[way][1]

        if way == 'D' or way =='U' : 

            sero[cur_x][cur_y] = True
            sero[n_x][n_y] = True

        elif way == 'L' or way == 'R' : 

            garo[cur_x][cur_y] = True
            garo[n_x][n_y] = True

        cur_x, cur_y = n_x, n_y



def solution():
    
    boundary = int(input())

    field = [['.' for _ in range(boundary)] for _ in range(boundary)]

    garo = [[ False for _ in range(boundary) ] for _ in range(boundary) ] 
    sero = [[ False for _ in range(boundary) ] for _ in range(boundary) ] 


    bfs(boundary, garo, sero)


    for row_idx in range(boundary):

        for col_idx in range(boundary):

            if garo[row_idx][col_idx] and sero[row_idx][col_idx] : field[row_idx][col_idx] = '+'

            elif garo[row_idx][col_idx] : field[row_idx][col_idx] = '-'

            elif sero[row_idx][col_idx] : field[row_idx][col_idx] = '|'


    for idx in range(boundary):
        print(''.join(field[idx]))

solution()