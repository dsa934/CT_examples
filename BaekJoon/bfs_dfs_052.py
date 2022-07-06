

'''

 Backjoon _ exampels 13700

  "���� ����"   by Jinwoo Lee

  < algorithm >

  1. �⺻���� bfs ����

  * �� k = 0 �� ��� police list�� �Է¹��� �ʱ� ������ EOF ������ �������

    => k�� 0�϶� ������ֱ� 

 

'''



from collections import deque

def bfs(n,s,d,f,b,k, police):


    visited = [ 0 for _ in range(n+1)]

    queue = deque([s])

    visited[s] = 0
    
    drow = [ f, -b ]

    while queue :

        _pos = queue.popleft()

        for idx in range(2):

            n_pos = _pos + drow[idx]

            if n_pos < 0 or n_pos > n : continue

            if n_pos in police: continue

            if visited[n_pos] == 0 :

                queue.append(n_pos)
                visited[n_pos] = visited[_pos] + 1

    if visited[d] != 0 :
        print(visited[d])

    else:
        print('BUG FOUND')

def solution():

    n, s, d, f, b, k = map(int, input().split())

    if k != 0 :
        police = list(map(int, input().split()))
    else:
        police = [] 

    bfs(n,s,d,f,b,k, police)
    

solution()