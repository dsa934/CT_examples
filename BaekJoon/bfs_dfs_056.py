
'''

 Backjoon _ exampels 14496

  "그대, 그머가 되어"   by Jinwoo Lee

  < algorithm >

  * 기본적인 bfs 문제, 기존의 풀던 방법과 다르게 발전된 부분 기록

    1.  queue 에서 pop 했을때 목적지일 경우 답을 출력하고 함수 종료

       => bfs를 끝마치고, for문으로 한번 더 조사하던 과거 코드보다 간결해짐

       => 최종 목표에 도달하지 못한 경우, bfs 종료 후 -1 등을 출력함으로써 과거보다 더 간결해짐



'''



from collections import deque

def bfs(start, end, node, graph):
    
    queue = deque([start])

    visited = [ 0 for _ in range(node+1)]

    visited[start]= 0

    while queue:

        _node = queue.popleft()

        if _node == end :

            print(visited[_node])

            return 0

        for n_node in graph[_node]:

            if n_node < 0 or n_node > node: continue

            if visited[n_node] == 0 :

                queue.append(n_node)
                visited[n_node] = visited[_node] + 1
             
              
    print(-1)





def solution():
    
    s, e = map(int, input().split())

    node, edge = map(int , input().split())

    graph= {}

    for idx in range(node):

        graph[idx+1] = []


    for _ in range(edge):

        _s, _e = map(int, input().split())

        graph[_s].append(_e)
        graph[_e].append(_s)

    bfs(s,e, node, graph)

        


solution()
