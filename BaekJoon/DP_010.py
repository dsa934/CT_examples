
'''

 Backjoon _ exampels 2156

  "포도주 시식 "   by Jinwoo Lee

  < algorithm >

  * 계단 오르기 문제와 비슷 ( 연속해서 3잔을 마실 수 없다는 조건 )


  1. 최대 섭취량 (dp) , 각 n번째 포도주 병의 섭취량 (info )이 주어진다.


  2. dp[num] = max( dp[num-3] + info[num-1] + info[num] , dp[num-2] + info[num] )

    a) dp[num-3] + info[num-1] + info[num]     : num-3 번째와, num-1로 한칸을 뛰고, num 번쨰 포도주병을 선택하는 경우 (1,3,4)
     
    b) dp[num-2] + info[num]                   : num-2번쨰와 num 번째의 포도주병을 선택 하는 경우                     (2, 4)


    
    => 2가지 방법 모두, 연속으로 3잔을 마시는 경우의 수를 피하기 위해 고려 되어짐 

    * 계단 오르기 문제의 경우, 이동 방법론 = { 2칸, 1칸 } 의 2가지 방식 밖에 없었기 때문에 위  2가지 사항만 고려했지만,

      이 문제에서는 한가지 사항을 더 고려해야 한다.

     ★ dp[num-1]                               : num에 해당하는 잔을 마시지 않았을 경우

    

    => a), b)의 경우 모두 num 칸이 선택 되었을떄의 경우의 수를 계산한다.
     
       ★의 경우,  bottom_up 방식으로 memoization를 사용하여 구현되었음으로, '연속되는 3잔을 마실 수 없다' 라는 규칙에 의거하여 
       
       dp_table이 잘 형성 된 경우, dp[num-1]이 갖는 의미는 

       ' 연속된 3잔을 마시지 않으면서 num-1번째 와인을 마셨을때의 최대값'이 되며 

        ★ 까지 고려하는 이유는 dp[num]을 a), b)에 의해 계산하는 경우의 수에서 num-1 번쨰 와인이 선택되지 않을 수 있는데
        
        num-1 번쨰 와인이 선택되지 않은 경우의 수가 num 번쨰 와인을 선택하는 경우의 수 보다 클 가능성이 있기 떄문이다.


       
       


 
'''

def solution():

    num_wine = int(input())

    info = [0]
    
    for _ in range(num_wine):

        info.append(int(input()))


    dp_table = [0]

    if num_wine >= 1:

        dp_table.append(info[1])

    if num_wine >= 2 :

        dp_table.append(info[2]+info[1])



    for idx in range(3,num_wine+1):

        target_before_one_step = dp_table[idx-3] + info[idx-1] + info[idx]

        target_before_two_step = dp_table[idx-2] + info[idx]

        dp_table.append(   max( target_before_one_step , target_before_two_step, dp_table[idx-1]) )

    #print(dp_table)
    return max(dp_table)


print( solution() )
