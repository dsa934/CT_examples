
'''

 Backjoon _ exampels 2579

  "계단 오르기"   by Jinwoo Lee

  < algorithm >
 
  1. N > 3 ,  F(N) = max ( F_cost[N-3] + F_stairs[n-1] + F_Stairs[n] , F_cost[N-2] + F_stairs[n])

  2. ' 연속해서 3개의 계단을 오를 수 없음' 의 조건에 의하여,  현재 위치를 t라고 할때

      a)  t-2 + 2 step up                => 2칸 아래에서 한번에 2칸으로 t 도착

      b)  t-3 + 2 step up + 1 step up    => 3칸 아래에서 바로 전칸 t-1까지 도착 후 1칸 이동하여 t 도착 


  3. 초기값 설정

     a) 0층  : 비용 없음, 0 

     b) 1층  : 한칸으로만 가능, info_stair[1]

     c) 2층  : 2칸 한번에 or 1칸씩 두번 , max( info_stairs[2], info_stairs[1] + info_stairs[2] )


     * 누적 비용 table 을 dp로 구성,  계단 정보는 참고배열로써 활용 ( 값 변화 x )
     
       a)  'RGB 거리' 문제와 다르게 info_table에 직접 누적하지 못하는 이유

           =>  공통점 : 현재에서 과거의 정보를 활용하여 문제 풀이 ( T번쨰 집에서 t-1 번쨰 집 정보 활용 ) 

               차이점 :  '연속으로 진행되지 않음 (3칸 연속 밟지 못함 )'

                          t층에 도달하기 위해 활용하는 정보가 과거임은 동일하지만,  비교하는 과거 시점( t-2, T-3 )이 달라지기 떄문에 추가 TABLE 필요 
               





  cf. DP 문제 풀이시 방법이 생각나지 않는다면,

    * 앞으로 가야하는 ' 미래 ' 로 생각하지 말고, 지나온 '과거'로 생각하기 

      계단을 몇개 올라가야 하는가?  =>  몇 계단전에서 출발 했는가 ?






'''

def climbing_stairs():

    num_stairs = int(input())

    info_stairs = [0]

    for _ in range(num_stairs):

        info_stairs.append(int(input()))
    
    if num_stairs == 1: 
        
        return info_stairs[-1]


    cost = [0, info_stairs[1] ,  max ( info_stairs[2], info_stairs[1] + info_stairs[2] ) ]  
    
    if num_stairs > 3:
        
        for idx in range(3, num_stairs+1):
            
            _cost = max ( cost[idx-3] + info_stairs[idx-1] + info_stairs[idx] , cost[idx-2] + info_stairs[idx] )

            cost.append(_cost)


    return cost[num_stairs]


print ( climbing_stairs() )

    


    
