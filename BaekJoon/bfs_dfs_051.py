
'''

 Backjoon _ exampels 12761

  "���ٸ�"   by Jinwoo Lee

  < algorithm >

  1. �̵� ����� ������ ��������, ������ ���� ���� �������ָ� �����ϰ� �ذ� ����

 

'''




from collections import deque

def bfs(a,b, start, target, max_boundary):
    
    queue = deque([start])

    visited = [ 0 for _ in range(max_boundary+1)]


    dx = [-1, +1, +a, -a, +b, -b ]

    dx_multiple = [a,b]


    while queue:

        _x = queue.popleft()

        for idx in range(6):

            n_x = _x + dx[idx]

            if n_x < 0 or n_x > max_boundary : continue

            if visited[n_x] == 0 :

                queue.append(n_x)
                visited[n_x] = visited[_x] + 1


        for idx in range(2):

            n_x = _x * dx_multiple[idx]

            if n_x < 0 or n_x > max_boundary : continue

            if visited[n_x] == 0 :

                queue.append(n_x)
                visited[n_x] = visited[_x] + 1


    return visited[target]






def solution():
    
    a, b, n, m = map(int, input().split())

    max_boundary = int(1e5)


    print( bfs(a,b, n, m, max_boundary ) )

solution()