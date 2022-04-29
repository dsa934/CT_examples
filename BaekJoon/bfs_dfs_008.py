
'''

 Backjoon _ exampels 5014

  "Start link"   by Jinwoo Lee

  < �˰��� >

  1. �ִ� ��� ���������� BFS�� Ǯ�� 

  2. visited�� Ȱ���Ͽ� ������ ����� ���� ���� ��� 'use the stairs'

  3. score�� Ȱ���Ͽ� �� ���� ���� �������� ��ư�� ���� Ƚ���� ��� 


  * ���� 

  1. ������ �ǰ��Ͽ� �ǹ��� ������ 0���� ���� ������ ���� ���ŵ� ��ġ(n_pos)�� 0�� ��쵵 ���� �ؾ� �� 


 
'''

from collections import deque

def bfs():

    f, s, g, u, d = list(map(int, input().split()))

    num_button, max_value = 0 , 100000

    if s == g: return num_button

    dx = [u, -d]

    queue = deque()

    visited = set()

    score ={}

    for idx in range(1, f+1):

        score[idx] = 0
    
    queue.append([s,num_button])
    visited.add(s)

    while queue:

        _pos, _cost = queue.popleft()

        for idx in range(2):

            n_pos = _pos + dx[idx]

            # 0���� ����, 1������ �����̱� ������ n_pos == 0�� ���� ���� �ؾ��� 
            if n_pos <= 0 or n_pos > f : continue

            else:

                if n_pos not in visited :

                    n_cost = _cost + 1

                    score[n_pos] = n_cost

                    visited.add(n_pos)

                    queue.append([n_pos, n_cost])

    
    if g not in visited :
        
        return "use the stairs"

    else:

        return score[g]

print(bfs())

