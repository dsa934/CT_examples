

'''

 Backjoon _ exampels 9204

  "ü��"   by Jinwoo Lee

  < algorithm >

  * bfs���� �̵� ��α��� ���ؾ� �ϴ� ��� 

  1. �� �̵� ��θ� ������ path table ���� 

     path = path = [ [deque([[num2eng[i],j]]) for j in range(col+1) ] for i in range(row+1)] ����


  2. ���� �������� ��ĭ���� �̵��߱� ������ bfs �˰��� ���� �ϸ� ������, 'ü��'����ó�� �ѹ��� ����ĭ�� �̵��� �� �ִ� ����

     �̵� ������ �Ÿ� n�� �����ִ� 2�� ���� ������ ���ϸ� �ִ� ��θ� ���� �� �ִ�.

     ( ���� ��ǥ�κ��� 4ĭ ������ ���� 1ĭ�� 4�� �̵��ϴ� �ͺ���, 4ĭ�� �ѹ��� �̵��ϴ°��� ���� �����ϱ� ������ )

     drow = [-1,1, 0,  0]
     dcol = [0, 0, -1, 1]

     # �Ÿ�
     for n in rnage(1, len(field)+1):

       # ����
       for idx in range(4):

         # ù �湮�� ��츸 
         if visited[n_row][n_col] == 0 :

            visited[n_row][n_col] = visited[_row][_col] + 1  # ����� ���� ���ϱ�

            path[n_row][n_col] = path[_row][_col]            # �ִ� ��� ���� ���ϱ� 

 

'''

from collections import deque


def bfs(start_x, start_y, target_x, target_y, num2eng, eng2num, row, col ):

    answer = []

    if start_x == target_x and start_y == target_y : 

        answer = [ 0, num2eng[start_x], start_y]

        print(*answer)

        return 0

    else:

        queue = deque([[start_x, start_y]])

        visited = [ [ 0 for _ in range(col+1)] for _ in range(row+1) ]     

        path = [ [deque([[num2eng[i],j]]) for j in range(col+1) ] for i in range(row+1)]

        # move  11  13   17   19
        drow = [-1, -1 , 1, 1]
        dcol = [-1, 1, 1, -1]


        while queue :

            _row, _col = queue.popleft()


            for n in range(1,8+1):

                for idx in range(4):

                    n_row = _row + drow[idx]*n
                    n_col = _col + dcol[idx]*n

                    if n_row <= 0 or n_col <= 0 or n_row > row or n_col > col : continue

                    if visited[n_row][n_col] == 0 :

                        queue.append([n_row, n_col])

                        visited[n_row][n_col] = visited[_row][_col] +1

                        path[n_row][n_col].extend(path[_row][_col])


    # add start_pos in path

    #path[target_x][target_y].append([start_x, start_y])

    answer = [ visited[target_x][target_y] ]



    while path[target_x][target_y]:

        _x, _y = path[target_x][target_y].pop()

        answer.extend([_x ,_y])
        
    
 
    print(*answer)

    return 0

 

def make_field(row, col):

    field = [ ['w' for _ in range(row+1) ] for _ in range(col+1)  ]

    for row_idx in range(2,row+1):

        if field[row_idx-1][1] =='w': field[row_idx][1] ='b'

    for row_idx in range(1, row+1):

        for col_idx in range(2, col+1):

            if field[row_idx][col_idx-1] == 'w' : field[row_idx][col_idx]='b'


    return field

 

def solution():

    num = int(input())
    row, col = 8,8 

    eng2num = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
    num2eng = {0:0,1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H'}


    field = make_field(row, col)


    for _ in range(num):


        s_x, s_y, e_x, e_y = list(input().split())

 

        if field[eng2num[s_x]][int(s_y)] != field[eng2num[e_x]][int(e_y)] : print('Impossible')


        else:

            bfs(eng2num[s_x],int(s_y),eng2num[e_x],int(e_y), num2eng, eng2num, row, col) 



solution()