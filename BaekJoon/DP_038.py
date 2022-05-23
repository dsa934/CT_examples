
'''

 Backjoon _ exampels 13699

  "��ȭ��"   by Jinwoo Lee

  < algorithm >

  1.  idx_1 : 0 ~ n-1,  idx_2 : n-1 ~ 0  �Ųٷ� cross �̵�

    => idx ��� ���� for�� 

    => ���� �ٸ� idx ��,�� ����ó���� ���� while �� ��� 

 

'''


def solution():

    num = int(input())

    dp = [0 for _ in range(num+1)]

    dp[0] = 1

    if num >= 1 : 

        dp[1] = dp[0] *dp[0]


        for idx in range(2,num+1):

            val_1, val_2 = 0, idx-1
            
            while val_2 >= 0 :

                dp[idx] += dp[val_1]*dp[val_2]

                val_1 += 1
                val_2 -= 1
                
    return dp[num]

print( solution() )