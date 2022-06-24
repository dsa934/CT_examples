
'''

 Backjoon _ exampels 6146

  "신아를 만나러"   by Jinwoo Lee

  < algorithm >
 
   1. field 범위가 -500 <= x, y <= 500 임으로 

      0<= x,y <= 1000 범위로 환산하여 문제풀기 

   2. 방문 리스트, field는 1000+1 로 설정 

      -500 + 500 = 0

      500 + 500 = 1000 임으로  0과 1000이 포함되야 한다 

      따라서, 1000+1로 크기잡기


'''




from collections import deque

def bfs(s_x, s_y, field, visited, row, col, t_x, t_y):
    

    queue = deque([[s_x+500, s_y+500]])
    

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    while queue :

        _x, _y = queue.popleft()


        if _x == t_x+500 and _y == t_y+500 :
            break

        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]


            if n_x < 0 or n_y < 0 or n_x > row or n_y > col :
                continue

            if field[n_x][n_y] == 'M':
                continue

            if visited[n_x][n_y] == 0:
                
                queue.append([n_x,n_y])
                visited[n_x][n_y] = visited[_x][_y] + 1

    return visited[t_x+500][t_y+500]





def solution():
    
    t_y, t_x, puddle = map(int, input().split())


    field = [ ['.' for _ in range(1000+1)] for _ in range(1000+1)]
    
    visited = [ [0 for _ in range(1000+1)] for _ in range(1000+1)]


    for _ in range(puddle):

        col, row = map(int, input().split())

        field[row+500][col+500] = 'M'
    

    print ( bfs(0,0 , field, visited, 1000, 1000, t_x, t_y) )



solution()