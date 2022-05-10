

'''

 Backjoon _ exampels 4963

  "���� ����"   by Jinwoo Lee

  < algorithm >

  1. �� ��ǥ(x,y)�� ���Ͽ� �湮������ ���� ��� (not visited) bfs�� �����Ѵ�

  
  2. bfs ���� visited �� ��� ��ǥ�� ���ؼ��� 0���� ��ȯ 

    * 2�� �������� �ߺ����� bfs �˰����� �����ϴ� ���� ����

    * �׷����� ���°� �ƴ�, �迭�� ���·� ������ ���޵�����, �ߺ� ������ ���� 0���� ��ȯ�ؾ��� 



  3. 1���� bfs�� �����ҋ����� result +=1 �Ͽ� ���� ���� ���� 



  * ó���� ���� �޶��� ������, �� ���������� �밢�̵�(diagonal) ��ҵ� �����ϱ� ����


  * �� ������ �׷����� ���·� Ǯ��, 0���� ��ȯ�ϴ� ������ ������ �� �־� ������ ������ ���� ����غ��� 
 

'''

from collections import deque

def bfs(w, h):

    field = [list(map(int,input().split())) for _ in range(h)]
    

    visited = []

    queue = deque()

    result = 0


    #    left, right, up, down. diagonal(11) , diagonal(13), diagonal(17), diagonal(19)
    dx = [-1, 1, 0 , 0, -1, 1, 1, -1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]


    for raw in range(h):

        for col in range(w):

            if field[raw][col] == 1 and [raw,col] not in visited:

                queue.append([raw,col])
                visited.append([raw,col])
                result +=1
                while queue:

                    _x , _y = queue.popleft()

                    for idx in range(8):

                        n_x = _x + dx[idx]
                        n_y = _y + dy[idx]

                        if n_x < 0 or n_y < 0 or n_x >= h or n_y >= w :

                            continue

                        if field[n_x][n_y] == 0:
                            continue

                        else:

                            if [n_x, n_y] not in visited:

                                queue.append([n_x,n_y])

                                field[n_x][n_y]= 0

                                visited.append([n_x, n_y])



    return result





def solution():


    while True:

        w, h = list(map(int,input().split()))

        if w ==0 and h == 0 : break

        print ( bfs (w,h ) )




solution()