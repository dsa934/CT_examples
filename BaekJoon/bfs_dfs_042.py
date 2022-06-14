
'''

 Backjoon _ exampels 1388

  "바닥 장식"   by Jinwoo Lee

  < algorithm >

  1. '-' , 'ㅣ' 가 각각 2개 이상 인접할 경우 1개의 판자로 친다는 말을 어렵게 써놓은듯

    => 각 _type 마다 bfs를 적용

    => 방문체크를 위한 visited table , 방문한 좌표의 모양을 o로 바꿈으로써 중복 cnt 피하기 
 

'''



from collections import deque


def bfs(field ,x ,y , visited, _type, row, col):
    
    queue = deque([[x,y]])

    visited[x][y] = True

    field[x][y] = 'o'

    dx = [ -1, 1 ]
    dy = [ -1, 1 ]

    while queue:

        _x, _y = queue.popleft()

        if _type == '-':

            for idx in range(2):

                n_x = _x 
                n_y = _y + dy[idx]
                
                if n_y < 0 or n_y >= col :
                    continue

                if visited[n_x][n_y] : 
                    continue

                if not visited[n_x][n_y] and field[n_x][n_y] == '-':

                    queue.append([n_x,n_y])
                    field[n_x][n_y] = 'o'
                    visited[n_x][n_y] = True



        elif _type =='|':


            for idx in range(2):

                n_x = _x + dx[idx]
                n_y = _y 

                if n_x < 0 or n_x >= row :
                    continue

                if visited[n_x][n_y]:
                    continue

                if not visited[n_x][n_y] and field[n_x][n_y] == '|':

                    queue.append([n_x,n_y])
                    field[n_x][n_y] = 'o'
                    visited[n_x][n_y] = True




def solution():

    row, col = map(int, input().split())

    field = [list(input()) for _ in range(row)]

    visited = [[False for _ in range(col)] for _ in range(row)]


    cnt = 0


    for row_idx in range(row):

        for col_idx in range(col):

            if field[row_idx][col_idx] == '-':
                cnt+=1
                bfs(field, row_idx, col_idx, visited, '-' , row, col)


            elif field[row_idx][col_idx] == '|':
                cnt+=1
                bfs(field, row_idx, col_idx, visited, '|', row, col )



    print(cnt)





solution()