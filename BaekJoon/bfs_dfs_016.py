
'''

 Backjoon _ exampels 14502

  "������"   by Jinwoo Lee

  < algorithm >

  1. �ٽ� �˰����� 3�� 

    a) N * M field���� 3���� ���� ����� ��� ����

    b) ���� �߰��� ������ new_field�� ���Ͽ� bfs 

    c) bfs ���� 0�� ������ ���� ���� ū ����� �������� ���� ���


  * ������� ���� ������ �ִ��� ���� ���븦 �����ϴ��� �� ���� ���� ������ ��� ���տ� ���� �Ǻ��ؾ� �Ѵ�.

    => combinations�� ���������,  �ش� library�� �����Ѵٸ�, �ٸ� ����� ����ؾ� �Ѵ� ( �� �κп� ���� ���� ������ �����ɸ� )



  * ���� field�� ���� ������ new_field�� �����ؾ� �ϱ� ������, copy.deepcopy()�� ���� ���� ���� ���

    => ���� ���縦 ���� ������ new_field ���� �������� �� ���� field�� ���� ���ϰ� ��



  * BFS

    => virus �� ���� ��ġ�� ���� virus_list�� �����Ͽ�, queue�� ���� ��ǥ�� ��� 



  * bfs ���� ��ǥ���� Ȱ���ؾ� �ϴ� ���, �ܼ� ����Ʈ���� 2���� �迭 ���°� �ð��� ���� �ȴ� .

    => '���ϻ���' �������� �� �� �ֵ���, ��ǥ���� ����ϴ� ��� 

        visited = [] �� ���� ��,  (new_x, new_y) �� �ش��ϴ� ��ǥ�� visited �� �ִ��� Ȯ���ϱ� ���� 

        [new_x, new_y] in visited �� ���� �Ǻ��ϸ� �ð� ���⵵�� O(N)�� �Ǿ������ ������ TLE�� �ɸ� Ȯ���� �ִ�.

        ���� vistied[new_x][new_y]=1 �� 2���� �迭 ���¸� ���� indexing�� ���� ���������ν� 

        �ð� ���⵵ O(1)�� �ǵ��� Ȱ���Ѵ� 


  ** �� ������ a)�� combinations �� ������� �ʰ� ������� ���� �ɷȰ�, �ᱹ �ۼ����� �Ӹ��� ����ϰ� ���صǴ� �ڵ尡 ������ �ʾ�

     library�� ����Ͽ��µ�, ���� �Ƿ��� ��� �ȴٸ� �̺κп� ���ؼ� �߰����� �ڵ屸���� ������ ���� �� ���� (2022.5.12 JHS,_LJW)
    
    
 

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