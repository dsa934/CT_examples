
'''

 Backjoon _ exampels 1303

  " 전쟁 - 전투 "   by Jinwoo Lee

  < algorithm >

   1. 각 W,B 위치에서 BFS 실행 


   2. 주의할 사항 2가지 


   * 문자열(string)은 요소 변환 불가능

     string = 'temp' , string[0] = 'K'  => error 

     문자열(string)은 불변(immutable) 요소 임으로 indexing 을 통한 내용 변환이 불가능 하기 떄문에,

     string = list('temp') 와 같이 문자열 => 리스트로 변환 해야지만, index를 통한 요소 변환이 가능하다

     example)

     WWWWWWW       =>        field = [ input() for _ in range(raw) ]  => 문자열 취급으로 요소 변경 불가능
     BBBBBBB  
     CCCCCC                  field = [ list(input() ) for _ in range(raw) ]  => 문자열을 list로 변환, 요소 접근 가능 





   * (number) ^ 2 :  제곱 연산(x), 비트 연산(XOR : 다르면 1, 같으면 0 )

     4 ^ 2 = >                 100 
                (xor 연산)      10  
                ------------------
                               110  = 6 

     4 ** 2 = 16 ( 이게 제곱 연산)

 

'''

from collections import deque

def bfs(info, s_x, s_y, raw, col):


    visited = [ [s_x,s_y] ]

    queue = deque()

    queue.append([s_x,s_y])


    # left right up down
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    while queue :

        _x, _y = queue.popleft()


        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]


            if n_x < 0 or n_y < 0 or n_x >= raw or n_y >= col :

                continue

            if info[n_x][n_y] == info[s_x][s_y] and [n_x, n_y] not in visited :

                visited.append([n_x,n_y])

                queue.append([n_x,n_y])

                info[n_x][n_y] = 'K'

    # visited ^2  : bit operator            
    return len(visited)**2






def solution():

    col, raw = list(map(int ,input().split()))

    # string -> list
    field = [list(input()) for _ in range(raw)]

    w_visited, b_visited = [], [] 

    result_w, result_b = 0, 0

    for raw_idx in range(raw):

        for col_idx in range(col):

            if field[raw_idx][col_idx] == 'W' :
                
                result_w += bfs(field, raw_idx, col_idx, raw, col)
                

            elif field[raw_idx][col_idx] == 'B' :

                result_b += bfs(field, raw_idx, col_idx, raw, col)
    

    print(result_w, result_b)


solution()