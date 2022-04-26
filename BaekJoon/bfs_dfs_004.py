
'''

 Backjoon _ exampels 2667

  " 단지번호붙이기"   by Jinwoo Lee


 < bfs / bfs 실 문제 적용 알고리즘 >


 1. 문제 정보에 따른 필드 구성

 2. 단지의 시작점이 여러곳이기 떄문에 2중 포문을 통해 bfs의 시작점 초기화 필요 

 3. 2중 포문으로 정해진 좌표 [ raw_idx, col_idx ] 에 대하여 bfs 실행 

 4. dfs 함수 구현

   * 좌표 이동( 대각선 제외) 임으로 dx, dy 설정 

   * 범위 제한, 값 제한(0이면 벽임 ) 설정

   * 방문 좌표는 visited에 저장, 추후 단지 별 주택 개수를 len(Visited)를 통해 return 

   * 이미 방문한 좌표에 대해서 0으로 삭제 ( 더 이상 필요가 없음 ) 

 
 

'''

def make_graph():

    n_size = int(input())

    temp_field = [ list(map(int, input()))  for _ in range(n_size)]

    return temp_field



def bfs(field, x, y ):

    # up down left right 
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = []
    visited = []

    queue.append([x,y])
    visited.append([x,y])
    field[x][y]=0

    while queue:

        _x, _y = queue.pop(0)

        for idx in range(4):

            nx = _x + dx[idx]
            ny = _y + dy[idx]

            if nx < 0 or ny < 0 or nx >= len(field) or ny >= len(field) : 
                continue

            if field[nx][ny] == 0 :
                continue

            if field[nx][ny] == 1:

                visited.append([nx,ny])

                queue.append([nx,ny])

                # delete 
                field[nx][ny]=0

        
    return len(visited)


field = make_graph()

result = []

for raw_idx in range(len(field)):

    for col_idx in range(len(field)):

        if field[raw_idx][col_idx] == 1:

            result.append( bfs(field, raw_idx, col_idx) )

print(len(result))

for value in sorted(result):

    print(value)

