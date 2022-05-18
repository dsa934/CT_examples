
'''

 Backjoon _ exampels 1325

  "ȿ������ ��ŷ"   by Jinwoo Lee

  < algorithm >

  1. A�� B�� �ŷ��ϸ�, b�� ��ŷ������ A�� ��ŷ�� �� �������� �׷��� ���� ���� ǥ���� '�� ����'���� ���ָ� �ȴ�

     => graph[B].append( A )


  2. �� ���⿡ ����� �׷����� ���� BFS / DFS �ϸ� ������, TLE ������ ��Ȯ���� ���� ���� 


  3. TLE�� ���̱� ���� ��µ� 

   * �Է��� sys�� �޴´�, import sys, input = sys.stdin.readline   => �̰� ���� ���ص� ��� ���� ����


   * �湮 ����Ʈ ���� �� , element not in visited ���·� �����ϸ� �ð� ���⵵�� O(N), 

     => O(1)�� ���� �� �� �ְ� indexing ���� ����


   * queue.append(n_node)

     => ��������, queue.append(graph[_node]) �� ���·� n_node�� ����� ��� node�� ť�� �־��µ� 

        �׷����� cyclic�� ���, �ߺ��� node�� ���� �湮�˻簡 ����Ǳ� ������ �ð��ʰ��� �߻��ϴ°����� �Ǵ� 

        for new_node in graph[_node]�� ����, ����� node�� ���� �湮�˻縦 �̸� �ǽ��Ͽ�, �ߺ� �湮�˻簡 �Ͼ�� �ʵ��� �ϴ°��� �߿��ѵ� 


   * list.clear()

    => max_value�� ���ŵɋ����� list���� ��ȯ���Ѿ� �ϴµ�, claer�� ����ϴ� ����� ����Ѱ� ����.
 

   * print ( * list) 
   
     ex)  temp = [1,2,3,4,5] 

          print(temp) = [1,2,3,4,5]

          print(*temp) = 1 2 3 4 5    good !!!   -> ������ list�� ���ܳ��� ���� ��ġ���� ��� ������ �� �־� ������ �����ϰ� ��� �����ϴ� 


'''

#import sys
from collections import deque 
#input = sys.stdin.readline

def bfs(start_x, graph, n_node):

    queue = deque([start_x])

    visited = [ False for _ in range(n_node+1)]
    visited[start_x] = True

    cnt = 1

    while queue :

        _node = queue.popleft()

        # 3-3 TLE ���� 
        for n_node in graph[_node]:

            if not visited[n_node] :

                visited[n_node]= True 
                queue.append(n_node)
                cnt+=1
        
    return cnt



def solution():

    node, edge = list(map(int, input().split()))

    graph = [ [] for _ in range(node+1) ] 

    
    for _ in range(1, edge+1):

        _a, _b = list(map(int, input().split()))
        
        graph[_b].append(_a)
        
    max_value = 0

    result = [] 

    for idx in range(1, node+1):

        cnt = bfs(idx, graph, node)
        
        if cnt > max_value :

            max_value = cnt
            
            result.clear()
            result.append(idx)

        elif cnt == max_value :

            result.append(idx)
            
    print(*result)

solution()