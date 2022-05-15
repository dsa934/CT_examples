
'''

 Backjoon _ exampels 1303

  " ���� - ���� "   by Jinwoo Lee

  < algorithm >

   1. �� W,B ��ġ���� BFS ���� 


   2. ������ ���� 2���� 


   * ���ڿ�(string)�� ��� ��ȯ �Ұ���

     string = 'temp' , string[0] = 'K'  => error 

     ���ڿ�(string)�� �Һ�(immutable) ��� ������ indexing �� ���� ���� ��ȯ�� �Ұ��� �ϱ� ������,

     string = list('temp') �� ���� ���ڿ� => ����Ʈ�� ��ȯ �ؾ�����, index�� ���� ��� ��ȯ�� �����ϴ�

     example)

     WWWWWWW       =>        field = [ input() for _ in range(raw) ]  => ���ڿ� ������� ��� ���� �Ұ���
     BBBBBBB  
     CCCCCC                  field = [ list(input() ) for _ in range(raw) ]  => ���ڿ��� list�� ��ȯ, ��� ���� ���� 





   * (number) ^ 2 :  ���� ����(x), ��Ʈ ����(XOR : �ٸ��� 1, ������ 0 )

     4 ^ 2 = >                 100 
                (xor ����)      10  
                ------------------
                               110  = 6 

     4 ** 2 = 16 ( �̰� ���� ����)

 

'''

from collections import deque

def bfs(info, s_x, s_y, raw, col):


    visited = [ [s_x,s_y] ]

    queue = deque()

    queue.append([s_x,s_y])


    # left right up down
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    while queue :

        _x, _y = queue.popleft()


        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]


            if n_x < 0 or n_y < 0 or n_x >= raw or n_y >= col :

                continue

            if info[n_x][n_y] == info[s_x][s_y] and [n_x, n_y] not in visited :

                visited.append([n_x,n_y])

                queue.append([n_x,n_y])

                info[n_x][n_y] = 'K'

    # visited ^2  : bit operator            
    return len(visited)**2






def solution():

    col, raw = list(map(int ,input().split()))

    # string -> list
    field = [list(input()) for _ in range(raw)]

    w_visited, b_visited = [], [] 

    result_w, result_b = 0, 0

    for raw_idx in range(raw):

        for col_idx in range(col):

            if field[raw_idx][col_idx] == 'W' :
                
                result_w += bfs(field, raw_idx, col_idx, raw, col)
                

            elif field[raw_idx][col_idx] == 'B' :

                result_b += bfs(field, raw_idx, col_idx, raw, col)
    

    print(result_w, result_b)


solution()