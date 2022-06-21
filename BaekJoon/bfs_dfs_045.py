
'''

 Backjoon _ exampels 1389

  "�ɺ� �������� 6�ܰ� ��Ģ"   by Jinwoo Lee

  < algorithm >

  1. ���� graph, visited array 0 �ʱ�ȭ 

  2. sum(visited[1:start_point ]) + sum(visited[start_point+1 :]) 

     �湮 array �ʱⰪ�� 0���� �����߱� ������ 

     cyclic�� graph ���¸� �� ���������� ���� ���� ��ǥ�� ���ƿ��� ����� ���� ���� 

     �̸� �����ϰ� ����ϴ°��� ������ �䱸���������� ���� ���� ��ǥ�� ���� �Ѵ� .


 

'''


from collections import deque


def bfs(_start, graph, node):
    

    queue = deque([_start])

    visited = [ 0 for _ in range(node+1) ] 
    
    while queue :

        _x = queue.popleft()


        for n_x in graph[_x]:

            if visited[n_x] == 0 :

                queue.append(n_x)

                visited[n_x] = visited[_x] + 1
                
    return sum(visited[1:_start]) + sum(visited[_start+1:])




def solution():
    

    node, edge = map(int, input().split())

    graph = [ [] for _ in range(node+1) ]

    for _ in range(edge):

        s , e = map(int, input().split())

        graph[s].append(e)
        graph[e].append(s)

    
    candidate = [ [] for _ in range(node+1) ]


    for start_point in range(1, node+1):

        candidate[start_point].append( bfs(start_point, graph, node) )


    min_value = min(candidate[1:])

    result = [] 

    for idx, value in enumerate(candidate):

        if value == min_value :

            result.append(idx)

    print(min(result))


solution()