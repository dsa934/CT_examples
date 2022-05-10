
'''

 Backjoon _ exampels 11742

  "���� ����� ����"   by Jinwoo Lee

  < algorithm >

  1. �� vertex�� ���� ���� ���� Ȯ���� ���� BFS �˰��� ���� 

  2. BFS�� �����ϴ� ������ ������� �湮���� ���� vertex�� �������� �Ѵ�

  3. �湮���� ���� vertex�� ������ ���, result+=1 �� ���� ���������� ���� Ȯ���Ѵ�.



  * �ش� �˰������� python ������ TLE, pypy ������ ����� ��� �� ������ ?

    => python���� TLE ,pypy���� ����� �Ǵ� ���� ��� �˰����� ������ �ƴ� �Է°��� ���� ����̴�.

       �� ��� sys ���̺귯���� ���� readlines ���� �ذ�Ǵµ�, ���׿����� ����Ǵ� ����� �ƴϴ�

       ����, �˰����� �Ϻ��ϴٰ� �����ȴٸ� pypy�� �����غ���, ���� �� ����� �ȴٸ� �˰��� ��ü�� ������ �������� ���� �Ǻ��θ� �������

       �ش� ������ ���� ��ü���� �ذ���� ���� �� ����.

 

'''


from collections import deque

def solution():

    vertex, edge = list(map(int , input().split()))

    graph = {}

    for idx in range(1, vertex+1):

        graph[idx] = []


    for _ in range(edge):

        _start, _destination = list(map(int, input().split()))

        graph[_start].append(_destination)
        graph[_destination].append(_start)



    visited =[]

    result = 0

    queue = deque()


    for pos in range(1, vertex+1):

        if pos not in visited :

            visited.append(pos)

            queue.extend(graph[pos])

            result +=1 

            while queue:

                _vertex = queue.popleft()

                if _vertex not in visited:

                    visited.append(_vertex)

                    queue.extend(graph[_vertex])

    return result




print( solution() )

