
'''

 Backjoon _ exampels ####

  "현수막"   by Jinwoo Lee

  < algorithm >

  1. bfs / dfs 기본 문제 

  2. 8방향 이동

  3. '방문하지 않은 node 중에서, 1이라면 

     1) visited 방문 처리
     
     2) queue 에 다음 좌표 추가

     3) 중복 카운팅 방지를 위한 field value = 0 setting


 

'''



from collections import deque

def bfs(row_idx, col_idx, row, col, field, visited):
    
    queue = deque([[row_idx, col_idx]])

    visited[row_idx][col_idx] = True
    field[row_idx][col_idx] = 0

    # move left right up down 11 13 17 19
    drow = [0, 0, -1, 1, -1, -1, 1, 1]
    dcol = [-1, 1, 0, 0, -1, 1, 1, -1]

    while queue :

        _x , _y = queue.popleft()

        for idx in range(8):

            n_x = _x + drow[idx]
            n_y = _y + dcol[idx]

            if n_x < 0 or n_y < 0 or n_x >= row or n_y >= col : continue
            
            if not visited[n_x][n_y] :
                
                if field[n_x][n_y] == 1:

                    queue.append([n_x,n_y])
                    visited[n_x][n_y] = True
                    field[n_x][n_y] = 0



def solution():
    

    row , col = map(int , input().split())

    field = [list(map(int , input().split())) for _ in range(row) ]

    visited = [ [ False for _ in range(col)] for _ in range(row) ]

    answer = 0
    
    for row_idx in range(row):

        for col_idx in range(col):

            if field[row_idx][col_idx] == 1:

                bfs(row_idx, col_idx, row, col, field, visited)
                answer +=1
                

    print(answer)



solution()