
'''

 Backjoon _ exampels 2206

  "벽 부수고 이동하기"   by Jinwoo Lee

  < algorithm >

  1. visited 를 3차원으로 구현하면,  아래의 두 가지 경우를 동시에 고려할 수 있다.

    a) 벽을 부수지 않고 진행하는 루트

    b) 벽을 부수면서 진행하는 루트 



    * a)  info[n_x][n_y] == 1  && _wall_count = 1 :                     # (n_x,n_y) 가 벽이고, 벽을 부수지 않았다면,

          visiteid[n_x][n_y][0] = visiteid[_x][_y][1] + 1                 벽을 부술 수 있는 기회는 1번이고,  (n_x, n_y) 는 벽을 부수고 방문한 좌표임으로 

          queue.append( [n_x, n_y, 0 ]  )                                 큐에 (n_x, n_y) 좌표를 추가하고, 방문노드에 (n_x, n_y) 좌표까지의 거리비용을 갱신 
          
                                                                           단, 더이상 벽을 부수지 못하기 떄문에, 벽을 부수지 못하는 visited[n_x][n_y][0] 에 값 추가 


                                                                           
    * b)  info[n_x][n_y] == 0  && visited[n_x][n_y][_wall_count] = 0 :  # (n_x,n_y) 가 벽이 아니고, 방문한적이 없다면,

          visiteid[n_x][n_y][_wall] = visiteid[_x][_y][_wall] + 1         해당 좌표 큐에 추가 및 방문 노드 설정 

          queue.append( [n_x, n_y, _wall ]  )                              
  


  2. BFS/DFS 알고리즘은 미로를 세워서 물을 부은것과 같다 

    => 벽에 대해 일일히 BFS를 적용한 이유가 ,  ' a)와 같이 하면 처음 만나는 벽만 부수지 않을까 ?' 라는 생각에서 그렇게 구현한 것인데,

      BFS / DFS 알고리즘에서 시작 좌표 (start_x, start_y) 를 기준으로 상,하,좌,우 로 뻗어나가는 경로(경우의 수)들은 제각기 '독립적'이다.

      아래로 향하는 경로에서 벽을 부순다고 해서,  좌,우,위쪽 방향으로 이동하는 경로들이 벽을 부수지 못하는 것이 아니다.

      각 루트들은 독립적이지만,  최단 경로를 갱신함에 있어 이전 좌표를 활용함으로 ( visited[n_x][n_y][_wall] = visited[_x][_y][_wall]+1) 

      visited[n_x][n_y][0] = visited[x][y][1] + 1  와 같이 3차원 배열을 통해,  현 위치 (n_x, n_y)에서 벽을 부쉈다면,

      그 다음 갱신 위치는 벽을 더이상 부술 수 없는 방문노드 vistied[n_x][n_y][0] 에 최단 루트 값을 저장해야 한다.


      이러한 각 방향의 독립성을 뒷받침 하기 위해, 

      기존에 2차원 배열로 visited를 활용하는 것과 달리, 3차원으로 구성하되, 3차원의 내용은 벽을 부쉇는가에 대한 yes/no 의 offset 역할을 할 수있는 [0][0] 을 추가해준다 .





  3. visited =  [ [ [0] *2  ]  for _ in range(col) ] for in range(raw)  ] 

    3차원 이상의 배열을 list 내포로 구현할 경우, 

    raw : 가장 밖에 선언, col : 두번쨰 선언 

    n : col 보다 안쪽에 선언 

    ex)  visited = [  [ [0] * 2 ] for _ in range(3) ] for in rnage(2) ] 

       [     
           [ [0], [0] ] , [ [0], [0] ], [ [0], [0] ]

           [ [0], [0] ] , [ [0], [0] ], [ [0], [0] ]
       
       
       ]





  * 기존의 '연구소' 문제와 다르게 모든 벽에 대해 BFS를 할 경우 TLE에 걸린다 ( '1개만' 지울 수 있다는 것이 Hint )

    => BFS의 시간 복잡도 O(NM) , N x M field를 모두 찾아야 함으로 

       벽돌의 최대 개수 n x m  임으로 ,  

       하나의 벽돌에 대해 bfs를 진행할 경우의 시간 복잡도는 O( (NM)^2 ) => TLE

 

'''

from collections import deque


def bfs(field, w, h):

    
    queue = deque()

    visited = [ [ [0] * 2 for _ in range(h) ] for _ in range(w) ]

    visited[0][0][1] = 1
    
    queue.append([0,0,1])

    # left right up down
    dx = [-1 , 1, 0, 0]
    dy = [0 , 0, -1, 1]
    
    while queue:

        _x, _y, _wall = queue.popleft()


        if _x == w -1 and _y == h-1 : 

            return visited[_x][_y][_wall]

        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]
            
            if n_x < 0 or n_y < 0 or n_x >= w or n_y >= h :
                continue

            if field[n_x][n_y] == 1 and _wall == 1:

                visited[n_x][n_y][0] = visited[_x][_y][1] + 1

                queue.append([n_x,n_y,0])

            elif field[n_x][n_y] == 0 and visited[n_x][n_y][_wall] == 0 :
                
                visited[n_x][n_y][_wall] = visited[_x][_y][_wall] + 1

                queue.append([n_x,n_y,_wall])
                
    return -1



def solution():
    
    w, h = list(map( int, input().split() ))

    field = [list(map(int, input())) for _ in range(w) ]
    
    return bfs(field,w,h)



print( solution() )

