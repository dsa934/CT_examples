

'''

 Backjoon _ exampels 1326

  "��¦��¦"   by Jinwoo Lee

  < algorithm >

  0. �⺻���� bfs/dfs �������� ������Ұ� 3���� ����


  1. '¡�� �ٸ��� ���� �ִ� ���� �����ŭ ������ �ִ� �� �̵� ����'  

      =>  ex) 3�̸�, +3, -3 �̵� ����

  2.  �ִ� �̵� Ƚ�� ������ dp[n_node] = dp[_node] + 1 


  3. queue���� ���� node�� end�� ��� break �Ͽ� �ð� ���� & ������ �� ������ -1 ��� 


 

'''


from collections import deque

def bfs(num, numbers, start, end):

    queue =deque([start])

    visited = [False for _ in range(num+1)] 

    visited[start] = True

    graph = [0 for _ in range(num+1)]


    while queue:

        _node = queue.popleft()

        if _node == end:break
 
        dx = [] 

        for value in range(1, num+1):

            if value % numbers[_node] == 0 :

                dx.append(value)
                dx.append(-value)

        for idx in dx:

            n_node = _node + idx

            if n_node <= 0 or n_node > num :
                continue

            if not visited[n_node] :

                queue.append(n_node)
                visited[n_node] = True

                graph[n_node] = graph[_node] + 1
                
    return -1 if graph[end] == 0 else graph[end]



def solution():
    
    num = int(input())

    numbers = [0] + list(map(int, input().split()))

    start, end = list(map(int , input().split()))


    ans = bfs(num, numbers, start, end)

    return ans

print( solution() )