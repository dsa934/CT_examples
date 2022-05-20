
'''

 Backjoon _ exampels 1679

  " ���� ���� "   by Jinwoo Lee

  < algorithm >

  1. �־��� ���� ���� ���� numbers ���� �ִ� k�� �̾Ƽ� ��������� ���� bfs/dfs ���� ���ϱ�

   => max(numbers) * k ���� ���� ���� , �湮 ��忡 max_value�� �ִٸ� while break 

   => �� ���� ���ڿ� ���� n���� �������� ����°Ͱ� ������ bfs�� ����

  * ������ ���ϴ� ���� ã���� break ���Ѿ� �ϴµ� �Ƚ��Ѽ� ù�õ� Ʋ��


  * 1�� �ݵ�� �����ؾ� �Ѵ��ؼ�, ���۳�尡 1�������� ������


 

'''

from collections import deque


def bfs(max_value, visited, numbers):

    queue = deque([0])

    visited.append(0)


    while queue:

        if max_value in visited:
            break

        _node = queue.popleft()

        for value in numbers:

            n_node = _node + value

            if n_node not in visited:

                visited.append(n_node)

                queue.append(n_node)



def solution():
    
    num = int(input())

    numbers = list(map(int, input().split()))

    n_max = int(input())

    max_value =  max(numbers) * (n_max)


    visited = [] 


    bfs(max_value, visited, numbers)

    
    visited = sorted(visited)
    
    ans = max_value +1 

    for idx, value in enumerate(visited):
        
        if idx != value :


            ans = idx
            break

    return f'holsoon win at {ans}' if ans % 2 == 0 else f'jjaksoon win at {ans}'




print( solution() )