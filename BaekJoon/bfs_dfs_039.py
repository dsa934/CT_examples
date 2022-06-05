

'''

 Backjoon _ exampels 11123

  "양 한마리.. 양 두마리"   by Jinwoo Lee


  < algorithm >

  1. field 안에 양 무리가 몇무리나 있는지 chk 

     => 첫 양무리를 만났을떄 인접 양무리 체크 후 양을 지워버리기 떄문에 '방문 노드 체크가 불필요 ' 
 

'''




from collections import deque 


def bfs(field, x, y, raw, col ):

    
    queue = deque([[x,y]])


    # move  left right up down
    dx = [-1 ,1 ,0 , 0]
    dy = [0 , 0, 1, -1]


    while queue :

        _x, _y = queue.popleft()

        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]


            if n_x < 0 or n_y < 0 or n_x >= raw or n_y >= col : 
                continue

            if  field[n_x][n_y] =='#':
                
                field[n_x][n_y]= '.'
                
                queue.append([n_x,n_y])




def solution():

    raw, col = map(int, input().split())

    field = [ list(input()) for _ in range(raw) ]

    
    cnt = 0

    for raw_idx in range(raw):

        for col_idx in range(col):

            if field[raw_idx][col_idx] == '#' :

                cnt+=1

                bfs(field, raw_idx, col_idx, raw,col)

    return cnt

num = int(input())

for _ in range(num):

    print( solution() )

