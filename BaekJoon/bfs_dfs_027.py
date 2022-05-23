
'''

 Backjoon _ exampels 13565

  "ħ��"   by Jinwoo Lee

  < algorithm >

  1. bfs �˰��� ���

    * outer side�� ������ raw_idx = 0  , col_idx = 0 : col(�Է°�) �������� 0�� ���� ��ǥ�� bfs ����

    * bfs ���� �� innser side�� ������ raw_idx = -1 , col_idx = 0 : col ���� True�� �Ǵ� ���� ������ Yes else No

    * BFS�� ��ǥ�� �����ϴ� ��� �湮 ��带 ��ǥ ���·� ���� ��, True / False ���ִ� ���� �ð����⵵ O(1)�̶� �䱸 �� 


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