

'''

 Backjoon _ exampels 1835

  "Ä«µå"   by Jinwoo Lee

  < algorithm >

  1. 
 

'''


from collections import deque

def solution():

    num = int((input()))
    queue = deque([num])

    for n_value in range(num-1, 0, -1):

        queue.appendleft((n_value))
 
        for _ in range(n_value):

            queue.appendleft(queue.pop() )

    print(*queue)

solution()