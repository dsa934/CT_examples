

'''

 Backjoon _ exampels 1926

  "�׸�"   by Jinwoo Lee

  < algorithm >

  1. �⺻ dfs/bfs �˰��� ������ �ٸ��� ������ ���� ���� 2���� 


   * �湮 ��� ó���� ���� visited ���� ���� TLE �߻� 

   
     1. visited = [ [ x_pos, y_pos ] ]    

     2. visited = [ [False for _ in range(Col) ] for _ in range(raw)]  ( in dfs )

     3. visited = [ [False for _ in range(Col) ] for _ in range(raw)]  ( in main f )
 

     * 1�� ���, ��ǥ�� �����ϴ� ������� �ߴ���, ���� �������� �����ߴ� [n_x, n_y] not in visited ������ �뷫 O(N)�� �ð����⵵�� ���� ������ ���� �߻�

     * 2�� ���, dfs function �ȿ� visited�� �����ߴ���, tle �߻�

     * 3�� ��� ó��, �������� �湮 ��� Ȯ���� ���� visited table �� �����ؾ� TLE�� ���� �� ���� 

'''




def dfs(x_pos, y_pos , field, raw, col, visited):


    
    stack = [] 

    stack.append([x_pos, y_pos])
    visited[x_pos][y_pos] = True


    candidate = [[x_pos,y_pos]] 

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while stack :

        _x, _y = stack.pop()


        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]


            if n_x < 0 or n_y < 0 or n_x >= raw or n_y >= col :

                continue

            if field[n_x][n_y] == 0 :
                
                continue

            if field[n_x][n_y] == 1 and not visited[n_x][n_y] :

                stack.append([n_x,n_y])
                visited[n_x][n_y] = True
                
                field[n_x][n_y] = 0

                candidate.append([n_x,n_y])
                
    return len(candidate)



def solution():

    raw, col = list(map(int, input().split()))

    field = [list(map(int, input().split())) for _ in range(raw)]

    # global visited
    visited = [ [False for _ in range(col)] for _ in range(raw) ] 

    result = [] 

    for raw_idx in range(raw):

        for col_idx in range(col):
            
            if field[raw_idx][col_idx] != 0 :
                
                result.append( dfs(raw_idx, col_idx, field, raw,col, visited) )

    if len(result) == 0 :
        print(len(result))
        print(0)

    else:
        print( len(result))  
        print( max(result))

solution()