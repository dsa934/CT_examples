
'''

 Backjoon _ exampels 15558

  " 점프 게임 "   by Jinwoo Lee

  < algorithm >

  1. BFS / DFS 문제의 난이도가 높아질 수록 '깍는 것'을 잘해야 한다,

    => 조건에 맞게 디테일 하게 설계 하는 것을의미 


  2. visited table 

    => 얼핏 보면 방문 노드가 필요 없어 보이지만,  이동 규칙은 +1, -1 , +k 임으로 이동량이 다르다

       따라서 +k 가 +1, -1 보다 먼저 도착할 가능성이 높기 떄문에 방문 노드 체크가 요구 된다


  3. time table 

    => 시작 좌표로 부터 각각의 방향으로 '동시에' 진행 후, 조건에 맞는 좌표들을 queue 에 넣는 방식이라서 

       단순히 queue 에서 pop 했을떄 시간 카운트를 증가 시키는 것이 아니라 

       time[n_x][n_y] = time[_x][_y] + 1 과 같이  각 좌표들의 ([ n_x, n_y] ) 부모 좌표 ([_x, _y])  의 시간을 기준으로 고려해야 한다 


  4. 탈출 조건

     => 조건을 만족하지 못하고 while 문을 탈출하면 게임 진행 불가, 조건 만족시 게임 진행 가능의 설계 구조

        게임 진행 가능 조건은 문제에서 주어지는 배열의 개수(num)를 넘을 경우 게임 진행 판정을 받게 되는데

        index 가 0부터 시작하기 때문에 

        종료 조건은  _y > num 이 아니라 ,  _y >= num 이 되어야 한다  ( 이거 떄문에 10시간 넘게 걸림 )




  ∴ 이렇듯 bfs/dfs 골드 수준의 문제에서는 조건을 디테일하게 깎는 부분들이 많이 요구 되기 떄문에 주의가 필요하다

'''



from collections import deque


def bfs( start_x, start_y, field, num, k ):

    queue = deque([[start_x, start_y]])

    visited = [ [ False for _ in range(num)] + [False]* k  for _ in range(2) ]

    visited[start_x][start_y] = True


    time = [ [ 0 for _ in range(num)] + [0] *k  for _ in range(2) ]

    #move front, back, jump
    drow = [1, -1, 0, 0]
    dcol = [k, k, 1,-1]
    

    while queue:

        _x , _y = queue.popleft()

        if _y >= num :
            print(1)
            return 0

        for idx in range(4):

            n_x = _x + drow[idx]
            n_y = _y + dcol[idx]


            if n_x < 0 or n_y < 0 or n_x >= 2 or n_y <= time[_x][_y] : continue

            if field[n_x][n_y] == 0 : continue

            
            if not visited[n_x][n_y] :
                
                queue.append([n_x, n_y])
                visited[n_x][n_y] = True
                time[n_x][n_y] = time[_x][_y] + 1

                #print("chk n_x, n_y", n_x, n_y , "_x, _y", _x, _y , "queue", queue, "time", time[n_x][n_y])


    print(0)





def solution():
    
    num , k = list(map(int , input().split()))

    field = [ list(map(int , input())) + [1]* k for _ in range(2) ]

   
    bfs(0, 0, field, num, k )


solution()