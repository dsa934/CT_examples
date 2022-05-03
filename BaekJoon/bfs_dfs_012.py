
'''

 Backjoon _ exampels 7562

  "����Ʈ�� �̵�"   by Jinwoo Lee

  < algorithm >
 
  1. visited �ʿ� ����,  area x area ũ���� ü���� ���� ( ��� 0 �ʱ�ȭ )

  2. ���� ��ġ = ���� ��ġ + 1���� visited ��� �̿� 

  3. ����Ʈ�� �̵� ������ 8�밢 ���������� ��ġ ���� 

    * ù �õ����� 8�� ���� ��ǥ ������ ���� 16 % Ʋ��


'''

from collections import deque


def bfs(field, start_x, start_y, desti_x, desti_y, area):


    if start_x == desti_x and start_y == desti_y :

        return 0
    
    
    # move
    #    10,  11, 1  ,2,  4, 5, 7, 8    
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1,  2,  2, 1, -1, -2]


    queue = deque()
    
    queue.append([start_x,start_y])

    while queue:

        _x , _y = queue.popleft()
        
        for idx in range(len(dx)):

            n_x = _x + dx[idx]

            n_y = _y + dy[idx]


            if n_x < 0 or n_y < 0 or n_x >= area or n_y >= area : 
                continue

            if field[n_x][n_y] == 0 :
                
                field[n_x][n_y] = field[_x][_y] + 1

                queue.append([n_x,n_y])

    return field[desti_x][desti_y]



def move_knight():

    area = int(input())

    s_x, s_y = list(map(int, input().split()))

    d_x, d_y = list(map(int, input().split()))

    info_field = [ [0 for _ in range(area)] for _ in range(area)]
    

    print( bfs(info_field, s_x, s_y, d_x, d_y, area) )


num_test = int(input())

for _ in range(num_test):

    move_knight()