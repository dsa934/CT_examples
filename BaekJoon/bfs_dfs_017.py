
'''

 Backjoon _ exampels 2206

  "�� �μ��� �̵��ϱ�"   by Jinwoo Lee

  < algorithm >

  1. visited �� 3�������� �����ϸ�,  �Ʒ��� �� ���� ��츦 ���ÿ� ����� �� �ִ�.

    a) ���� �μ��� �ʰ� �����ϴ� ��Ʈ

    b) ���� �μ��鼭 �����ϴ� ��Ʈ 



    * a)  info[n_x][n_y] == 1  && _wall_count = 1 :                     # (n_x,n_y) �� ���̰�, ���� �μ��� �ʾҴٸ�,

          visiteid[n_x][n_y][0] = visiteid[_x][_y][1] + 1                 ���� �μ� �� �ִ� ��ȸ�� 1���̰�,  (n_x, n_y) �� ���� �μ��� �湮�� ��ǥ������ 

          queue.append( [n_x, n_y, 0 ]  )                                 ť�� (n_x, n_y) ��ǥ�� �߰��ϰ�, �湮��忡 (n_x, n_y) ��ǥ������ �Ÿ������ ���� 
          
                                                                           ��, ���̻� ���� �μ��� ���ϱ� ������, ���� �μ��� ���ϴ� visited[n_x][n_y][0] �� �� �߰� 


                                                                           
    * b)  info[n_x][n_y] == 0  && visited[n_x][n_y][_wall_count] = 0 :  # (n_x,n_y) �� ���� �ƴϰ�, �湮������ ���ٸ�,

          visiteid[n_x][n_y][_wall] = visiteid[_x][_y][_wall] + 1         �ش� ��ǥ ť�� �߰� �� �湮 ��� ���� 

          queue.append( [n_x, n_y, _wall ]  )                              
  


  2. BFS/DFS �˰����� �̷θ� ������ ���� �����Ͱ� ���� 

    => ���� ���� ������ BFS�� ������ ������ ,  ' a)�� ���� �ϸ� ó�� ������ ���� �μ��� ������ ?' ��� �������� �׷��� ������ ���ε�,

      BFS / DFS �˰��򿡼� ���� ��ǥ (start_x, start_y) �� �������� ��,��,��,�� �� ������� ���(����� ��)���� ������ '������'�̴�.

      �Ʒ��� ���ϴ� ��ο��� ���� �μ��ٰ� �ؼ�,  ��,��,���� �������� �̵��ϴ� ��ε��� ���� �μ��� ���ϴ� ���� �ƴϴ�.

      �� ��Ʈ���� ������������,  �ִ� ��θ� �����Կ� �־� ���� ��ǥ�� Ȱ�������� ( visited[n_x][n_y][_wall] = visited[_x][_y][_wall]+1) 

      visited[n_x][n_y][0] = visited[x][y][1] + 1  �� ���� 3���� �迭�� ����,  �� ��ġ (n_x, n_y)���� ���� �ν��ٸ�,

      �� ���� ���� ��ġ�� ���� ���̻� �μ� �� ���� �湮��� vistied[n_x][n_y][0] �� �ִ� ��Ʈ ���� �����ؾ� �Ѵ�.


      �̷��� �� ������ �������� �޹�ħ �ϱ� ����, 

      ������ 2���� �迭�� visited�� Ȱ���ϴ� �Ͱ� �޸�, 3�������� �����ϵ�, 3������ ������ ���� �Κb�°��� ���� yes/no �� offset ������ �� ���ִ� [0][0] �� �߰����ش� .





  3. visited =  [ [ [0] *2  ]  for _ in range(col) ] for in range(raw)  ] 

    3���� �̻��� �迭�� list ������ ������ ���, 

    raw : ���� �ۿ� ����, col : �ι��� ���� 

    n : col ���� ���ʿ� ���� 

    ex)  visited = [  [ [0] * 2 ] for _ in range(3) ] for in rnage(2) ] 

       [     
           [ [0], [0] ] , [ [0], [0] ], [ [0], [0] ]

           [ [0], [0] ] , [ [0], [0] ], [ [0], [0] ]
       
       
       ]





  * ������ '������' ������ �ٸ��� ��� ���� ���� BFS�� �� ��� TLE�� �ɸ��� ( '1����' ���� �� �ִٴ� ���� Hint )

    => BFS�� �ð� ���⵵ O(NM) , N x M field�� ��� ã�ƾ� ������ 

       ������ �ִ� ���� n x m  ������ ,  

       �ϳ��� ������ ���� bfs�� ������ ����� �ð� ���⵵�� O( (NM)^2 ) => TLE

 

'''

from collections import deque


def bfs(field, w, h):

    
    queue = deque()

    visited = [ [ [0] * 2 for _ in range(h) ] for _ in range(w) ]

    visited[0][0][1] = 1
    
    queue.append([0,0,1])

    # left right up down
    dx = [-1 , 1, 0, 0]
    dy = [0 , 0, -1, 1]
    
    while queue:

        _x, _y, _wall = queue.popleft()


        if _x == w -1 and _y == h-1 : 

            return visited[_x][_y][_wall]

        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]
            
            if n_x < 0 or n_y < 0 or n_x >= w or n_y >= h :
                continue

            if field[n_x][n_y] == 1 and _wall == 1:

                visited[n_x][n_y][0] = visited[_x][_y][1] + 1

                queue.append([n_x,n_y,0])

            elif field[n_x][n_y] == 0 and visited[n_x][n_y][_wall] == 0 :
                
                visited[n_x][n_y][_wall] = visited[_x][_y][_wall] + 1

                queue.append([n_x,n_y,_wall])
                
    return -1



def solution():
    
    w, h = list(map( int, input().split() ))

    field = [list(map(int, input())) for _ in range(w) ]
    
    return bfs(field,w,h)



print( solution() )

