
'''

 Backjoon _ exampels 2178

  " 미로 찾기  "   by Jinwoo Lee


 < bfs / dfs 실 문제 적용 알고리즘 >

 1. 미로에서 최단경로를 찾는 방법은  [ 시작 지점 ] 으로 부터 연결된 여러갈래 길을 비교 하는 것 

    => BFS  ( 시작 지점에 연결된 각기 다른 경로는 모두 같은 level 임 ) 

 

 2. BFS는 queue를 이용하고, 큐에 넣고 뺴는것은 좌표,   좌표 이동은 4방위 이동 ( 대각선으로 가지는 않음 ) 

    2  3  X
    3  z  y           
  
   -> 이전 위치(x,y) 까지의 경로  + 1 하는 방식으로 계산 가능 

    

 3. 처음에 헷깔렸던 내용  ( 0 : 벽 , 1 : 이동가능)

  1 1 1 1 1   * (1,1) => (5,5) 이동에는 2가지 루트가 존재 함 
  1 0 1 0 1
  1 0 1 0 1     BFS가 queue를 이용하여 모든 경로를 탐색하는건 알겠는데 이 두가지 루트중에 어느 쪽이 더 나은지는 코딩으로 어떻게 구현 ?
  1 0 1 0 1
  1 1 1 0 1     => 2가지 루트가 공통적으로 거쳐가는 부분은 (0,2) , 그러나 A,B 각각 2개의 루트에 대해서  (A가 더빠르다고 가정) 
   
                   A 루트가 이미 (0,2)를 1이 아닌 다른수로 변화 시켰기 떄문에 B가 (0,2)를 도착했을떄의 숫자 비교는 필요가 없음 

                   왜냐 ?  "최단 루트'를 구하는 문제이기 떄문


                  ∴ '처음 방문했을 경우' (이문제에서는 miro[nx][ny] == 1 ) 만 최단 거리를 반환하면 된다 



'''


def make_field():

    raw, col = list(map(int, input().split()))

    field = [list(map(int, input())) for _ in range(raw)]

    return field, raw, col



def bfs(miro, x,y,  raw, col ):

    queue = []

    # up, down, left, right
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue.append([x,y])

    while queue:

        x_pos, y_pos = queue.pop(0)

        # 4방위 이동
        for idx in range(4):

            nx = x_pos + dx[idx]
            ny = y_pos + dy[idx]

            # range check
            if nx < 0 or ny < 0 or nx >= raw or ny >= col :
                continue

            if miro[nx][ny] == 0 : 
                continue

            # 가장 처음 방문하는 경우만 최단거리 갱신 
            if miro[nx][ny] == 1:

                miro[nx][ny] = miro[x_pos][y_pos] + 1

                queue.append([nx,ny])

        
    #print("===========")
    #print(miro)
    return miro[raw-1][col-1]



miro, raw, col = make_field()


result = bfs(miro, 0,0, raw, col)

print(result)