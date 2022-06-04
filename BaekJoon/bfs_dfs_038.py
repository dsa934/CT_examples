
'''

 Backjoon _ exampels 18126

  "�ʱ��� ���� (���縯�� p��ȸ)"   by Jinwoo Lee

  < algorithm >

  1. 4���� ������ �ʿ�

   1) ���� ���踦 ��Ÿ���� graph

   2) �湮 ���θ� ��Ÿ���� visited
   
   3) ���� ��庰 ����ġ�� weight 

   4) ������ ���� �� weight ���� ������ set_score



  * ���� ��ġ 1����, ���� �� ���� �־��� num�� �ƴ϶�, weight_sum�� ���� ū ���� ����ϴ°� (ù �õ��� �̰� ���� )
 

'''


from collections import deque 


def bfs(graph, score, num):

    queue = deque([1])

    visited = [ False for _ in range(num+1) ]

    set_score = [  0 for _ in range(num+1) ]

    visited[1] = True


    ans = 0 


    while queue:

        _node = queue.popleft()

        for value in graph[_node]:

            if not visited[value] :

                queue.append(value)
                visited[value] = True

                set_score[value] = set_score[_node] + score[_node][value]


    return max(set_score)







def solution():

    num = int(input())

    graph = [ [] for _ in range(num+1) ]

    score = [ [0 for _ in range(num+1)] for _ in range(num+1) ]

    
    for _ in range(num-1):

        start, end, weight  = map(int, input().split())

        graph[start].append(end)
        graph[end].append(start)

        score[start][end] = weight
        score[end][start] = weight


    print(  bfs(graph, score, num)  )

solution()



