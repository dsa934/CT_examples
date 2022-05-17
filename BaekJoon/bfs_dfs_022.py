

'''

 Backjoon _ exampels 1926

  "그림"   by Jinwoo Lee

  < algorithm >

  1. 기본 dfs/bfs 알고리즘 문제와 다를게 없지만 주의 사항 2가지 


   * 방문 노드 처리를 위한 visited 선언에 따른 TLE 발생 

   
     1. visited = [ [ x_pos, y_pos ] ]    

     2. visited = [ [False for _ in range(Col) ] for _ in range(raw)]  ( in dfs )

     3. visited = [ [False for _ in range(Col) ] for _ in range(raw)]  ( in main f )
 

     * 1의 경우, 좌표를 저장하는 방식으로 했더니, 이전 문제에서 정리했던 [n_x, n_y] not in visited 문에서 대략 O(N)의 시간복잡도를 갖기 떄문에 문제 발생

     * 2의 경우, dfs function 안에 visited을 생성했더니, tle 발생

     * 3의 경우 처럼, 전역으로 방문 노드 확인을 위한 visited table 을 설정해야 TLE를 줄일 수 있음 

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