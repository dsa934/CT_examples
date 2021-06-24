'''

 Backjoon _ exampels #

  "Baek 2468 - 안전영역(BF - DFS/BFS) "   by Jinwoo Lee


 # Algorithm 

  0. 높이정보가 주어지면 안전지대의 개수를 출력하는 프로그램 

  1. DFS를 사용하여 문제를 해결할 수 있을 것 같다.

  2. 현 위치에서 내가 갈수있는 모든 연결된 위치를 가봄 -> DFS 특성 ( BFS는 최단경로)

  3. 높이가 1~100 으로 주어지기 떄문에 방문가능한 노드를 0 , 방문한노드 'v', 방문불가노드 'x'

  4. 강수량이 주워지지 않는 문제이기 때문에 region 만들떄 0~ max(지형높이) 까지 다 해봐야한다.

  

 # Attention for Implementation

  - 이 문제에서 잘못 이해한 점 ->  최대 안전지역을 구하는 것인데 강수량이 정해지지 않았다 -> 강수량을 0 ~ max(지형높이) 까지 해야함 

  - 2차원 이상 배열에서 max값 한번에 구하기 -> max_value = max(map(max,array))

  - dfs를 여러번 하는것이기 떄문에 region 초기화를 위해 real_region / region을 나눠야 한다.


  - ★ 객체복사 Mutable(list, set, dict) / Immutable (bool, int, float, tuple, str, fronzenset)

    * int 자료형 : Immutable  a=1, b=a, b=2 해도 a값은 변하지 않음 => 자료형의 특성떄문

    * list 자료형 : Mutable, 따라서 위와같이하면 형태가 변함 ( a,b가 같은 주소값을 가지기 떄문)

    * 얕은복사(Shallow Copy) : 원본 객체의 주소값 복사 -> 원본이 같이 바뀜

    * 깊은복사(Deep Copy) : 전체 복사, 참조된 객체 자체를 복사 -> 원본 배열을 보존하고 싶을때 사용

      => 2차원 이상의 배열 사용시 list.copy() , copy module의 copy() 함수의 경우 내부 객체까지 완전한 깊은복사가 이루어지지 않기 떄문에

      => copy module의 deepcopy를 사용해야함 

      

'''
import copy 
import sys
sys.setrecursionlimit(100000)

def dfs(row,col):
    
    # Range check
    if row < 0 or col <0 or row > height-1 or col > height -1 : return False

    if field[row][col] == 0 : 

        field[row][col] = 'v'

        # retun value 있지만 사용하지않고, 방문가능한노드만 탐방 
        dfs(row+1,col)
        dfs(row-1,col)
        dfs(row,col+1)
        dfs(row,col-1)

        return True

    return False

height = int(input())

region = [list(map(int ,input().split())) for _ in range(height)]

result = []

rain = 0

while rain < max(map(max,region))+1:

    # 강수량에 따라 field가 바뀜 
    field = copy.deepcopy(region)

    cnt = 0

    for i in range(height):

        for j in range(height):

            if field[i][j] <= rain : field[i][j] = 'x'
            else : field[i][j] = 0



    for i in range(height):

        for j in range(height):

            if dfs(i,j) : cnt+=1

    result.append(cnt)
    rain +=1

print(max(result))
