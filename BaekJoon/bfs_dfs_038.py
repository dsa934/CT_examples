
'''

 Backjoon _ exampels 18126

  "너구리 구구 (가톨릭대 p대회)"   by Jinwoo Lee

  < algorithm >

  1. 4가지 정보가 필요

   1) 연결 관계를 나타내는 graph

   2) 방문 여부를 나타내는 visited
   
   3) 연결 노드별 가중치를 weight 

   4) 목적지 도착 시 weight 값을 저장할 set_score



  * 시작 위치 1고정, 가장 먼 방은 주어진 num이 아니라, weight_sum이 가장 큰 값을 출력하는것 (첫 시도에 이거 착각 )
 

'''


from collections import deque 


def bfs(graph, score, num):

    queue = deque([1])

    visited = [ False for _ in range(num+1) ]

    set_score = [  0 for _ in range(num+1) ]

    visited[1] = True


    ans = 0 


    while queue:

        _node = queue.popleft()

        for value in graph[_node]:

            if not visited[value] :

                queue.append(value)
                visited[value] = True

                set_score[value] = set_score[_node] + score[_node][value]


    return max(set_score)







def solution():

    num = int(input())

    graph = [ [] for _ in range(num+1) ]

    score = [ [0 for _ in range(num+1)] for _ in range(num+1) ]

    
    for _ in range(num-1):

        start, end, weight  = map(int, input().split())

        graph[start].append(end)
        graph[end].append(start)

        score[start][end] = weight
        score[end][start] = weight


    print(  bfs(graph, score, num)  )

solution()



