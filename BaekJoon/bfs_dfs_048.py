
'''

 Backjoon _ exampels 6118

  "숨박꼭질"   by Jinwoo Lee

  < algorithm >

  1, 양방향 관계 그래프 설정

  2. visited array를 0으로 초기화, 시작 지점을 제외하고 카운팅

     => 초기값을 0으로 설정하면, 시작node 역시 0이기 때문에 update 되는데,

        문제에서 요구하는 답을 구할 때 start 지점은 제외 

        ex) after bfs operations ,  visited[start] =0 
 

'''




from collections import deque


def bfs(start, graph, node, edge):
    
    queue = deque([start])

    visited = [ 0 for _ in range(node+1) ]


    while queue :


        _node = queue.popleft()

        for n_node in graph[_node]:

            if visited[n_node] == 0:

                queue.append(n_node)

                visited[n_node] = visited[_node] + 1

                
    visited[start] = 0

    max_value = max(visited)

    candidate = [] 

    for idx, value in enumerate(visited):

        if max_value == value : candidate.append(idx)


    return sorted(candidate)[0], max_value, len(candidate)



def solution():
    
    node, edge = map(int, input().split())

    graph =[ [] for _ in range(node+1) ]

    for _ in range(edge):

        s,e = map(int, input().split())

        graph[s].append(e)
        graph[e].append(s)



    ans = bfs(1, graph, node, edge)


    print(*ans)

solution()