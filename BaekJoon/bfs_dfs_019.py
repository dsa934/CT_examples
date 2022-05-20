
'''

 Backjoon _ exampels 1679

  " 숫자 놀이 "   by Jinwoo Lee

  < algorithm >

  1. 주어진 숫자 조합 집합 numbers 에서 최대 k번 뽑아서 만들어지는 수를 bfs/dfs 통해 구하기

   => max(numbers) * k 값을 넘지 못함 , 방문 노드에 max_value가 있다면 while break 

   => 한 시작 숫자에 대해 n개의 갈림길이 생기는것과 같으니 bfs가 적합

  * 만들지 못하는 숫자 찾으면 break 시켜야 하는데 안시켜서 첫시도 틀림


  * 1을 반드시 포함해야 한다해서, 시작노드가 1부터인줄 착각함


 

'''

from collections import deque


def bfs(max_value, visited, numbers):

    queue = deque([0])

    visited.append(0)


    while queue:

        if max_value in visited:
            break

        _node = queue.popleft()

        for value in numbers:

            n_node = _node + value

            if n_node not in visited:

                visited.append(n_node)

                queue.append(n_node)



def solution():
    
    num = int(input())

    numbers = list(map(int, input().split()))

    n_max = int(input())

    max_value =  max(numbers) * (n_max)


    visited = [] 


    bfs(max_value, visited, numbers)

    
    visited = sorted(visited)
    
    ans = max_value +1 

    for idx, value in enumerate(visited):
        
        if idx != value :


            ans = idx
            break

    return f'holsoon win at {ans}' if ans % 2 == 0 else f'jjaksoon win at {ans}'




print( solution() )