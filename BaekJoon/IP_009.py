

'''

 Backjoon _ exampels 1730

  "��ȭ"   by Jinwoo Lee

  < algorithm >


  1. garo, sero status table

     => orders ���� �̾Ƴ� ����� ���� U,D // L,R�� ���ϴ� ��� ������ ��ǥ�� �ش��ϴ� sero, garo status �� True�� ����


  2. ������ ��ǥ (cur_x, cur_y) ���� direction ��ŭ �̵� �� ���ο� ��ǥ (n_x, n_y)�� field ������ �Ѿ���� üũ 

     => garo, sero ǥ�Ⱑ ������ ��ǥ��, �̷���ǥ�� �ߺ����� ������ �ֱ� ����



  * ���� �õ����� bfs ������ ����ؼ� Ǯ�������� AC ���� ���� ����

   => U,D,L,R ���θ� �ϳ��� field_status�� ó�� �ߴµ� ���⼭ ������ �߻��Ѱ����� ������ 

   => ���� ������ �ش��ϴ� ��� ������ ������ ���������� ������ �Ǻ��ϴ°��� ���� ������ ���� ��
 
'''

from collections import deque

def bfs(boundary, garo, sero):

    orders = deque(list(input()))

    cur_x, cur_y = 0 , 0


    # move 
    directions = {'D':[1,0], 'U':[-1,0], 'L':[0,-1], 'R':[0,1]}


    while orders:

        way = orders.popleft()


        if cur_x + directions[way][0] < 0 or cur_y + directions[way][1] < 0 or cur_x + directions[way][0] >= boundary or cur_y + directions[way][1] >= boundary : continue

        n_x = cur_x + directions[way][0]

        n_y = cur_y + directions[way][1]

        if way == 'D' or way =='U' : 

            sero[cur_x][cur_y] = True
            sero[n_x][n_y] = True

        elif way == 'L' or way == 'R' : 

            garo[cur_x][cur_y] = True
            garo[n_x][n_y] = True

        cur_x, cur_y = n_x, n_y



def solution():
    
    boundary = int(input())

    field = [['.' for _ in range(boundary)] for _ in range(boundary)]

    garo = [[ False for _ in range(boundary) ] for _ in range(boundary) ] 
    sero = [[ False for _ in range(boundary) ] for _ in range(boundary) ] 


    bfs(boundary, garo, sero)


    for row_idx in range(boundary):

        for col_idx in range(boundary):

            if garo[row_idx][col_idx] and sero[row_idx][col_idx] : field[row_idx][col_idx] = '+'

            elif garo[row_idx][col_idx] : field[row_idx][col_idx] = '-'

            elif sero[row_idx][col_idx] : field[row_idx][col_idx] = '|'


    for idx in range(boundary):
        print(''.join(field[idx]))

solution()