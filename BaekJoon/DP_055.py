
'''

 Backjoon _ exampels 1793

  "Ÿ�ϸ�"   by Jinwoo Lee

  < algorithm >

  1. dp[idx] = dp[idx-2] * 2 + dp[idx-1]

  2. ���� ������ ���� �Է� ���� : try ~ except ��� 

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