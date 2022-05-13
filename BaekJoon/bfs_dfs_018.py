
'''

 Backjoon _ exampels 2583

  "영역 구하기"   by Jinwoo Lee


  < algorithm >

  1. 2중 포문을 통해 필드를 돌며, 0인 부분에 bfs / dfs 알고리즘 실행

  2. 알고리즘 이후, 방문한 좌표는 area_cnt로 채워준다 ( 영역별 크기를 계산해야 하기 떄문에 )

  3. field에 area_cnt에 해당하는 좌표의 개수를 각각 카운팅 하여 출력 



 

'''

from collections import deque

def bfs(field, x_pos, y_pos,  raw, col, visited, area_cnt ):

    queue = deque()

    queue.append([x_pos, y_pos])

    visited[x_pos][y_pos] = 1

    field[x_pos][y_pos] = area_cnt

    #  left, right, up , down
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:

        _x, _y = queue.popleft()

        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]

            if n_x < 0 or n_y < 0 or n_x >= raw or n_y >= col :
                continue

            if field[n_x][n_y] == 0 and visited[n_x][n_y] == 0:

                field[n_x][n_y] = area_cnt

                queue.append([n_x,n_y])

                visited[n_x][n_y] = 1

    

def solution():

    raw, col, k = list(map(int, input().split()))

    field = [ [ 0 for _ in range(col) ] for _ in range(raw)]

    
    for _ in range(k):

        s_col, s_raw, e_col, e_raw  = list(map(int , input().split()))


        for raw_idx in range(s_raw, e_raw):

            for col_idx in range(s_col, e_col):
                
                field[raw_idx][col_idx] = 1

    area_cnt = 1

    candidate = [] 

    visited = [ [0 for _ in range(col)] for _ in range(raw) ]

    for raw_idx in range(raw):

        for col_idx in range(col):

            if field[raw_idx][col_idx] == 0 :

                area_cnt +=1

                candidate.append(area_cnt)

                bfs(field, raw_idx, col_idx, raw, col, visited, area_cnt)
                
                

    result = []

    
    for value in candidate :

        cnt = 0 


        for raw_idx in range(raw):

            for col_idx in range(col):

                if field[raw_idx][col_idx] == value :

                    cnt+=1


        result.append(cnt)

    print(len(result))
        
    for value in sorted(result):

        print(value, end=" ")
    

solution()