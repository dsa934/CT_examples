

'''

 Backjoon _ exampels 2606

  " 바이러스  "   by Jinwoo Lee


 < bfs / dfs 실 문제 적용 알고리즘 >

 1. 문제 정보를 토대로 컴퓨터 간 연결관계 graph 형성

 2. 시작번호가 1번 고정임으로 1번을 통해 dfs 구현 후 visited 의 수가 몇인지 출력하기 

 3. 1번 컴퓨터가 감염 됬을떄, 몇개의 컴퓨터가 감염인지 찾아야 함으로 len(visited)-1 


'''

def make_graph():

    n_com = int(input())

    connect = int(input())

    graph = {}

    for idx in range(1,n_com+1):

        graph[idx] = []



    for _ in range(connect):

        _node, _edge = list(map(int , input().split()))

        graph[_node].append(_edge)
        graph[_edge].append(_node)


    return graph


def dfs(graph, start):

    visited = set()
    stack = []

    stack.append(start)
    
    while stack:

        _node = stack.pop()

        if _node not in visited:

            visited.add(_node)

            stack.extend(graph[_node])



    return len(visited)-1




info_connect = make_graph()

result = dfs(info_connect,1)

print(result)




