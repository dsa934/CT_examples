

'''

 Backjoon _ exampels 11060

  "점프 점프"   by Jinwoo Lee

  < algorithm >

   1. 시작좌표(1)로 부터  각각 1~ numbers[1] 만큼 이동하는 여러 루트 중 최단 거리를 구하는 문제와 같다

      1 -> 1 + 1 
      1 -> 1 + 2 
      ...
      1 -> 1 + numbers[1]



  * 크기가 1이면, 점프를 안해도 되기 떄문에 어떠한 수가 오던지 상관없이 답이 0 
 

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