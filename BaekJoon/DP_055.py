
'''

 Backjoon _ exampels 1793

  "타일링"   by Jinwoo Lee

  < algorithm >

  1. dp[idx] = dp[idx-2] * 2 + dp[idx-1]

  2. 종료 조건이 없는 입력 문제 : try ~ except 사용 

     try : 

           code 

     except :

           break 


 

'''


def solution():


    while True:


        try : 
            num = int(input())

            dp = [1,1]

            if num > 1:

                for idx in range(2, num+1):

                    value = dp[idx-2]*2 +dp[idx-1]

                    dp.append(value)

            print(dp[num])
        except:
            break



solution()