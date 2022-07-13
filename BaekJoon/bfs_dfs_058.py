
'''

 Backjoon _ exampels 15558

  " ���� ���� "   by Jinwoo Lee

  < algorithm >

  1. BFS / DFS ������ ���̵��� ������ ���� '��� ��'�� ���ؾ� �Ѵ�,

    => ���ǿ� �°� ������ �ϰ� ���� �ϴ� �����ǹ� 


  2. visited table 

    => ���� ���� �湮 ��尡 �ʿ� ���� ��������,  �̵� ��Ģ�� +1, -1 , +k ������ �̵����� �ٸ���

       ���� +k �� +1, -1 ���� ���� ������ ���ɼ��� ���� ������ �湮 ��� üũ�� �䱸 �ȴ�


  3. time table 

    => ���� ��ǥ�� ���� ������ �������� '���ÿ�' ���� ��, ���ǿ� �´� ��ǥ���� queue �� �ִ� ����̶� 

       �ܼ��� queue ���� pop ������ �ð� ī��Ʈ�� ���� ��Ű�� ���� �ƴ϶� 

       time[n_x][n_y] = time[_x][_y] + 1 �� ����  �� ��ǥ���� ([ n_x, n_y] ) �θ� ��ǥ ([_x, _y])  �� �ð��� �������� ����ؾ� �Ѵ� 


  4. Ż�� ����

     => ������ �������� ���ϰ� while ���� Ż���ϸ� ���� ���� �Ұ�, ���� ������ ���� ���� ������ ���� ����

        ���� ���� ���� ������ �������� �־����� �迭�� ����(num)�� ���� ��� ���� ���� ������ �ް� �Ǵµ�

        index �� 0���� �����ϱ� ������ 

        ���� ������  _y > num �� �ƴ϶� ,  _y >= num �� �Ǿ�� �Ѵ�  ( �̰� ������ 10�ð� �Ѱ� �ɸ� )




  �� �̷��� bfs/dfs ��� ������ ���������� ������ �������ϰ� ��� �κе��� ���� �䱸 �Ǳ� ������ ���ǰ� �ʿ��ϴ�

'''



from collections import deque


def bfs( start_x, start_y, field, num, k ):

    queue = deque([[start_x, start_y]])

    visited = [ [ False for _ in range(num)] + [False]* k  for _ in range(2) ]

    visited[start_x][start_y] = True


    time = [ [ 0 for _ in range(num)] + [0] *k  for _ in range(2) ]

    #move front, back, jump
    drow = [1, -1, 0, 0]
    dcol = [k, k, 1,-1]
    

    while queue:

        _x , _y = queue.popleft()

        if _y >= num :
            print(1)
            return 0

        for idx in range(4):

            n_x = _x + drow[idx]
            n_y = _y + dcol[idx]


            if n_x < 0 or n_y < 0 or n_x >= 2 or n_y <= time[_x][_y] : continue

            if field[n_x][n_y] == 0 : continue

            
            if not visited[n_x][n_y] :
                
                queue.append([n_x, n_y])
                visited[n_x][n_y] = True
                time[n_x][n_y] = time[_x][_y] + 1

                #print("chk n_x, n_y", n_x, n_y , "_x, _y", _x, _y , "queue", queue, "time", time[n_x][n_y])


    print(0)





def solution():
    
    num , k = list(map(int , input().split()))

    field = [ list(map(int , input())) + [1]* k for _ in range(2) ]

   
    bfs(0, 0, field, num, k )


solution()