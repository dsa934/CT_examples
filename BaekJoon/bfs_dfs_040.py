



'''

 Backjoon _ exampels 21736

  "�峻��� ģ���� �ʿ��� "   by Jinwoo Lee

  < algorithm >

  1. �������� DFS/BFS ����

    => 4���� ���� ����� PASS

    1) ������ �Ѵ� ��� continue

    2) ���� ��� continue

    3) ù �湮 + ������̸� �̵�

    4) ù �湮 + ����̸� �̵� + res �� �߰� 
 

'''



def dfs(x, y , field, raw, col ):


    stack = [ [x,y] ] 

    visited = [ [False for _ in range(col)] for _ in range(raw) ]

    visited[x][y]= True
    
    res = 0

    # move left right up down
    dx = [-1, 1, 0 , 0]
    dy = [0 , 0, 1, -1 ]

    while stack :


        _x, _y = stack.pop()


        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]


            if n_x < 0 or n_y < 0 or n_x >= raw or n_y >= col : 
                continue

            if field[n_x][n_y] == 1 :

                continue
            
            if not visited[n_x][n_y] and field[n_x][n_y] == 'O':

                stack.append([n_x,n_y])
                visited[n_x][n_y] = True

            if not visited[n_x][n_y] and field[n_x][n_y] == 'P' :

                stack.append([n_x,n_y])
                visited[n_x][n_y] = True

                res +=1 
                


    return res if res != 0 else 'TT'









def solution():

    raw, col = map(int, input().split())

    field = [list(input()) for _ in range(raw)]
    
    
    for raw_idx in range(raw):

        for col_idx in range(col):


            if field[raw_idx][col_idx] == 'I':
                
                print( dfs(raw_idx, col_idx, field, raw, col ) )
                break


solution()
