

'''

 Backjoon _ exampels 3184

  "¾ç"   by Jinwoo Lee

  < algorithm >

  1. basic -bfs/dfs problem

 

'''




from collections import deque

def bfs(x,y, field, visited, row, col):
    
    queue = deque([[x,y]])
    visited[x][y] = True

    _vcnt, _ocnt =  0, 0

    if field[x][y]=='v' : 
        _vcnt +=1
        field[x][y]='.'

    elif field[x][y] =='o' :
        _ocnt +=1
        field[x][y]='.'


    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue :

        _x, _y = queue.popleft()


        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]


            if n_x < 0 or n_y < 0 or n_x >= row or n_y >= col:
                continue

            if field[n_x][n_y] =='#' :
                continue

            if not visited[n_x][n_y] :

                if field[n_x][n_y]=='o':
                    _ocnt +=1                  
                    field[n_x][n_y]='.'

                elif field[n_x][n_y]=='v':
                    _vcnt +=1
                    field[n_x][n_y]='.'

                queue.append([n_x,n_y])
                visited[n_x][n_y]=True


    if _ocnt > _vcnt : _vcnt = 0

    else: _ocnt =0 

    return _ocnt, _vcnt







def solution():

    row, col = map(int, input().split())

    field = [ list(input()) for _ in range(row) ]
    
    visited = [ [False for _ in range(col)] for _ in range(row) ]
    o_cnt, v_cnt = 0,0 
    
    for row_idx in range(row):

        for col_idx in range(col):

            if field[row_idx][col_idx] == 'v' or field[row_idx][col_idx] == 'o' :
                
                _ocnt, _vcnt = bfs(row_idx, col_idx, field, visited, row, col)

                o_cnt += _ocnt
                v_cnt += _vcnt

    print(o_cnt, v_cnt)

solution()