
'''

 Backjoon _ exampels 14940

  "쉬운 최단거리"   by Jinwoo Lee

  < algorithm >

  1. 문제 조건 

     0 ( not available) 인데 못가면 : 0

     1 ( available) 인데 못가면 : -1 

     => 단순히 bfs만 하면 시작부터 못가는 땅(0인 부분) 은 0이다 라는 처리가 되지 않아서 AC 받지 못함


  * 이번 문제가 다량으로 틀렸던 이유는 출력의 형태가 [ 0,1,2,3,4,5 , ... ] 가 아닌 0 1 2 3 4 5 ..

    즉 print(score[idx]) 가 아니라, print( * score[idx]) 로 고쳤어야 했음

    => 문제를 제대로 체크할 것
 

'''




from collections import deque

def bfs(start_x, start_y, score, field, row, col):
    

    queue = deque([[start_x, start_y]])

    visited = [ [False for _ in range(col)] for _ in range(row) ]

    visited[start_x][start_y] = True

    score[start_x][start_y] = 0

    # move left right up down
    drow = [0, 0, -1, 1]
    dcol = [-1, 1, 0, 0]

    while queue :

        _x , _y = queue.popleft()

        for idx in range(4):

            n_x = _x + drow[idx]
            n_y = _y + dcol[idx]


            if n_x < 0 or n_y < 0 or n_x >= row or n_y >= col : continue

            if not visited[n_x][n_y] and field[n_x][n_y] == 1:

                queue.append([n_x,n_y])
                visited[n_x][n_y] = True

                score[n_x][n_y] = score[_x][_y] + 1



    return score


def solution():
    
    row, col = map(int, input().split())

    field = [ list(map(int, input().split())) for _ in range(row) ]

    score = [ [-1 for _ in range(col)] for _ in range(row) ]


    start_x, start_y = None, None

    for row_idx in range(row):

        for col_idx in range(col):

            if field[row_idx][col_idx] == 2 :

                start_x, start_y = row_idx, col_idx

            elif field[row_idx][col_idx] == 0 : 

                score[row_idx][col_idx] = 0 

    score = bfs(start_x, start_y, score, field, row, col)

    for idx in range(row):

        print(*score[idx])


solution()