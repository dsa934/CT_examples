

'''

 Backjoon _ exampels 18232

  ""   by Jinwoo Lee

  < algorithm >

  
  1. start 기준으로 이동할 수 있는 영역은 [ -1, 1, 텔포정류장1, 텔포정류장2 ... ]

     =>  -1, 1과 텔포 정류장으로 연결된 1은 다르기 떄문에 이를 구별하기 위한 cnt 필요 

     =>  -1, 1 의 경우 n_node = _node + path 

         텔포 정류장의 1인 경우  n_node = path 



  2. vistied array 를 0으로 set, 이동시 +1 증가 



  * 텔레포트 정류장은 양방향 연결이다, 관계 그래프 형성시 양방향으로 set 




  * python 제출 시 TLE, pypy3 제출시 통과

    => 이유 아직 못찾음 


 

'''


from collections import deque 


def bfs(start, end, graph, node):
    
    queue = deque([start])
    
    visited = [ 0 for _ in range(node+1) ]


    while queue :

        _node = queue.popleft()
        
        #print("node & graph", _node, graph[_node])
        
        cnt = 0 

        for path in graph[_node]:

            if cnt == 0 or cnt == 1:

                n_node = _node + path

                cnt+=1

            else:

                n_node = path
            
            
            if n_node <= 0 or n_node > node :
                continue

            if visited[n_node] == 0 :

                queue.append(n_node)
                visited[n_node] = visited[_node] + 1

                
    return visited[end]




def solution():

    node, edge = list(map(int , input().split()))

    start, end = list(map(int ,input().split()))

    graph = {}

    for idx in range(1, node+1):

        graph[idx] = [-1, 1]


    for _ in range(1,edge+1):

        node_s, node_e = list(map(int , input().split()))

        graph[node_s].append( node_e )
        graph[node_e].append(node_s)

    
    ans = bfs(start, end, graph, node)

    return ans


print( solution() )


