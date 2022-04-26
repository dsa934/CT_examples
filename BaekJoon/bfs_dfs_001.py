
'''

 Backjoon _ exampels 1260

  " dfs & bfs "   by Jinwoo Lee

 < bfs / dfs 실 문제 적용 알고리즘 >

 1. 문제의 정보를 통해 연결 관계를 나타내는 graph 구성 

    graph =  [ 
               [], 
               [2,3,8],
               [4,5,6],
               ...
             ] 

    * graph 관계 구현 시 방향 / 무방향 graph 체크 필요 
   
      -> 양방향일 경우  (vertex 1,4 가 연결되있다면 )  =>   1: [4]  , 4: [1]

    * dict 자료형 요소 추가(append) 하기 

      - dict을 list로 초기화 하면 append 기능 활성화 가능 



 2. 방문한 node 집합 set을 구성 

 3. bfs / dfs 방법론에 따른 queue / stack 사용 


'''

def make_graph():

    n_vertex, n_edge, start_point = list(map(int, input().split()))

    graph = {}

    for idx in range(1,n_vertex+1):

        graph[idx]=[]

    
    for _ in range(n_edge):

        _vertex, _edge = list(map(int , input().split()))

        graph[_vertex].append(_edge)
        graph[_edge].append(_vertex)

    return graph, start_point



def graph_sort(graph):

    for idx,value in enumerate(graph.values()):

        graph[idx+1] = sorted(value)

    return graph


def graph_reverse(graph):

    for idx,value in enumerate(graph.values()):

        graph[idx+1] = sorted(value, reverse = True)

    return graph


def dfs(graph, start):

    result, stack = [], []
    dfs_visited = set()

    stack.append(start)
    
    while stack:

        _node = stack.pop()
  
        if _node not in dfs_visited:

            dfs_visited.add(_node)

            stack.extend(graph[_node])

            result.append(_node)

    return result


def bfs(graph, start):

    result, queue = [], []
    bfs_visited = set()

    queue.append(start)

    while queue:

        _node = queue.pop(0)

        if _node not in bfs_visited:

            bfs_visited.add(_node)
            result.append(_node)

            queue.extend(graph[_node])


    return result






# graph를 통한 vertex 간 관계 구성
info_graph, s_point = make_graph()

# dfs
r_graph = graph_reverse(info_graph)
dfs_result = dfs(r_graph ,s_point)

# bfs
s_graph = graph_sort(info_graph)
bfs_result = bfs(s_graph, s_point)


for value in dfs_result:

    print(value, end=" ")

print()

for value in bfs_result:

    print(value, end=" ")

print()