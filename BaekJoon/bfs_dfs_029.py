

'''

 Backjoon _ exampels 17086

  "�Ʊ� ��� 2"   by Jinwoo Lee

  < algorithm >


  1.  �θ� ��ǥ [ _x, _y] �� ���� 8���� �̵� ������ �ڽ� ��ǥ ���� [ n_x, n_y ]


  2. �ʵ��� ���(0)�� ���� ���� bfs �����Ͽ� ���ʷ� ���(1)�� �������� ���� ĭ �� ã�� 

    => �θ� ��ǥ�� ���� �����Ͽ�, �ڽ� ��ǥ�� ���� 1�ϋ� bfs ���� �� ĭ�� return 

    =>  for raw_idx in range(raw):

            for col_idx in range(col):

               if field[raw_idx][col_idx] == 0 : 

                    bfs(raw_idx, col_idx, field, raw, col )


  3. �� �θ� ��ǥ �� ���� �Ÿ� �� ���� ū ���� return

 

'''


from collections import deque 

def bfs(x, y , field, raw, col):


    queue = deque( [ [x,y] ] )

    visited = [[False for _ in range(col)] for _ in range(raw)]
    score = [[0 for _ in range(col)] for _ in range(raw) ]
    visited[x][y] = True


    # move : left right up down 11 13 17 19
    dx = [-1, 1, 0, 0 , -1, 1, 1, -1]
    dy = [0, 0, 1, -1, -1, -1, 1, 1 ]


    while queue :

        _x, _y = queue.popleft()
        
        for idx in range(8):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]

            
            if n_x < 0 or n_y < 0 or n_x >= raw or n_y >= col :
                continue

            if not visited[n_x][n_y] and field[n_x][n_y] == 0 : 

                visited[n_x][n_y] = True

                queue.append([n_x,n_y])

                score[n_x][n_y] = score[_x][_y] + 1

            if not visited[n_x][n_y] and field[n_x][n_y] == 1:

                return score[_x][_y] + 1




def solution():
    
    raw, col = list(map(int , input().split()))

    field = [list(map(int, input().split())) for _ in range(raw)]

    
    ans = [] 

    for raw_idx in range(raw):

        for col_idx in range(col):

            if field[raw_idx][col_idx] == 0 :

                ans.append(bfs(raw_idx, col_idx, field, raw,col))


    return max(ans)


print( solution() )