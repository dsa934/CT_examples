
'''

 Backjoon _ exampels 13903

  "출근"   by Jinwoo Lee

  < algorithm >

  * 시작 좌표들을 queue에 넣고, bfs 실행


  ** 구현시 주의할 몇가지


  1) 보통의 bfs와 달리, 시작 좌표가 여러개 이기 떄문에 deque에 여러개의 데이터를 넣어야 함

     start_point = [시작 좌표들 ],  queue = deque( start_point )

     => 큐에 1개의 데이터 or 좌표를 넣을때의 형식은 deque([좌표]) 이지만, 

        이미 여러개의 요소를 포함한 list 형태의 데이터를 큐에 넣는 것이기 때문에 []가 생략됨

        => 네이버 CT 3번 문제에서 이 부분이 문제가 생겨서 코딩을 완성하지 못했으니 참고하기


  2) visited ,score 따로 활용하기

    => 문제가 쉬울 경우 visited 을 0으로 초기화 하여, +1 씩 증가시키면서 최단 경로값을 구할 수 있지만

       문제가 다소 복잡한 경우, 경로값, 방문여부를 따로 판단하는 것이 알 수 없는 오류에서 벗어날 확률이 높다.



  2) 간단하지만 AC를 한번에 받지 못한 이유 

   => answer = bfs() 

      if len(answer) == 0 : return -1 

      위와 같은 형태로 출근 불가능의 경우 -1, 가능의 경우 최소값을 출력하도록 설계 하였는데

      1 <= row <= 1000 의 범위를 가지고 있기 떄문에 1일 경우 문제가 생긴다


   ∴ 여러개의 시작 좌표로 bfs를 설계 하더라도, 큐에 시작 좌표를 모두 옮겨놓고 시작하면 각 시작 좌표에서 동시에 출발하는 것으로 해석할 수 있다.

      순서를 따지면 각 시작 좌표들이 동시에 처리되지 않는 것처럼 보이지만,  시작좌표 A,B에서 동일한 이동 규칙에 따라 이동한다면, 

      시작 좌표 A,B,C, .. 에서 각각 퍼져나가는 형태의 코딩이 되는것이다.

      그렇기 때문에,

      _x, _y = queue.popleft()

      if _X == row-1 :
        print(score[_x][_y])
        return 0

      위와 같이 큐에서 뽑아낸 값이 마지막 행에 도달했다면 그 값은 row에 도달한 모든 값들 중에 최소가 됨을 알 수 있다.


'''



from collections import deque 

def bfs(start_point, row, col, field, drow, dcol, n_rule):
    
    queue = deque(start_point)

    visited = [ [ False for _ in range(col)] for _ in range(row) ]

    for value in start_point:

        visited[value[0]][value[1]] = True


    score = [ [ 0 for _ in range(col)] for _ in range(row) ]



    while queue :

        _x, _y = queue.popleft()

        
        if _x == row-1 :

            print(score[_x][_y])

            return 0
        
        for idx in range(n_rule):

            n_x = _x + drow[idx]
            n_y = _y + dcol[idx]

            if n_x < 0 or n_y < 0 or n_x >= row or n_y >= col : continue

            if not visited[n_x][n_y] and field[n_x][n_y] ==1 :

                queue.append([n_x,n_y] )
                visited[n_x][n_y] = True
                score[n_x][n_y] = score[_x][_y] + 1 


    print(-1)




def solution():
    
    row, col = map(int, input().split())

    field = [list(map(int, input().split())) for _ in range(row) ]

    n_rule = int(input())

    drow = []
    dcol = []

    for _ in range(n_rule):
        
        r, c = map(int, input().split())

        drow.append(r)
        dcol.append(c)


    start_point = [] 

    for col_idx in range(col):

        if field[0][col_idx] == 1:

            start_point.append([0, col_idx])


    bfs(start_point, row, col, field, drow, dcol, n_rule)


solution()