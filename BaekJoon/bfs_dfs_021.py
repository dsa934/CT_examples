
'''

 Backjoon _ exampels 1325

  "효율적인 해킹"   by Jinwoo Lee

  < algorithm >

  1. A가 B를 신뢰하면, b를 해킹했을떄 A도 해킹할 수 있음으로 그래프 연결 관계 표현을 '단 방향'으로 해주면 된다

     => graph[B].append( A )


  2. 단 방향에 연결된 그래프에 대해 BFS / DFS 하면 되지만, TLE 떄문에 정확도가 낮은 문제 


  3. TLE를 줄이기 위한 노력들 

   * 입력을 sys로 받는다, import sys, input = sys.stdin.readline   => 이거 굳이 안해도 통과 판정 받음


   * 방문 리스트 구현 시 , element not in visited 형태로 구현하면 시간 복잡도가 O(N), 

     => O(1)로 접근 할 수 있게 indexing 으로 접근


   * queue.append(n_node)

     => 기존에는, queue.append(graph[_node]) 의 형태로 n_node와 연결된 모든 node를 큐에 넣었는데 

        그래프가 cyclic한 경우, 중복된 node에 대한 방문검사가 진행되기 떄문에 시간초과가 발생하는것으로 판단 

        for new_node in graph[_node]를 통해, 연결된 node에 대해 방문검사를 미리 실시하여, 중복 방문검사가 일어나지 않도록 하는것이 중요한듯 


   * list.clear()

    => max_value가 갱신될떄마다 list값을 변환시켜야 하는데, claer를 사용하는 방법은 깔끔한것 같다.
 

   * print ( * list) 
   
     ex)  temp = [1,2,3,4,5] 

          print(temp) = [1,2,3,4,5]

          print(*temp) = 1 2 3 4 5    good !!!   -> 기존에 list를 벗겨내기 위한 조치들을 모두 생략할 수 있어 앞으로 유용하게 사용 가능하다 


'''

#import sys
from collections import deque 
#input = sys.stdin.readline

def bfs(start_x, graph, n_node):

    queue = deque([start_x])

    visited = [ False for _ in range(n_node+1)]
    visited[start_x] = True

    cnt = 1

    while queue :

        _node = queue.popleft()

        # 3-3 TLE 참조 
        for n_node in graph[_node]:

            if not visited[n_node] :

                visited[n_node]= True 
                queue.append(n_node)
                cnt+=1
        
    return cnt



def solution():

    node, edge = list(map(int, input().split()))

    graph = [ [] for _ in range(node+1) ] 

    
    for _ in range(1, edge+1):

        _a, _b = list(map(int, input().split()))
        
        graph[_b].append(_a)
        
    max_value = 0

    result = [] 

    for idx in range(1, node+1):

        cnt = bfs(idx, graph, node)
        
        if cnt > max_value :

            max_value = cnt
            
            result.clear()
            result.append(idx)

        elif cnt == max_value :

            result.append(idx)
            
    print(*result)

solution()