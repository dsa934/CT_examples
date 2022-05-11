
'''

 Backjoon _ exampels 10026

  "���ϻ���"   by Jinwoo Lee

  < algorithm >

  1. DFS / BFS ��� ����

  2. �� ���� Ǯ�� TLE�� �ɷȴ�.

  * �湮 ��ǥ�� �����ϱ� ���� visited�� ���¿��� ���� ���� 

   a) visited = []

   b) visited = [ [0] * num for _ in range(num) ] 

   
   a) �� ���, �湮���� ���� ��ǥ (n_x, n_y) �� list�� �߰��ϴ� ����

   b) �� ���, [x][y]�� ���� 2���� �迭��, �湮�� indexing�� ���� 0 -> 1 ��ȯ 


   b)�� ��� indexing ���������� O(1) �� �ݸ�, 

   a)�� ���� list�� �߰��ϰ�, �湮 ���θ� �˻��ҋ� in�� ����Ͽ������� O(n) �� �ȴ�.

   ���� �ð��� �����ϱ� ���ؼ��� b) ����� 2���� �迭 ����� ����ϴ°��� �Ǵ�


'''

from collections import deque


def dfs(graph, area):
    
    visited = [[0] * area for _ in range(area)] 

    answer = 0 

    # left, right, up, down
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    
    for raw in range(area):
        
        for col in range(area):

            if not visited[raw][col] :

                queue = deque()

                answer +=1

                set_color= graph[raw][col]
                
                visited[raw][col] = 1

                queue.append( [raw,col] )
                

                while queue:

                    _x, _y = queue.popleft()
                    

                    for idx in range(4):

                        n_x = _x + dx[idx]
                        n_y = _y + dy[idx]

                        if n_x < 0 or n_y < 0 or n_x >= area or n_y >= area:
                            continue

                        if graph[n_x][n_y] != set_color:
                            continue

                        if visited[n_x][n_y]==0 and graph[n_x][n_y] == set_color:

                            visited[n_x][n_y]= 1
                            
                            queue.append([n_x,n_y])

    return answer




def solution():

    num = int(input())
    
    field =[ input()  for _ in range(num)]
    
    result = dfs(field, num)


    field = [ ['R' if idx == 'G' else idx for idx in raw ] for raw in field ]

    result_color = dfs(field, num)

    return result, result_color




result, result_color = solution()

print( result, result_color )