
'''

 Backjoon _ exampels 9657

  "돌 게임 3"   by Jinwoo Lee

  < algorithm >
 
  1. 해당 게임은 마지막에 돌을 가져가는 플레이어가 승리하는 구조 

     * 돌을 1, 3, 4 개 가져 갈 수 있다



  2. N에 대하여 N-1, N-3, N-4 의 경우의 수가 있다.


     * 1 <= N <= 4 일 경우, init value를 통해 답을 도출

     * N >= 5인 경우, prev_value = [ N-1, N-3, N-4 ] 를 계산해도 돌의 개수가 0이 되지 않는다

       즉,  prev_value 중에 한번이라도 'CY'가 있으면 (상대턴이면) 남은 돌은 'SK'가 가져 오기 떄문에 승리한다




  * 완벽하게 게임한다 => 이길 수 있는 수단이 있다면 무조건 그 수만 놓는다 ( 최적의 수만 놓는다 )

'''

def solution():

    num = int(input())

    dp = [0, 'SK', 'CY', 'SK', 'SK']

    if num > 4:

        for idx in range(5, num+1):

            if 'CY' in [ dp[idx-1], dp[idx-3], dp[idx-4] ] :

                dp.append('SK')

            else:
                dp.append('CY')
    return dp[num]


print( solution() )