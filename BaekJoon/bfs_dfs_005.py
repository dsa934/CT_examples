
'''

 Backjoon _ exampels 2644

  "촌수 계산"   by Jinwoo Lee


 < bfs / bfs 실 문제 적용 알고리즘 >


 1. 문제 정보에 따른 양방향 관계 그래프 구성


 2. BFS를 이용한 최단 거리 문제

    - 최단 거리 문제의 경우, 특정 좌표(x,y) 에서 갈 수 있는 모든 방향 에 대하여 

      field[nx][ny] = field[x][y] + 1 의 형태로 값을 update 하면서, 특정 지역(n,m)에 도달헀을때의 최단거리 값을 도출 하는 형태 



 3. 촌수문제는 BFS를 이용한 최단 거리 문제와 같다 

  - 문제 풀이에 필요한 것 
  
    1. BFS & DFS 알고리즘 실행을 위한 < 양방향 관계 그래프 , visited > 

    2. 위 알고리즘을 실행하며, 각 node 별 가중치 계산을 위한 Score list 

  

  - Algorithm 

    * 기존에는 stack & queue.extend(graph[_node]) 와 같이 _node 에 연결된 모든 다른 node들을 한번에 stack & queue 에 올렸으나 

       이 문제의 경우 각 node 별 비용을 계산해 주어야 하기 떄문에 

       a) 최초 시작점은 stack & visited 에 미리 넣어줌

       b) 각 node 별 비용 계산을 위해 for 문을 통해 개별적으로 접근하여 
    
           - 각 node 별 도착 score 값 update 

           - queue 에 값 update 


        2          4        
      /  \        /
     3    5     10             
   / | \
  7  8 9 


  * 시작점(5) 에서 도착점(7) 까지의 촌수는 3촌 -> 7, 8, 9 모두 5와 3촌 임에 주의 



 4. end가 visited 에 없을 경우 -1 return < 문제 조건 > 


'''

def make_grpah():

    num_person = int(input())

    start, end = list(map(int ,input().split()))

    num_edge = int(input())

    graph = {}

    score = {}

    for idx in range(1, num_person+1):

        graph[idx] = []
        score[idx] = 0


    for _ in range(num_edge):

        _node, _edge = list(map(int, input().split()))

        graph[_node].append(_edge)
        graph[_edge].append(_node)

    return graph, score,  start, end


def bfs(graph, score, start, end):

    queue = []

    visited = []

    # a) 설명 참조 
    queue.append(start)

    visited.append(start)

    while queue:

        _node = queue.pop(0)
       
        # b) 설명 참조
        for _value in graph[_node]:

            if _value not in visited:

                visited.append(_value)

                score[_value] = score[_node] + 1

                queue.append(_value)

    if end not in visited :

        return -1

    return score[end]

        


info_graph, score, start, end = make_grpah()

print ( bfs(info_graph, score, start, end)  )
