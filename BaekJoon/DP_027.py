
'''

 Backjoon _ exampels 13301

  "Ÿ�� ��Ĺ�"   by Jinwoo Lee

  < algorithm >

  1. �� Ÿ���� ����  1, 1, 2, 3, 5, 8 

     => dp[idx] = dp[idx-2] + dp[idx-1] 


  2. ���簢�� ���� 

    =>  dp[num] + dp[num]  + dp[num+1] + dp[num+1]
 

  3. num�� ��, num+1 �� �ʿ��ϱ� ������ 

    if num >= 6 then  for idx in range( 7 ,  num +2  )   // num+2 ���� �����ؾ� num, num+1 ���� �������

'''

def solution():
    
    num = int(input())

    dp = [0,1,1,2,3,5,8]

    if num >= 6:

        for idx in range(7, num+2):

            value = dp[idx-1] + dp[idx-2]

            dp.append(value)

    return (2* dp[num] + 2* dp[num+1])





print( solution() )