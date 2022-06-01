
'''

 Backjoon _ exampels 16173

  "������ �A��(SMALL)"   by Jinwoo Lee

  < algorithm >

  1. ���� ������ ������ ĭ�� �� ��ŭ �̵�,  ���� = < right, down > 

    =>  amount = field[_x][_y]
    
        n_x = _x + (dx[idx] * amount)

        n_y = _y + (dy[idx] + amount )
 
  2. �ð� ���⵵�� ���̱� ���� visited�� table�� ����

     => ��� �ε��� �������� O(1)

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