
'''

 Backjoon _ exampels 14218

  "�׷��� Ž�� 2"   by Jinwoo Lee

  < algorithm >

  1. ���� ���踦 ��Ÿ���� graph ���� ��

     �ܹ���, ����� �׷������� üũ�� �� �ؾ� �� !


 

'''



from collections import deque


def bfs(_node, graph, start):
    

    queue = deque([start])
    visited = [False for _ in range(_node+1)]

    visited[start]= True

    score = [-1 for _ in range(_node+1)]
    score[start] = 0

    while queue:

        _node = queue.popleft()

        for n_node in graph[_node]:


            if not visited[n_node] :

                queue.append(n_node)
                visited[n_node] = True
                score[n_node] = score[_node] + 1

    print(*score[1:])



def solution():
    
    _node, _edge = map(int, input().split())

    #init graph
    graph = {}

    for idx in range(_node):

        graph[idx+1] = [] 

    for _ in range(_edge):

        s,e = map(int, input().split())

        graph[s].append(e)
        graph[e].append(s)

    n_change = int(input())

    for _ in range(n_change):

        s,e = map(int, input().split())

        graph[s].append(e)
        graph[e].append(s)

        bfs(_node, graph, 1) 


solution()