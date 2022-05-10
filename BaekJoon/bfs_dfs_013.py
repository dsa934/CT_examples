
'''

 Backjoon _ exampels 11742

  "연결 요소의 개수"   by Jinwoo Lee

  < algorithm >

  1. 각 vertex에 대한 연결 지점 확인을 위해 BFS 알고리즘 적용 

  2. BFS를 적용하는 기준은 현재까지 방문하지 않은 vertex를 기준으로 한다

  3. 방문되지 않은 vertex를 만났을 경우, result+=1 을 통해 연결지점의 수를 확보한다.



  * 해당 알고리즘으로 python 에서는 TLE, pypy 에서는 통과가 뜬다 그 이유는 ?

    => python에서 TLE ,pypy에서 통과가 되는 경우는 대게 알고리즘의 문제가 아닌 입력값이 많은 경우이다.

       이 경우 sys 라이브러리를 통한 readlines 사용시 해결되는데, 코테에서는 권장되는 방법이 아니다

       따라서, 알고리즘이 완벽하다고 생각된다면 pypy로 제출해보고, 제출 후 통과가 된다면 알고리즘 자체에 문제가 없는지에 대한 판별로만 사용하자

       해당 문제에 대한 구체적인 해결법은 없는 것 같다.

 

'''


from collections import deque

def solution():

    vertex, edge = list(map(int , input().split()))

    graph = {}

    for idx in range(1, vertex+1):

        graph[idx] = []


    for _ in range(edge):

        _start, _destination = list(map(int, input().split()))

        graph[_start].append(_destination)
        graph[_destination].append(_start)



    visited =[]

    result = 0

    queue = deque()


    for pos in range(1, vertex+1):

        if pos not in visited :

            visited.append(pos)

            queue.extend(graph[pos])

            result +=1 

            while queue:

                _vertex = queue.popleft()

                if _vertex not in visited:

                    visited.append(_vertex)

                    queue.extend(graph[_vertex])

    return result




print( solution() )

