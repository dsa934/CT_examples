
'''

 Backjoon _ exampels 24447

  " 알고리즘 수업 - 너비 우선 탐색 4 "   by Jinwoo Lee

  < algorithm >

  1. 이전 알고리즘 수업 시리즈 총합본 
 

'''



from collections import deque


def bfs(node, graph, start):

    # visited= [depth, order]
    visited = [ [-1,0] for _ in range(node+1)]

    cnt = 1 

    visited[start] = [0, cnt]

    queue = deque([start])

    while queue:

        _node = queue.popleft()

        for value in graph[_node]:

            if visited[value][0] == -1 :

                cnt += 1 

                queue.append(value)

                visited[value][0] = visited[_node][0] + 1

                visited[value][1] = cnt

    return visited




def solution():

    node, edge, start = map(int, input().split())

    graph = [ [] for _ in range(node+1) ]

    for _ in range(edge):

        s,e = map(int, input().split())

        graph[s].append(e)
        graph[e].append(s)

    for value in graph:

        value.sort()


    ans = bfs(node, graph, start)
    
    result = 0
    
    for value in ans[1:]:
        
        order, visit = value

        result += order * visit


    print(result)

solution()