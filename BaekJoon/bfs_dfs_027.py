
'''

 Backjoon _ exampels 13565

  "침투"   by Jinwoo Lee

  < algorithm >

  1. bfs 알고리즘 사용

    * outer side에 인접한 raw_idx = 0  , col_idx = 0 : col(입력값) 범위에서 0인 곳의 좌표만 bfs 실행

    * bfs 실행 후 innser side에 인접한 raw_idx = -1 , col_idx = 0 : col 에서 True가 되는 곳이 있으면 Yes else No

    * BFS를 좌표에 적용하는 경우 방문 노드를 좌표 형태로 형성 후, True / False 해주는 것이 시간복잡도 O(1)이라 요구 됨 


'''

from collections import deque 


def bfs(raw_idx, col_idx, field, visited, raw, col):
    
    queue = deque([[raw_idx, col_idx]])

    visited[raw_idx][col_idx] = True

    #     left, right , up, down
    dx = [ -1, 1, 0 , 0]
    dy = [ 0, 0, 1, -1 ]

    
    while queue :

        _x , _y = queue.popleft()

        
        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]


            if n_x < 0 or n_y < 0 or n_x >= raw or n_y >= col : 
                continue

            if field[n_x][n_y] == 1: 
                continue

            if not visited[n_x][n_y] and field[n_x][n_y] == 0 :

                queue.append([n_x,n_y])

                visited[n_x][n_y] = True
                

def solution():

    raw, col = list(map(int , input().split()))

    field = [ list(map(int, input())) for _ in range(raw) ]

    visited = [ [False for _ in range(col)] for _ in range(raw) ]

    
    for col_idx in range(col):

        if field[0][col_idx] == 0 :

            bfs(0, col_idx, field, visited, raw, col)

    ans = 'NO'

    
    for value in visited[-1]:
        
        if value :
            ans = 'YES'

    return ans

print( solution() ) 