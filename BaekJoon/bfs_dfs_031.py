

'''

 Backjoon _ exampels 11725

  "Ʈ�� �θ� ã��"   by Jinwoo Lee

  < algorithm >

  1. BFS�� �̿��Ͽ�,  ť�κ��� �θ� ��忡 �ش��ϴ� _node�� ����

  2. graph[_node]�� ���� �θ� ���� ���� �� �ڽ� ��� ������ ���, 

     ������ �ڽ� ��尡 �θ� ��尡 ���ٸ� ( ans[value] == 0 ) �θ� ���� 

     for value in graph[_node[]:

        if ans[value] == 0 : 

           ans[value] = _node


  3. ��Ʈ ��忡 �ش��ϴ� 1�� ��� �����ϰ�, 2 ~ N ������ �θ� ��� ��� 
 

'''


from collections import deque

def bfs(boundary, graph):
    

    root_node = 1 

    queue = deque([root_node])

    visited = [ False for _ in range(boundary+1)]
    visited[1] = True

    ans = {} 

    for idx in range(1, boundary+1):

        ans[idx] = 0
 
    while queue :
        

        _node = queue.popleft()

        for value in graph[_node] :
            

            if ans[value] == 0 :

                ans[value] = _node
          

            if not visited[value] :

                queue.append(value)

                visited[value] = True


    for idx,value in ans.items():

        if idx == 1 :
            continue

        print(value)


def solution():

    num = int(input())

    graph = {}

    for idx in range(1, num+1):

        graph[idx] = [] 


    for _ in range(2,num+1):

        start, end = list(map(int, input().split()))

        graph[start].append(end)
        graph[end].append(start)

    bfs(num, graph)



solution()