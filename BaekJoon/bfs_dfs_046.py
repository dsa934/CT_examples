
'''

 Backjoon _ exampels 1743

  "���Ĺ� ���ϱ�"   by Jinwoo Lee

  < algorithm >

  * bfs�� �̿��Ͽ� �ʵ� �� ��ֹ�('#")�� ���� �� ������ Ǯ ��� 

  1. ��ֹ��� ���� ��ǥ ����

  2. ��ֹ��� ���� ��ǥ��� ���� bfs ����

     1). bfs ���� �� ���� ��ǥ�� ����� ��ҷ� ��ȯ ( '#" -> '.' )

     2). ���� ��ǥ�� ������ �κ��� ��� ���� ��ֹ��̶�� ����� ��ҷ� ��ȯ 

     3). ���� ��ǥ�� ���� ���� ��� continue

     4). ���� ��ǥ�� ���� ��ǥ�� ����� ����� ��� continue

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