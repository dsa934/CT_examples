

'''

 Backjoon _ exampels 11725

  "트리 부모 찾기"   by Jinwoo Lee

  < algorithm >

  1. BFS를 이용하여,  큐로부터 부모 노드에 해당하는 _node를 추출

  2. graph[_node]를 통해 부모 노드와 연결 된 자식 노드 정보를 얻고, 

     각각의 자식 노드가 부모 노드가 없다면 ( ans[value] == 0 ) 부모를 설정 

     for value in graph[_node[]:

        if ans[value] == 0 : 

           ans[value] = _node


  3. 루트 노드에 해당하는 1번 노드 제외하고, 2 ~ N 까지의 부모 노드 출력 
 

'''


from collections import deque

def bfs(boundary, graph):
    

    root_node = 1 

    queue = deque([root_node])

    visited = [ False for _ in range(boundary+1)]
    visited[1] = True

    ans = {} 

    for idx in range(1, boundary+1):

        ans[idx] = 0
 
    while queue :
        

        _node = queue.popleft()

        for value in graph[_node] :
            

            if ans[value] == 0 :

                ans[value] = _node
          

            if not visited[value] :

                queue.append(value)

                visited[value] = True


    for idx,value in ans.items():

        if idx == 1 :
            continue

        print(value)


def solution():

    num = int(input())

    graph = {}

    for idx in range(1, num+1):

        graph[idx] = [] 


    for _ in range(2,num+1):

        start, end = list(map(int, input().split()))

        graph[start].append(end)
        graph[end].append(start)

    bfs(num, graph)



solution()