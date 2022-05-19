
'''

 Backjoon _ exampels 1240

  "�������� �Ÿ� "   by Jinwoo Lee

  < algorithm >
 
  1. graph / tree �������� �� �������� �Ÿ��� ���ϴ� �������� 3���� + bfs/dfs �˰��� �ʿ�  

  * ���� �׷��� 

    => �� node ���� ���� ���踦 ǥ�� ( �����, �ܹ����� ������ �°� ���� )


  * score dict 

    => socre[child_node] = score[parent_node] + weight_Table[parent][child]

      score[parent_node]�� bfs/dfs Ž�� ��������, child_node �������� �󸶸�ŭ�� ���(������ ��) �� ��������� ���� ���� ��

      bfs/dfs �˰��� ���� parent, child�� ���÷� ��ȭ �� 


    => wieght_table ��� + 1 �� �� ��� '�̼� ���' ���� 

 
  * weight table ( ���� ���� )

    => '�̼� ���' ������ ��� node�� ���� node ���� ������ ũ�Ⱑ 1�� �����̱� ������ ������ ����

       but '��� ������ �Ÿ�' ���������� �� ��庰 ������ ũ�Ⱑ �ٸ��� ������, �� ����� ��庰 ������ ũ�⸦ ��Ÿ�� �� weight table �ʿ� ( 2���� )


'''


from collections import deque

def bfs(start, end, graph, n , weight):

    visited =  [ False for _ in range(n+1) ]

    queue = deque([start])

    visited[start] = True


    score = {} 
    
    for idx in range(1,n+1):
        
        score[idx] = 0
        

    while queue : 

        _node = queue.popleft()
        
        for n_node in graph[_node]:

            if not visited[n_node] : 

                queue.append(n_node)
                visited[n_node] = True
                
                score[n_node] = score[_node] +  weight[_node][n_node]


    return score[end]



def solution():
    
    n, m = list(map(int , input().split()))

    graph = {}
    weight = [[ 0 for _ in range(n+1) ] for _ in range(n+1) ]

    for idx in range(1,n+1):

        graph[idx] = []
        


    for _ in range(n-1):

        s, e, w = list(map(int, input().split()))

        graph[s].append(e)
        graph[e].append(s)

        weight[s][e] = w
        weight[e][s] = w

    ans = [] 

    for _ in range(m):

        start, end = list(map(int, input().split()))

        ans.append( bfs(start, end, graph, n , weight))


    for value in ans:
        print(value)


solution()