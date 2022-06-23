
'''

 Backjoon _ exampels 6118

  "���ڲ���"   by Jinwoo Lee

  < algorithm >

  1, ����� ���� �׷��� ����

  2. visited array�� 0���� �ʱ�ȭ, ���� ������ �����ϰ� ī����

     => �ʱⰪ�� 0���� �����ϸ�, ����node ���� 0�̱� ������ update �Ǵµ�,

        �������� �䱸�ϴ� ���� ���� �� start ������ ���� 

        ex) after bfs operations ,  visited[start] =0 
 

'''




from collections import deque


def bfs(start, graph, node, edge):
    
    queue = deque([start])

    visited = [ 0 for _ in range(node+1) ]


    while queue :


        _node = queue.popleft()

        for n_node in graph[_node]:

            if visited[n_node] == 0:

                queue.append(n_node)

                visited[n_node] = visited[_node] + 1

                
    visited[start] = 0

    max_value = max(visited)

    candidate = [] 

    for idx, value in enumerate(visited):

        if max_value == value : candidate.append(idx)


    return sorted(candidate)[0], max_value, len(candidate)



def solution():
    
    node, edge = map(int, input().split())

    graph =[ [] for _ in range(node+1) ]

    for _ in range(edge):

        s,e = map(int, input().split())

        graph[s].append(e)
        graph[e].append(s)



    ans = bfs(1, graph, node, edge)


    print(*ans)

solution()