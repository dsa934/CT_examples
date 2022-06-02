
'''

 Backjoon _ exampels 24444

  "알고리즘 수업 - 너비 우선 탐색 1 "   by Jinwoo Lee

  < algorithm >

  1. python 제출시 TLE, pypy3  제출시 통과 

    => python으로 패스한 친구들은 sys library 사용한듯 -> 되도록 코테 연습용이라 안쓰는게 좋음 


  < 해당 문제를 풀면서 알게 된 clean code 요소 들 >

  1. 인접 list를 통한 graph 형성 시

     dictionary 형태도 좋지만 graph = [  []  for _ in range(node+1) ]  형태도 가능

     => dict을 쓸 경우 fo문을 따로 써서 초기화 but 위의 방식은 list 내포로 깔끔하게 가능 (초기화 관점에서)



  2. visited 를 True/False 가 아닌 count 로 사용하기

     if visited[value] == 0  then cnt+=1 , visited[value] = cnt 


 

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

        value.sort()
        
    answer = bfs(node, start, graph)

    for idx in range(1,node+1):
        print(answer[idx])

solution()
