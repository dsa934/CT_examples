

'''

 Backjoon _ exampels 18232

  ""   by Jinwoo Lee

  < algorithm >

  
  1. start �������� �̵��� �� �ִ� ������ [ -1, 1, ����������1, ����������2 ... ]

     =>  -1, 1�� ���� ���������� ����� 1�� �ٸ��� ������ �̸� �����ϱ� ���� cnt �ʿ� 

     =>  -1, 1 �� ��� n_node = _node + path 

         ���� �������� 1�� ���  n_node = path 



  2. vistied array �� 0���� set, �̵��� +1 ���� 



  * �ڷ���Ʈ �������� ����� �����̴�, ���� �׷��� ������ ��������� set 




  * python ���� �� TLE, pypy3 ����� ���

    => ���� ���� ��ã�� 


 

'''


from collections import deque 


def bfs(start, end, graph, node):
    
    queue = deque([start])
    
    visited = [ 0 for _ in range(node+1) ]


    while queue :

        _node = queue.popleft()
        
        #print("node & graph", _node, graph[_node])
        
        cnt = 0 

        for path in graph[_node]:

            if cnt == 0 or cnt == 1:

                n_node = _node + path

                cnt+=1

            else:

                n_node = path
            
            
            if n_node <= 0 or n_node > node :
                continue

            if visited[n_node] == 0 :

                queue.append(n_node)
                visited[n_node] = visited[_node] + 1

                
    return visited[end]




def solution():

    node, edge = list(map(int , input().split()))

    start, end = list(map(int ,input().split()))

    graph = {}

    for idx in range(1, node+1):

        graph[idx] = [-1, 1]


    for _ in range(1,edge+1):

        node_s, node_e = list(map(int , input().split()))

        graph[node_s].append( node_e )
        graph[node_e].append(node_s)

    
    ans = bfs(start, end, graph, node)

    return ans


print( solution() )


