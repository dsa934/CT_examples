

from collections import deque


def bfs(node, graph, start):

    visited = [ -1 for _ in range(node+1)]

    visited[start] = 0 

    queue = deque([start])

    while queue:

        _node = queue.popleft()

        for value in graph[_node]:

            if visited[value] == -1 :

                queue.append(value)

                visited[value] = visited[_node] + 1

    return visited




def solution():

    node, edge, start = map(int, input().split())

    graph = [ [] for _ in range(node+1) ]

    for _ in range(edge):

        s,e = map(int, input().split())

        graph[s].append(e)
        graph[e].append(s)

    ans = bfs(node, graph, start)

    for value in ans[1:]:
        print(value)

solution()