
'''

 Backjoon _ exampels 16174

  "점프왕 젤리(Larget)"   by Jinwoo Lee

  < algorithm >

  1. 16173 - 점프왕 젤리(small) 문제와 동일한 코드 사용 -> pass 판정

    * visited 를 table로 형성하여 indexing 접근한것

    * queue 에 넣기 전에 조건 검사하기

    * 범위 밖이면 continue로 처리 
 

'''


from collections import deque


def bfs(area, field):

    queue = deque([[0,0]])

    visited = [[ False for _ in range(area) ]for _ in range(area)]
    
    visited[0][0] = True

    #  right down 
    dx = [1, 0]
    dy = [0, 1]


    while queue :

        _x, _y = queue.popleft()

        amount = field[_x][_y]

        for idx in range(2):

            n_x = _x + (dx[idx] * amount) 
            n_y = _y + (dy[idx] * amount)


            if n_x < 0 or n_y < 0 or n_x >= area or n_y >= area :
                continue

            if not visited[n_x][n_y] :

                queue.append([n_x,n_y])
                visited[n_x][n_y]= True


    if visited[area-1][area-1] : 
        return 'HaruHaru'

    else:
        return 'Hing'




def solution():

    area = int(input())

    field = [list(map(int, input().split())) for _ in range(area)]

    print( bfs(area, field) )


solution() 