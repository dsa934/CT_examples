
'''

 Backjoon _ exampels 14562

  "태권왕 - 중앙대학교 "   by Jinwoo Lee

  < algorithm >

  0. 이동 가능 루트 = [ *2 , +1] , but 목적지가 *2 사용시 변한다는 점이 기존 bfs 문제들과 차이점

    => visited & graph node 구성에 dictionary 사용  :  목적지가 변하면, 정적 크기를 지정할 수 없기 때문에 

    => 하지만 이 방법은 4%에서 실패 하였음 (반례를 아직 찾지 못함 )



  1. bfs에서 queue에 넣는 contents는 보통 변하는것( 좌표 ) 지만, 목적지와 count가 같이 변하기 떄문에 
  
    queue = deque([ [ start, end, cnt] ]) 와 같이 한번에 묶어주는 것도 좋은 방법 


  2. 중복된 수의 대한 처리가 없으나, 통상적으로 중복된 수 n이 있다면,  +1 보단 *2 가 n에 빠르게 도달할 것임으로 ( 도달하지 못한 경우는 고려 x)

     따로 중복 처리를 하지 않아도 된다


 
  * deque() 는 scalar element 라도 넣을떄 [] 형태로 넣어 주어야 한다.

    따라서 list를 초기값으로 지정할 경우에는 

    queue = deque( [  ] )   이 안에 리스트를 넣어야 한다

    queue = deque( [ [a,b,c]  ] )  =>  [ a,b,c ]

    if queue = deque( [ a,b,c ]) =>  a,b,c



'''

from collections import deque


def bfs(start, end):
    
    cnt = 0 

    queue = deque([ [start, end, cnt ] ])

    while queue:
        
        s_node, e_node, _cnt = queue.popleft()

        if s_node < e_node :

            queue.append([s_node*2, e_node+3, _cnt+1])
            queue.append([s_node+1, e_node, _cnt+1])

        if s_node == e_node :

            return _cnt
        

def solution():
    
    num = int(input())

    for _ in range(num):

        s, e = list(map(int , input().split()))
        
        ans = bfs(s,e)

        print(ans)

solution()


'''
* 최초 틀렸을떄 bfs 코드 

def bfs(start, end):
    
    
    queue = deque([start])

    visited = [start] 

    
    graph, path = {}, {}

    graph[start], path[start] = end, 0
    
    while queue:

        _node = queue.popleft()
        
        if _node == graph[_node]:

            return path[_node]

        dx = [ _node , 1]
        
        for value in dx:

            n_node = _node + value
            
            if n_node < 0 or n_node > graph[_node]+3 :
                continue

            if n_node not in visited:

                visited.append(n_node)
                queue.append(n_node)
                path[n_node] = path[_node]+1

                if value != 1 :

                    graph[n_node] = graph[_node] +3

                else:
                    graph[n_node] = graph[_node]
        


'''
