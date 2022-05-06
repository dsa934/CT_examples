
'''

 Backjoon _ exampels 1932

  "정수 삼각형"   by Jinwoo Lee

  < algorithm >

  0. 최소/최대 비용 문제 풀때 생각할 점 

    * Greedy가 최적해 보장 X 

      => DP 활용, How ?


         * 현재 시점을 기준으로, 한단계 이전 시점을 고려,  cost = current_cost + max or min ( prev_cost )

         => greedy가 최적해를 보장하지 않는 단점을 해결 할 solution 


    * dfs/bfs와의 차이 

      => dfs/bfs의 경우, 경우의 수가 N가지일 경우 적합하지 않은 풀이가 된다 ( 최단 경로 okay,  최소비용 경로 Not perfectly okay ) 

         최초로 도착했다면 ( not in visited,  value[_x][_y] == 0 , etc.. ) , 해당 위치 값을 선점하여 표기 하면 문제가 해결되는 경우가 많기 때문

         [_x][_y] 위치에 가장 빨리 도달했어도 그 길이  weight 떄문에 최소비용의 길이 아닐 수 있음 




   1. 관계식 찾기 
 
      first element :=  F[raw, 0] +=  F[raw-1, col]                       => a

      others :=  F[raw, n] += max ( F[raw-1, n] , F[raw-1, n-1] )         => b


      a) 삼각형 모양, 하위 원소는 left/right diagonal element만 사용 가능한 조건임으로 

         [raw][first_column] 은 [raw-1][first_column] 만 사용 가능


      b) 삼각형 모양이기 떄문에, [raw][-1] 의 경우 [raw][column-1] 만 사용가능 했으나, 

         입력값으로 이루어진 field를  zero padding을 통해 정사각형 형태로 만들어 관계식 통일 



'''


def int_triangle():

    num_floor = int(input())
    
    field = [list(map(int , input().split())) for _ in range(num_floor)]


    for raw_idx in range(num_floor):

        if len(field[raw_idx]) != num_floor:

            for _ in range( num_floor -len(field[raw_idx]) ):
                
                field[raw_idx].append(0)


    
    for raw_idx in range(1,num_floor):

        for col_idx in range(num_floor):

            if col_idx == 0 :

                field[raw_idx][col_idx] += field[raw_idx-1][col_idx]

            else:

                field[raw_idx][col_idx] += max( field[raw_idx-1][col_idx] , field[raw_idx-1][col_idx-1])

    
    return max(field[-1])



print(int_triangle())

