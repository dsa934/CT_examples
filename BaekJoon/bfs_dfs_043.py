
'''

 Backjoon _ exampels 3187

  "��ġ�� �� "   by Jinwoo Lee

  < algorithm >

  1. �ʵ� ������ Ư�� ����Ʈ( ����, ��)�ϋ� bfs�� ���ϴ� ������ ��� 

     ����, ���� ���� ���� ������ bfs�� ���� ����

     bfs ���� ������ ���� �ؼ� ó���ϴ� ���� ������ ������ �� �ִ� Ȯ���� ���� �� ������ �ϴ�



  * ��� ������ ���� �ش� �ڵ嵵 ù �õ��� �ڵ�� �ٸ� �ǹ̰� ���µ� ��� �Ǵ� ���� ���� 

    ������ case by case�� �����ϰ� �����°��� ������ ���� ���� �ִ� 

    => �ִ��� ������ �ڵ� 
 

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