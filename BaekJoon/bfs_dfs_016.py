
'''

 Backjoon _ exampels 14502

  "연구소"   by Jinwoo Lee

  < algorithm >

  1. 핵심 알고리즘은 3개 

    a) N * M field에서 3개의 벽을 세우는 모든 조합

    b) 벽이 추가로 설립된 new_field에 대하여 bfs 

    c) bfs 이후 0인 지역의 수가 가장 큰 경우의 안전지역 범위 계산


  * 어느곳에 벽을 세워야 최대의 안전 지대를 형성하는지 알 수가 없기 떄문에 모든 조합에 대해 판별해야 한다.

    => combinations을 사용했으나,  해당 library를 금지한다면, 다른 방법을 고려해야 한다 ( 이 부분에 대한 생각 떄문에 오래걸림 )



  * 최초 field에 벽을 세워서 new_field를 형성해야 하기 떄문에, copy.deepcopy()를 통한 깊은 복사 사용

    => 깊은 복사를 하지 않으면 new_field 값을 변경했을 때 최초 field가 같이 변하게 됨



  * BFS

    => virus 의 시작 위치를 담은 virus_list를 구현하여, queue에 시작 좌표로 사용 



  * bfs 에서 좌표값을 활용해야 하는 경우, 단순 리스트보다 2차원 배열 형태가 시간이 단축 된다 .

    => '적록색맹' 문제에서 알 수 있듯이, 좌표값을 사용하는 경우 

        visited = [] 로 구현 시,  (new_x, new_y) 에 해당하는 좌표가 visited 에 있는지 확인하기 위해 

        [new_x, new_y] in visited 와 같이 판별하면 시간 복잡도가 O(N)이 되어버리기 떄문에 TLE에 걸릴 확률이 있다.

        따라서 vistied[new_x][new_y]=1 의 2차원 배열 형태를 통해 indexing을 통해 접근함으로써 

        시간 복잡도 O(1)이 되도록 활용한다 


  ** 이 문제는 a)를 combinations 을 사용하지 않고 만드려다 오래 걸렸고, 결국 작성자의 머리로 깔끔하게 이해되는 코드가 나오지 않아

     library를 사용하였는데, 추후 실력이 향상 된다면 이부분에 대해서 추가적인 코드구현이 있으면 좋을 것 같다 (2022.5.12 JHS,_LJW)
    
    
 

'''

import copy

from itertools import combinations

from collections import deque


def find_virus(field, width, height):

    virus = []


    for raw in range(width):

        for col in range(height):

            if field[raw][col] == 2 :

                virus.append([raw,col])


    return virus

def find_wall_space(field, width, height):

    wall = []


    for raw in range(width):

        for col in range(height):

            if field[raw][col] == 0 : 

                wall.append([raw,col])


    wall_combi = list( combinations(wall, 3) )
    
    return wall_combi




def setup_wall_and_bfs(field, width, height, wall_list, virus_list):

    # set wall
    for wall_value in wall_list:
        
        w_x, w_y = wall_value

        field[w_x][w_y] = 1


    # chk bfs

    queue = deque()

    visited = [ [0 for _ in range( height) ] for _ in range(width) ]

    #   left, right, up ,down
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue.extend(virus_list)

    for value in virus_list:

        v_x, v_y = value

        visited[v_x][v_y] = 1



    while queue:

        _x, _y = queue.popleft()

        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]


            if n_x < 0 or n_y < 0 or n_x >= width or n_y >= height :

                continue

            if field[n_x][n_y] == 1 : 

                continue

            if field[n_x][n_y] == 0 and visited[n_x][n_y] == 0 :

                visited[n_x][n_y] = 1
                field[n_x][n_y] = 2
                queue.append([n_x,n_y])


    num_safe = 0

    for raw_idx in range(width):

        for col_idx in range(height):

            if field[raw_idx][col_idx] == 0 :

                num_safe +=1


    return num_safe


def solution():

    result = 0

    w, h = list(map(int, input().split()))

    field = [list(map(int, input().split())) for _ in range(w) ]

    wall_list = find_wall_space(field, w, h)

    virus_list = find_virus(field,w,h)

    for value in wall_list:

        new_field = copy.deepcopy(field)
        
        answer =  setup_wall_and_bfs(new_field, w, h, value, virus_list)

        if answer > result : result = answer

    return result 

print( solution() )