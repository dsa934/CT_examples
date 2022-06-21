
'''

 Backjoon _ exampels 1788

  "피보나치 수의 확장 "   by Jinwoo Lee

  < algorithm >

  1. 피보나치를 음의 방향으로 확장할 경우 

     -10  -9  -8   -7   -6  -5   -4  -3  -2  -1  0  1  2  3  4  5  6   7   8   9   10

     -55  34  -21  13   -8   5   -3   2  -1   1  0  1  1  2  3  5  8   13  21  34   55 

     => 음의 방향에서는 부호가 지속적으로 변하는 것을 확인 할 수 있다

     
     1) 양수의 경우 

        dp[idx] = dp[idx-1] + dp[idx-2]


     2) 음수의 경우 

       => dp[idx], dp[idx-1] 값을 알고 dp[idx-2]를 모르는 상황 임으로 

       dp[idx-2] = dp[idx] - dp[idx-1] 


       하지만 음수이기 때문에 dp[idx-2]가 오히려 미래 시점이 되어버린다. ( dp[idx-2]를 모르고 dp[idx], dp[idx-1]을 아는 상황에 대한 이유 )

       dp[idx-2] <=> dp[idx]의 교환이 이루어져야 한다 

       ∴ value = dp[idx-2] - dp[idx-1]


 
  * 1e10 : 10, 000, 000, 000 

    => e 뒤에는 0의 개수를 의미함 혼동하지 말것 

    => 문제에서 1,000,000,000 (10억)을 요구했는데 100억으로 해서 틀림 



'''


def solution():

    num = int(input())

    mode = int(1e9)
    
    _type = 0 
    dp = [0, 1]

    if num != 0 and num > 1:
        
        for idx in range(2, num+1):

            value = (dp[idx-1] + dp[idx-2]) % mode 

            dp.append(value)


    elif num != 0 and num < -1 :
        
        for idx in range(2, abs(num)+1):

            value = dp[idx-2] - dp[idx-1]


            if value < 0 :
                
                value %= -mode


            elif value > 0 :

                value %= mode

            dp.append(value)
    
    

    if dp[abs(num)] > 0 :
        _type = 1

    elif dp[abs(num)] < 0 :
        _type = -1

    print(dp)
    print(_type)
    print(abs(dp[abs(num)]))

solution()