
'''

 Backjoon _ exampels 9655

  "�� ����"   by Jinwoo Lee

  < algorithm >

  1. ���� idx �� true /false �̸� ���� �ݴ�� ���� 


 

'''



def solution():

    num = int(input())

    dp = [ [ False for _ in range(num+1) ] for _ in range(2) ]

    dp[0][1] = True



    if num >=2 :

        for idx in range(2,num+1):


            if not dp[0][idx-1] : dp[0][idx] = True
            
            if not dp[1][idx-1] : dp[1][idx] = True

            
    if dp[0][num] : return 'SK'

    elif dp[1][num] : return 'CY'


print( solution() )