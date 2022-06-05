

'''

 Backjoon _ exampels 11123

  "�� �Ѹ���.. �� �θ���"   by Jinwoo Lee


  < algorithm >

  1. field �ȿ� �� ������ ����� �ִ��� chk 

     => ù �繫���� �������� ���� �繫�� üũ �� ���� ���������� ������ '�湮 ��� üũ�� ���ʿ� ' 
 

'''




from collections import deque 


def bfs(field, x, y, raw, col ):

    
    queue = deque([[x,y]])


    # move  left right up down
    dx = [-1 ,1 ,0 , 0]
    dy = [0 , 0, 1, -1]


    while queue :

        _x, _y = queue.popleft()

        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]


            if n_x < 0 or n_y < 0 or n_x >= raw or n_y >= col : 
                continue

            if  field[n_x][n_y] =='#':
                
                field[n_x][n_y]= '.'
                
                queue.append([n_x,n_y])




def solution():

    raw, col = map(int, input().split())

    field = [ list(input()) for _ in range(raw) ]

    
    cnt = 0

    for raw_idx in range(raw):

        for col_idx in range(col):

            if field[raw_idx][col_idx] == '#' :

                cnt+=1

                bfs(field, raw_idx, col_idx, raw,col)

    return cnt

num = int(input())

for _ in range(num):

    print( solution() )

