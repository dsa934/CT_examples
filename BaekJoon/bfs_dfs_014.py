

'''

 Backjoon _ exampels 4963

  "섬의 개수"   by Jinwoo Lee

  < algorithm >

  1. 각 좌표(x,y)에 대하여 방문한적이 없는 경우 (not visited) bfs를 실행한다

  
  2. bfs 이후 visited 에 담긴 좌표에 대해서는 0으로 변환 

    * 2중 포문에서 중복으로 bfs 알고리즘을 적용하는 것을 방지

    * 그래프의 형태가 아닌, 배열의 형태로 정보가 전달됨으로, 중복 방지를 위해 0으로 변환해야함 



  3. 1에서 bfs를 실행할떄마다 result +=1 하여 섬의 개수 세기 



  * 처음에 답이 달랐던 이유는, 이 문제에서는 대각이동(diagonal) 요소도 포함하기 때문


  * 이 문제를 그래프의 형태로 풀면, 0으로 변환하는 과정이 생략될 수 있어 좋을것 같은데 추후 고민해보기 
 

'''

from collections import deque

def bfs(w, h):

    field = [list(map(int,input().split())) for _ in range(h)]
    

    visited = []

    queue = deque()

    result = 0


    #    left, right, up, down. diagonal(11) , diagonal(13), diagonal(17), diagonal(19)
    dx = [-1, 1, 0 , 0, -1, 1, 1, -1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]


    for raw in range(h):

        for col in range(w):

            if field[raw][col] == 1 and [raw,col] not in visited:

                queue.append([raw,col])
                visited.append([raw,col])
                result +=1
                while queue:

                    _x , _y = queue.popleft()

                    for idx in range(8):

                        n_x = _x + dx[idx]
                        n_y = _y + dy[idx]

                        if n_x < 0 or n_y < 0 or n_x >= h or n_y >= w :

                            continue

                        if field[n_x][n_y] == 0:
                            continue

                        else:

                            if [n_x, n_y] not in visited:

                                queue.append([n_x,n_y])

                                field[n_x][n_y]= 0

                                visited.append([n_x, n_y])



    return result





def solution():


    while True:

        w, h = list(map(int,input().split()))

        if w ==0 and h == 0 : break

        print ( bfs (w,h ) )




solution()