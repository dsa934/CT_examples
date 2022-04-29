
'''

 Backjoon _ exampels 5014

  "Start link"   by Jinwoo Lee

  < 알고리즘 >

  1. 최단 경로 문제임으로 BFS로 풀이 

  2. visited를 활용하여 가능한 경우의 수가 없는 경우 'use the stairs'

  3. score를 활용하여 각 층에 도달 했을떄의 버튼을 누른 횟수를 기록 


  * 주의 

  1. 문제에 의거하여 건물의 층수는 0층이 없기 때문에 새로 갱신된 위치(n_pos)가 0일 경우도 제외 해야 함 


 
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

            # 0층이 없고, 1층부터 시작이기 떄문에 n_pos == 0일 경우는 제외 해야함 
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

