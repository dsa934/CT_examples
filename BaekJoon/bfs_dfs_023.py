
'''

 Backjoon _ exampels 1240

  "노드사이의 거리 "   by Jinwoo Lee

  < algorithm >
 
  1. graph / tree 문제에서 각 노드사이의 거리를 구하는 문제에는 3가지 + bfs/dfs 알고리즘 필요  

  * 관계 그래프 

    => 각 node 들의 연결 관계를 표현 ( 양방향, 단방향은 문제에 맞게 설정 )


  * score dict 

    => socre[child_node] = score[parent_node] + weight_Table[parent][child]

      score[parent_node]는 bfs/dfs 탐색 과정에서, child_node 직전까지 얼마만큼의 비용(간선의 합) 이 들었는지에 대한 누적 합

      bfs/dfs 알고리즘에 의해 parent, child가 수시로 변화 됨 


    => wieght_table 대신 + 1 을 할 경우 '촌수 계산' 문제 

 
  * weight table ( 생략 가능 )

    => '촌수 계산' 문제의 경우 node와 인접 node 간의 간선의 크기가 1로 고정이기 떄문에 생략이 가능

       but '노드 사이의 거리' 문제에서는 각 노드별 간선의 크기가 다르기 떄문에, 각 연결된 노드별 간선의 크기를 나타내 줄 weight table 필요 ( 2차원 )


'''


from collections import deque

def bfs(start, end, graph, n , weight):

    visited =  [ False for _ in range(n+1) ]

    queue = deque([start])

    visited[start] = True


    score = {} 
    
    for idx in range(1,n+1):
        
        score[idx] = 0
        

    while queue : 

        _node = queue.popleft()
        
        for n_node in graph[_node]:

            if not visited[n_node] : 

                queue.append(n_node)
                visited[n_node] = True
                
                score[n_node] = score[_node] +  weight[_node][n_node]


    return score[end]



def solution():
    
    n, m = list(map(int , input().split()))

    graph = {}
    weight = [[ 0 for _ in range(n+1) ] for _ in range(n+1) ]

    for idx in range(1,n+1):

        graph[idx] = []
        


    for _ in range(n-1):

        s, e, w = list(map(int, input().split()))

        graph[s].append(e)
        graph[e].append(s)

        weight[s][e] = w
        weight[e][s] = w

    ans = [] 

    for _ in range(m):

        start, end = list(map(int, input().split()))

        ans.append( bfs(start, end, graph, n , weight))


    for value in ans:
        print(value)


solution()