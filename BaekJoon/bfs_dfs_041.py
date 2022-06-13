
'''

 Backjoon _ exampels 18352

  "특정 거리의 도시 찾기 "   by Jinwoo Lee

  < algorithm >

  1. 자기 자신과의 연결은 0으로 셋팅하기 떄문에,  방문 노드를 체크하기 위한 array 의 초기값을 0으로 줄 경우 통과 판정을 받지 못한다.

     -> (문제 분석)  
     
        모든 node의 초기값을 0으로 주는 경우,  요청 distance(k) 가 0일 경우, 방문하지 않은 node까지 출력해버리는 오류를 범할 수 있음 


        => 방문 노드의 초기값을 -1로 셋팅,  visited[start]= 0 의 방식으로 스타트 지점만 0으로 변환하여 사용하는 방식을 취함

 

'''


from collections import deque 


def bfs(graph, start, node, distance):
    
    queue = deque([start])

    visited = [ -1 for _ in range(node+1)]
    
    visited[start] = 0

    while queue :

        _node = queue.popleft()

        for value in graph[_node]:

            if visited[value] == -1 :

                visited[value] = visited[_node] +1

                queue.append(value)


    ans = [] 

    for idx, value in enumerate(visited):

        if idx == 0 :continue

        if value == distance :

            ans.append(idx)

    if len(ans) == 0 :
        print(-1)

    else:

        for value in sorted(ans):
            print(value)



def solution():

    node, edge, distance, start = map(int, input().split())


    graph = [ [] for _ in range(node+1) ]

    for _ in range(edge):

        s, e = map(int, input().split())

        graph[s].append(e)


    bfs(graph, start, node, distance)


solution()
