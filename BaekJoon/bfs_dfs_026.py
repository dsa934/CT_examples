

'''

 Backjoon _ exampels 1326

  "폴짝폴짝"   by Jinwoo Lee

  < algorithm >

  0. 기본적인 bfs/dfs 문제지만 함정요소가 3가지 있음


  1. '징검 다리에 쓰여 있는 수의 배수만큼 떨어져 있는 곳 이동 가능'  

      =>  ex) 3이면, +3, -3 이동 가능

  2.  최단 이동 횟수 임으로 dp[n_node] = dp[_node] + 1 


  3. queue에서 꺼낸 node가 end일 경우 break 하여 시간 단축 & 도달할 수 없으면 -1 출력 


 

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