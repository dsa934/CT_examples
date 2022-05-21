
'''

 Backjoon _ exampels 14248

  "���� ����"   by Jinwoo Lee


  < algorithm >

  1. ����� �������� ��������

  => �������� bfs ����
 

'''



from collections import deque


def bfs(num, numbers, start):
    

    queue = deque([start])

    visited =[start]

    
    while queue :

        _node = queue.popleft()
        
        dx = [ numbers[_node], -numbers[_node] ] 

        for way in dx :

            n_node = _node + way

            if n_node <= 0 or n_node > num :
                continue

            if n_node not in visited:

                visited.append(n_node)
                queue.append(n_node)

    return len(visited)




def solution():
    

    num = int(input())

    numbers = [0] + list(map(int, input().split()))

    s_pos = int(input())


    ans = bfs(num, numbers, s_pos)


    print(ans)



solution()

