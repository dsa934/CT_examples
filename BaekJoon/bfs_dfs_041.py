
'''

 Backjoon _ exampels 18352

  "Ư�� �Ÿ��� ���� ã�� "   by Jinwoo Lee

  < algorithm >

  1. �ڱ� �ڽŰ��� ������ 0���� �����ϱ� ������,  �湮 ��带 üũ�ϱ� ���� array �� �ʱⰪ�� 0���� �� ��� ��� ������ ���� ���Ѵ�.

     -> (���� �м�)  
     
        ��� node�� �ʱⰪ�� 0���� �ִ� ���,  ��û distance(k) �� 0�� ���, �湮���� ���� node���� ����ع����� ������ ���� �� ���� 


        => �湮 ����� �ʱⰪ�� -1�� ����,  visited[start]= 0 �� ������� ��ŸƮ ������ 0���� ��ȯ�Ͽ� ����ϴ� ����� ����

 

'''


from collections import deque 


def bfs(graph, start, node, distance):
    
    queue = deque([start])

    visited = [ -1 for _ in range(node+1)]
    
    visited[start] = 0

    while queue :

        _node = queue.popleft()

        for value in graph[_node]:

            if visited[value] == -1 :

                visited[value] = visited[_node] +1

                queue.append(value)


    ans = [] 

    for idx, value in enumerate(visited):

        if idx == 0 :continue

        if value == distance :

            ans.append(idx)

    if len(ans) == 0 :
        print(-1)

    else:

        for value in sorted(ans):
            print(value)



def solution():

    node, edge, distance, start = map(int, input().split())


    graph = [ [] for _ in range(node+1) ]

    for _ in range(edge):

        s, e = map(int, input().split())

        graph[s].append(e)


    bfs(graph, start, node, distance)


solution()
