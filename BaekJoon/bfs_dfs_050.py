

'''

 Backjoon _ exampels 9204

  "체스"   by Jinwoo Lee

  < algorithm >

  * bfs에서 이동 경로까지 구해야 하는 경우 

  1. 각 이동 경로를 저장할 path table 설정 

     path = path = [ [deque([[num2eng[i],j]]) for j in range(col+1) ] for i in range(row+1)] 선언


  2. 기존 문제들은 한칸씩만 이동했기 때문에 bfs 알고리즘만 적용 하면 됬지만, '체스'문제처럼 한번에 여러칸을 이동할 수 있는 경우는

     이동 가능한 거리 n을 곱해주는 2중 포문 구조를 취하면 최단 경로를 구할 수 있다.

     ( 시작 좌표로부터 4칸 떨어진 곳을 1칸씩 4번 이동하는 것보다, 4칸을 한번에 이동하는것이 먼저 도착하기 때문에 )

     drow = [-1,1, 0,  0]
     dcol = [0, 0, -1, 1]

     # 거리
     for n in rnage(1, len(field)+1):

       # 방향
       for idx in range(4):

         # 첫 방문인 경우만 
         if visited[n_row][n_col] == 0 :

            visited[n_row][n_col] = visited[_row][_col] + 1  # 경로의 길이 구하기

            path[n_row][n_col] = path[_row][_col]            # 최단 경로 구성 구하기 

 

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