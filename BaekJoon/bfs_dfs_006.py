'''

 Backjoon _ exampels 1667

  "���ڲ���"   by Jinwoo Lee


  ���� ���� : Start -> End ������ �ִ� ��θ� ���ϴ� ������ �̵� ������ dx = [ -1, +1, x2 ] �� ���� 

  1. �ִ� ��� ������ bfs �˰��� Ȱ��

  2. �ٽ� ���̵�� 

     * [��ǥ��, �ش� ��ǥ�ϋ��� cost] ������ queue�� Ȱ��

     * visited�� ������ [] ���°� �ƴ� set()�� ����ؾ� �ߺ��� ����� 

       => �̹� �湮�� ���̶�� �� ���� ����ϱ� ���� �������� ���� ������ 

          �ֳ� ?  �̹� �湮�� ���̶�� �ش� ���� �����ϱ� ���� �������� �̹� �޼� ���ִٰ� ������ �� ���� 


     * �� �������� ���� ( 0<= pos <= 100000 )�� �������� ������ �ð� �ʰ��� �ɸ� 

       1.  pos >= 0       ,    ���� �� ��� *2 ������ ����� �ʿ� ���� ���̰��� �þ� �� �� ���� 

       2.  pos <= 100000  ,   

          ���� 100000�� �����ؾ� �ϴ� ���� ���ؼ� �����غ���

          a) 50001 x2 -1 -1 

          b) 50001 -1 x2 

          a) ���� b)�� ��� ����� �� ���� 




'''

def bfs(start, end):
    
    queue = []
    visited = set()

    max_value = 100000

    cost = 0

    dx = [ -1, 1 , 2 ]

    queue.append([start,cost])

    visited.add(start)
    

    while queue:

        _pos, _cost = queue.pop(0)

        if _pos == end :

            return _cost

        
        for idx in range(3):



            if idx == 2 : 

                n_pos = _pos * dx[idx]


            else:

                n_pos = _pos + dx[idx]



            if n_pos not in visited and n_pos <= max_value and n_pos >= 0 :

                visited.add(n_pos)

                n_cost = _cost + 1

                queue.append([n_pos, n_cost])
        



start, end = list(map(int, input().split()))

print( bfs(start, end) )