
'''

 Backjoon _ exampels 13903

  "���"   by Jinwoo Lee

  < algorithm >

  * ���� ��ǥ���� queue�� �ְ�, bfs ����


  ** ������ ������ ���


  1) ������ bfs�� �޸�, ���� ��ǥ�� ������ �̱� ������ deque�� �������� �����͸� �־�� ��

     start_point = [���� ��ǥ�� ],  queue = deque( start_point )

     => ť�� 1���� ������ or ��ǥ�� �������� ������ deque([��ǥ]) ������, 

        �̹� �������� ��Ҹ� ������ list ������ �����͸� ť�� �ִ� ���̱� ������ []�� ������

        => ���̹� CT 3�� �������� �� �κ��� ������ ���ܼ� �ڵ��� �ϼ����� �������� �����ϱ�


  2) visited ,score ���� Ȱ���ϱ�

    => ������ ���� ��� visited �� 0���� �ʱ�ȭ �Ͽ�, +1 �� ������Ű�鼭 �ִ� ��ΰ��� ���� �� ������

       ������ �ټ� ������ ���, ��ΰ�, �湮���θ� ���� �Ǵ��ϴ� ���� �� �� ���� �������� ��� Ȯ���� ����.



  2) ���������� AC�� �ѹ��� ���� ���� ���� 

   => answer = bfs() 

      if len(answer) == 0 : return -1 

      ���� ���� ���·� ��� �Ұ����� ��� -1, ������ ��� �ּҰ��� ����ϵ��� ���� �Ͽ��µ�

      1 <= row <= 1000 �� ������ ������ �ֱ� ������ 1�� ��� ������ �����


   �� �������� ���� ��ǥ�� bfs�� ���� �ϴ���, ť�� ���� ��ǥ�� ��� �Űܳ��� �����ϸ� �� ���� ��ǥ���� ���ÿ� ����ϴ� ������ �ؼ��� �� �ִ�.

      ������ ������ �� ���� ��ǥ���� ���ÿ� ó������ �ʴ� ��ó�� ��������,  ������ǥ A,B���� ������ �̵� ��Ģ�� ���� �̵��Ѵٸ�, 

      ���� ��ǥ A,B,C, .. ���� ���� ���������� ������ �ڵ��� �Ǵ°��̴�.

      �׷��� ������,

      _x, _y = queue.popleft()

      if _X == row-1 :
        print(score[_x][_y])
        return 0

      ���� ���� ť���� �̾Ƴ� ���� ������ �࿡ �����ߴٸ� �� ���� row�� ������ ��� ���� �߿� �ּҰ� ���� �� �� �ִ�.


'''



from collections import deque 

def bfs(start_point, row, col, field, drow, dcol, n_rule):
    
    queue = deque(start_point)

    visited = [ [ False for _ in range(col)] for _ in range(row) ]

    for value in start_point:

        visited[value[0]][value[1]] = True


    score = [ [ 0 for _ in range(col)] for _ in range(row) ]



    while queue :

        _x, _y = queue.popleft()

        
        if _x == row-1 :

            print(score[_x][_y])

            return 0
        
        for idx in range(n_rule):

            n_x = _x + drow[idx]
            n_y = _y + dcol[idx]

            if n_x < 0 or n_y < 0 or n_x >= row or n_y >= col : continue

            if not visited[n_x][n_y] and field[n_x][n_y] ==1 :

                queue.append([n_x,n_y] )
                visited[n_x][n_y] = True
                score[n_x][n_y] = score[_x][_y] + 1 


    print(-1)




def solution():
    
    row, col = map(int, input().split())

    field = [list(map(int, input().split())) for _ in range(row) ]

    n_rule = int(input())

    drow = []
    dcol = []

    for _ in range(n_rule):
        
        r, c = map(int, input().split())

        drow.append(r)
        dcol.append(c)


    start_point = [] 

    for col_idx in range(col):

        if field[0][col_idx] == 1:

            start_point.append([0, col_idx])


    bfs(start_point, row, col, field, drow, dcol, n_rule)


solution()