
'''

 Backjoon _ exampels 1389

  "케빈 베이컨의 6단계 법칙"   by Jinwoo Lee

  < algorithm >

  1. 관계 graph, visited array 0 초기화 

  2. sum(visited[1:start_point ]) + sum(visited[start_point+1 :]) 

     방문 array 초기값을 0으로 설정했기 때문에 

     cyclic한 graph 형태를 띈 문제에서는 최초 시작 좌표로 돌아오는 경우의 수도 존재 

     이를 제외하고 계산하는것이 문제의 요구사항임으로 최초 시작 좌표는 제외 한다 .


 

'''


from collections import deque


def bfs(_start, graph, node):
    

    queue = deque([_start])

    visited = [ 0 for _ in range(node+1) ] 
    
    while queue :

        _x = queue.popleft()


        for n_x in graph[_x]:

            if visited[n_x] == 0 :

                queue.append(n_x)

                visited[n_x] = visited[_x] + 1
                
    return sum(visited[1:_start]) + sum(visited[_start+1:])




def solution():
    

    node, edge = map(int, input().split())

    graph = [ [] for _ in range(node+1) ]

    for _ in range(edge):

        s , e = map(int, input().split())

        graph[s].append(e)
        graph[e].append(s)

    
    candidate = [ [] for _ in range(node+1) ]


    for start_point in range(1, node+1):

        candidate[start_point].append( bfs(start_point, graph, node) )


    min_value = min(candidate[1:])

    result = [] 

    for idx, value in enumerate(candidate):

        if value == min_value :

            result.append(idx)

    print(min(result))


solution()