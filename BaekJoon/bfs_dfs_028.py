
'''

 Backjoon _ exampels 14562

  "�±ǿ� - �߾Ӵ��б� "   by Jinwoo Lee

  < algorithm >

  0. �̵� ���� ��Ʈ = [ *2 , +1] , but �������� *2 ���� ���Ѵٴ� ���� ���� bfs ������� ������

    => visited & graph node ������ dictionary ���  :  �������� ���ϸ�, ���� ũ�⸦ ������ �� ���� ������ 

    => ������ �� ����� 4%���� ���� �Ͽ��� (�ݷʸ� ���� ã�� ���� )



  1. bfs���� queue�� �ִ� contents�� ���� ���ϴ°�( ��ǥ ) ����, �������� count�� ���� ���ϱ� ������ 
  
    queue = deque([ [ start, end, cnt] ]) �� ���� �ѹ��� �����ִ� �͵� ���� ��� 


  2. �ߺ��� ���� ���� ó���� ������, ��������� �ߺ��� �� n�� �ִٸ�,  +1 ���� *2 �� n�� ������ ������ �������� ( �������� ���� ���� ��� x)

     ���� �ߺ� ó���� ���� �ʾƵ� �ȴ�


 
  * deque() �� scalar element �� ������ [] ���·� �־� �־�� �Ѵ�.

    ���� list�� �ʱⰪ���� ������ ��쿡�� 

    queue = deque( [  ] )   �� �ȿ� ����Ʈ�� �־�� �Ѵ�

    queue = deque( [ [a,b,c]  ] )  =>  [ a,b,c ]

    if queue = deque( [ a,b,c ]) =>  a,b,c



'''

from collections import deque


def bfs(start, end):
    
    cnt = 0 

    queue = deque([ [start, end, cnt ] ])

    while queue:
        
        s_node, e_node, _cnt = queue.popleft()

        if s_node < e_node :

            queue.append([s_node*2, e_node+3, _cnt+1])
            queue.append([s_node+1, e_node, _cnt+1])

        if s_node == e_node :

            return _cnt
        

def solution():
    
    num = int(input())

    for _ in range(num):

        s, e = list(map(int , input().split()))
        
        ans = bfs(s,e)

        print(ans)

solution()


'''
* ���� Ʋ������ bfs �ڵ� 

def bfs(start, end):
    
    
    queue = deque([start])

    visited = [start] 

    
    graph, path = {}, {}

    graph[start], path[start] = end, 0
    
    while queue:

        _node = queue.popleft()
        
        if _node == graph[_node]:

            return path[_node]

        dx = [ _node , 1]
        
        for value in dx:

            n_node = _node + value
            
            if n_node < 0 or n_node > graph[_node]+3 :
                continue

            if n_node not in visited:

                visited.append(n_node)
                queue.append(n_node)
                path[n_node] = path[_node]+1

                if value != 1 :

                    graph[n_node] = graph[_node] +3

                else:
                    graph[n_node] = graph[_node]
        


'''
