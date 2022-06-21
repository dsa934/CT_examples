
'''

 Backjoon _ exampels 1743

  "음식물 피하기"   by Jinwoo Lee

  < algorithm >

  * bfs를 이용하여 필드 내 장애물('#")에 관련 된 문제를 풀 경우 

  1. 장애물의 시작 좌표 추출

  2. 장애물의 시작 좌표들로 부터 bfs 실행

     1). bfs 실행 후 시작 좌표는 평범한 요소로 변환 ( '#" -> '.' )

     2). 시작 좌표와 인접한 부분의 요소 또한 장애물이라면 평범한 요소로 전환 

     3). 인접 좌표가 범위 밖일 경우 continue

     4). 시작 좌표의 인접 좌표가 평범한 요소일 경우 continue

         if field[n_x][n_y] == '.' : continue

   

'''


from collections import deque

def bfs(x, y, field, row, col):

    queue = deque([[x,y]])

    visited = [ [False for _ in range(col)] for _ in range(row)]

    visited[x][y]= True

    field[x][y] = 0 

    gar_cnt = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    while queue :

        _x, _y = queue.popleft()

        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]


            if n_x < 0 or n_y < 0 or n_x >= row or n_y >= col :
                continue

            if field[n_x][n_y] == 0 : 
                continue


            if not visited[n_x][n_y] and field[n_x][n_y] == 1:

                gar_cnt +=1 

                field[n_x][n_y]= 0

                queue.append([n_x, n_y])
                visited[n_x][n_y] = True
                
    return gar_cnt




def solution():
    
    row, col, garbage = map(int, input().split())

    field = [ [0 for _ in range(col) ] for _ in range(row)]

    for _ in range(garbage):

        _x, _y = map(int, input().split())
        
        field[_x-1][_y-1] = 1


    result = [] 

    for row_idx in range(row):

        for col_idx in range(col):

            if field[row_idx][col_idx] == 1:

                result.append(bfs(row_idx, col_idx, field, row, col))
                
    print(max(result))

solution()