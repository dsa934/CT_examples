

'''

 Backjoon _ exampels 21938

  "����ó��"   by Jinwoo Lee

  < algorithm >
  
  1. R,G,B ���� ���ʴ�� �Է� �Ǳ� ������ score[col_idx : col_idx+3 ]  

     col_idx ~ col_idx+3 -> +2 ���� ó���ؼ� col_idx, col_idx+1 ������ �������� ������� ���� ���ϴ� �Ǽ� 

     slicing �� [start : end] �����ϸ� end �� ���ܵ��� ����ϱ� 


 

'''

from collections import deque 

def bfs(field, visited, x, y, row, col):
    

    queue = deque([[x,y]])

    visited[x][y] = True


    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    candidate = [] 

    while queue :

        _x , _y = queue.popleft()


        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]


            if n_x < 0 or n_y < 0 or n_x >= row or n_y >= col:
                continue

            if field[n_x][n_y] == 0:

                continue

            if not visited[n_x][n_y] :

                queue.append([n_x,n_y])
                visited[n_x][n_y]= True

                if field[n_x][n_y] == 1:

                    field[n_x][n_y] = 0
        

def solution():

    row , col = map(int, input().split())

    score = [ list(map(int, input().split())) for _ in range(row) ]
    

    threshold = int(input()) 

    field = [ [ 0 for _ in range(col)] for _ in range(row) ]


    for row_idx in range(row):

        for col_idx in range(0,col*3,3):

            
            if int(sum(score[row_idx][col_idx:col_idx+3])/3) >= threshold:

                field[row_idx][int(col_idx//3)] = 1

  
    cnt = 0 

    visited = [[False for _ in range(col)] for _ in range(row) ]

    for row_idx in range(row):

        for col_idx in range(col):

            if field[row_idx][col_idx] == 1:

                cnt += 1

                bfs(field, visited, row_idx, col_idx, row, col )



    print(cnt)


    

solution()