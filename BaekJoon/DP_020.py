
'''

 Backjoon _ exampels 1309

  "������"   by Jinwoo Lee

  < algorithm >

  1. dp[idx] = dp[idx-2] + dp[idx-1] + dp[idx-1]


  < n condition >   <0����> <1���� > ... < n���� >

    n = 1   then ,   1         2                        = 3

    n = 2   then ,   1         4        2               = 7  

    n = 3   then ,   1         6        8        2      = 17  ( 3 + 7 + 7 )



  * dp ���������� ��ȭ�� ������ ���� n = 3���� , n =1,2 ���� �̿��Ͽ� ��Ÿ���� ������ ������ �ϴ�. ( dp ������ ī�װ�ȭ�� ���� db �״��� 2022/5/15)


'''

def solution():

    num = int(input())

    dp = [0,3,7]

    if num > 2 :

        for idx in range(3, num+1):

            value = dp[idx-2] + 2 * dp[idx-1]

            dp.append(value%9901)

    return dp[num]

print( solution() )