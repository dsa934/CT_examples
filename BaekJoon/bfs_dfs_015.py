
'''

 Backjoon _ exampels 10026

  "적록색약"   by Jinwoo Lee

  < algorithm >

  1. DFS / BFS 모두 가능

  2. 이 문제 풀떄 TLE에 걸렸다.

  * 방문 좌표를 저장하기 위한 visited의 형태에서 오는 차이 

   a) visited = []

   b) visited = [ [0] * num for _ in range(num) ] 

   
   a) 의 경우, 방문하지 않은 좌표 (n_x, n_y) 를 list에 추가하는 형태

   b) 의 경우, [x][y]에 대한 2차원 배열로, 방문시 indexing을 통해 0 -> 1 변환 


   b)의 경우 indexing 접근임으로 O(1) 인 반면, 

   a)의 경우는 list에 추가하고, 방문 여부를 검사할떄 in을 사용하였음으로 O(n) 이 된다.

   따라서 시간을 절약하기 위해서는 b) 방식인 2차원 배열 방식을 사용하는것이 옳다


'''

from collections import deque


def dfs(graph, area):
    
    visited = [[0] * area for _ in range(area)] 

    answer = 0 

    # left, right, up, down
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    
    for raw in range(area):
        
        for col in range(area):

            if not visited[raw][col] :

                queue = deque()

                answer +=1

                set_color= graph[raw][col]
                
                visited[raw][col] = 1

                queue.append( [raw,col] )
                

                while queue:

                    _x, _y = queue.popleft()
                    

                    for idx in range(4):

                        n_x = _x + dx[idx]
                        n_y = _y + dy[idx]

                        if n_x < 0 or n_y < 0 or n_x >= area or n_y >= area:
                            continue

                        if graph[n_x][n_y] != set_color:
                            continue

                        if visited[n_x][n_y]==0 and graph[n_x][n_y] == set_color:

                            visited[n_x][n_y]= 1
                            
                            queue.append([n_x,n_y])

    return answer




def solution():

    num = int(input())
    
    field =[ input()  for _ in range(num)]
    
    result = dfs(field, num)


    field = [ ['R' if idx == 'G' else idx for idx in raw ] for raw in field ]

    result_color = dfs(field, num)

    return result, result_color




result, result_color = solution()

print( result, result_color )