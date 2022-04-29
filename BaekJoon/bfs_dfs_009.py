
'''

 Backjoon _ exampels 9205

  "맥주 마시면서 걸어가기 "   by Jinwoo Lee


  < 알고리즘 >

  1. 최단 거리 BFS 알고리즘의 응용 문제 

     * 시작점 부터 도착 지점까지 '어떠한 지점을 경유해서' 이동

     * 도착점 까지의 최단 경로가 아닌, '도착이 가능한지' 가  핵심


  2. 상하좌우 이동을 +- 50 씩 일일히 구현하는 것이 아니라 

    '중간 경유지인 편의점'을 거리조건에 의해 (맥주 20명 , 1000 이하) queue에 넣을 수 있는지 없는지에 대하여 BFS 적용 



'''


from collections import deque

def input_data():

    num_store = int(input())

    start_x, start_y = list(map(int, input().split()))

    store = [list(map(int ,input().split())) for _ in range(num_store)]

    destination_x, destination_y = list(map(int , input().split()))



    return start_x, start_y, destination_x, destination_y, store 




def dfs(start_x, start_y, destination_x, destination_y, store):

    queue = deque()

    visited = []


    visited.append([start_x, start_y])

    queue.append([start_x, start_y])


    while queue:

        _x , _y = queue.popleft()


        if abs(_x - destination_x) + abs(_y - destination_y) <= 1000:

            return "happy"

        for idx in range(len(store)):

            n_x , n_y = store[idx]

            if [n_x, n_y] not in visited:
                
                if abs(n_x - _x) + abs(n_y - _y) <= 1000:

                    queue.append([n_x, n_y])
                    visited.append([n_x, n_y])

    return "sad"






num_test = int(input())

for _ in range(num_test):

    s_x, s_y, d_x, d_y, store = input_data()


    print(dfs(s_x, s_y, d_x, d_y, store))
