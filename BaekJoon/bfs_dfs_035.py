
'''

 Backjoon _ exampels 24445

  "알고리즘 수업 - 너비 우선 탐색 2"   by Jinwoo Lee

  < algorithm >

  1. sort 만 reverse, 나머진 24444와 동일 
 

'''



from collections import deque

def bfs(node, start, graph):

    visited = [ 0 for _ in range(node+1)]
    
    queue = deque([start])
    
    cnt = 1 

    visited[start] = cnt

    while queue :

        _node = queue.popleft()
        
        for value in graph[_node]:

            if visited[value] == 0 :

                cnt+=1

                queue.append(value)
                visited[value] = cnt

                
    return visited




def solution():
    
    node, edge, start = map(int, input().split())

    graph = [ [] for _ in range(node+1)]
    
    for _ in range(edge):

        s, e = list(map(int , input().split()))

        graph[s].append(e)
        graph[e].append(s)

    for value in graph:

        value.sort(reverse= True)
        
    answer = bfs(node, start, graph)

    for idx in range(1,node+1):
        print(answer[idx])

solution()
