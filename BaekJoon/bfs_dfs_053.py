
'''

 Backjoon _ exampels 14940

  "���� �ִܰŸ�"   by Jinwoo Lee

  < algorithm >

  1. ���� ���� 

     0 ( not available) �ε� ������ : 0

     1 ( available) �ε� ������ : -1 

     => �ܼ��� bfs�� �ϸ� ���ۺ��� ������ ��(0�� �κ�) �� 0�̴� ��� ó���� ���� �ʾƼ� AC ���� ����


  * �̹� ������ �ٷ����� Ʋ�ȴ� ������ ����� ���°� [ 0,1,2,3,4,5 , ... ] �� �ƴ� 0 1 2 3 4 5 ..

    �� print(score[idx]) �� �ƴ϶�, print( * score[idx]) �� ���ƾ�� ����

    => ������ ����� üũ�� ��
 

'''




from collections import deque

def bfs(start_x, start_y, score, field, row, col):
    

    queue = deque([[start_x, start_y]])

    visited = [ [False for _ in range(col)] for _ in range(row) ]

    visited[start_x][start_y] = True

    score[start_x][start_y] = 0

    # move left right up down
    drow = [0, 0, -1, 1]
    dcol = [-1, 1, 0, 0]

    while queue :

        _x , _y = queue.popleft()

        for idx in range(4):

            n_x = _x + drow[idx]
            n_y = _y + dcol[idx]


            if n_x < 0 or n_y < 0 or n_x >= row or n_y >= col : continue

            if not visited[n_x][n_y] and field[n_x][n_y] == 1:

                queue.append([n_x,n_y])
                visited[n_x][n_y] = True

                score[n_x][n_y] = score[_x][_y] + 1



    return score


def solution():
    
    row, col = map(int, input().split())

    field = [ list(map(int, input().split())) for _ in range(row) ]

    score = [ [-1 for _ in range(col)] for _ in range(row) ]


    start_x, start_y = None, None

    for row_idx in range(row):

        for col_idx in range(col):

            if field[row_idx][col_idx] == 2 :

                start_x, start_y = row_idx, col_idx

            elif field[row_idx][col_idx] == 0 : 

                score[row_idx][col_idx] = 0 

    score = bfs(start_x, start_y, score, field, row, col)

    for idx in range(row):

        print(*score[idx])


solution()