

'''

 Backjoon _ exampels 11060

  "���� ����"   by Jinwoo Lee

  < algorithm >

   1. ������ǥ(1)�� ����  ���� 1~ numbers[1] ��ŭ �̵��ϴ� ���� ��Ʈ �� �ִ� �Ÿ��� ���ϴ� ������ ����

      1 -> 1 + 1 
      1 -> 1 + 2 
      ...
      1 -> 1 + numbers[1]



  * ũ�Ⱑ 1�̸�, ������ ���ص� �Ǳ� ������ ��� ���� ������ ������� ���� 0 
 

'''


from collections import deque


def bfs(num, numbers):


    visited = [0 for _ in range(num+1)]

    queue = deque([1])


    while queue :

        _node = queue.popleft()

        for value in range(1, numbers[_node]+1):

            n_node = _node + value


            if n_node <= num and visited[n_node] == 0 :

                visited[n_node] = visited[_node] + 1

                queue.append(n_node)

    return visited[num] if visited[num] != 0 else -1 

def solution():
    

    num = int(input())

    numbers = [0] + list(map(int, input().split()))

    if num == 1 :
        return 0

    return bfs(num,numbers)

print( solution() )