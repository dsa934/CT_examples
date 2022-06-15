
'''

 Backjoon _ exampels 3187

  "양치기 꿍 "   by Jinwoo Lee

  < algorithm >

  1. 필드 내에서 특정 포인트( 늑대, 양)일떄 bfs를 취하는 문제의 경우 

     늑대, 양의 경우로 각각 나눠서 bfs를 하지 말고

     bfs 진입 시점을 통일 해서 처리하는 것이 오류를 방지할 수 있는 확률이 조금 더 높은듯 하다



  * 통과 판정을 받은 해당 코드도 첫 시도의 코드와 다른 의미가 없는데 통과 되는 것을 보면 

    오히려 case by case로 세세하게 나누는것이 문제가 생길 수도 있다 

    => 최대한 간결한 코딩 
 

'''


from collections import deque


def bfs(field, visited, x, y, row, col):
    
    queue = deque([[x,y]])

    visited[x][y] = True


    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    v_list, k_list  = [], [] 

    if field[x][y] == 'v' : v_list.append([x,y])
    else : k_list.append([x,y])
    

    while queue :

        _x, _y = queue.popleft()
        
        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]


            if n_x < 0 or n_y < 0 or n_x >= row or n_y >= col:
                continue

            if field[n_x][n_y] == '#':
                continue

            if not visited[n_x][n_y] :

                queue.append([n_x,n_y])
                visited[n_x][n_y] = True

                if field[n_x][n_y] =='v' :   v_list.append([n_x,n_y])

                elif field[n_x][n_y] == 'k' : k_list.append([n_x,n_y])


    v_cnt, k_cnt = 0, 0 

    if len(v_list) >= len(k_list): v_cnt = len(v_list)
    
    else : k_cnt = len(k_list)
        

    candidate = []
    candidate.extend(k_list)
    candidate.extend(v_list)

    for value in candidate:

        x_val, y_val = value 

        field[x_val][y_val] = '.'
    

    return v_cnt, k_cnt



def solution():

    row, col = map(int ,input().split())
    
    field = [list(input()) for _ in range(row)]
    
    visited = [[False for _ in range(col)] for _ in range(row) ]

    v_ans, k_ans = 0 , 0

    for row_idx in range(row):

        for col_idx in range(col):

            if field[row_idx][col_idx] == 'v' or field[row_idx][col_idx] == 'k':

                v, k = bfs(field, visited, row_idx, col_idx, row, col)

                v_ans += v
                k_ans += k


    print(k_ans, v_ans)


solution()