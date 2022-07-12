
'''

 Backjoon _ exampels 14496

  "�״�, �׸Ӱ� �Ǿ�"   by Jinwoo Lee

  < algorithm >

  * �⺻���� bfs ����, ������ Ǯ�� ����� �ٸ��� ������ �κ� ���

    1.  queue ���� pop ������ �������� ��� ���� ����ϰ� �Լ� ����

       => bfs�� ����ġ��, for������ �ѹ� �� �����ϴ� ���� �ڵ庸�� ��������

       => ���� ��ǥ�� �������� ���� ���, bfs ���� �� -1 ���� ��������ν� ���ź��� �� ��������



'''



from collections import deque

def bfs(start, end, node, graph):
    
    queue = deque([start])

    visited = [ 0 for _ in range(node+1)]

    visited[start]= 0

    while queue:

        _node = queue.popleft()

        if _node == end :

            print(visited[_node])

            return 0

        for n_node in graph[_node]:

            if n_node < 0 or n_node > node: continue

            if visited[n_node] == 0 :

                queue.append(n_node)
                visited[n_node] = visited[_node] + 1
             
              
    print(-1)





def solution():
    
    s, e = map(int, input().split())

    node, edge = map(int , input().split())

    graph= {}

    for idx in range(node):

        graph[idx+1] = []


    for _ in range(edge):

        _s, _e = map(int, input().split())

        graph[_s].append(_e)
        graph[_e].append(_s)

    bfs(s,e, node, graph)

        


solution()
