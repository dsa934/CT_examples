
'''

 Backjoon _ exampels 10844

  "�����ܼ�"   by Jinwoo Lee

  < algorithm >

  number :    0 1 2 3 4 5 6 7 8 9

  �ڸ���(1) : 0 1 1 1 1 1 1 1 1 1

  �ڸ���(2) : 1 1 2 2 2 2 2 2 2 1

  �ڸ���(3) : 1 3 3 4 4 4 4 4 3 2


  1. ��ȭ��

   num == 0 : 

   num == 9 :  dp[pos][num] = dp[pos][8]

   others   :  dp[pos][num] = dp[pos-1][num-1] + dp[pos-1][num+1]


  2. init value

     1�ڸ��� ��� ���� ���,  1 ~ 9���� �� �ڿ� ��ġ�Ǵ� ���� 1, 0�� ����(�ڸ����� 1�̸� 0���� �����ϴ� �� �̱� ���� )

     dp_table[1][1~9] = 1 , dp_table[1][0] = 0 


  * dp table�� n���� �迭�� ������ �� �ִ�.

    dp_table[�ڸ���][��ܼ� �������� ��ġ�� ����]


  * ������ �а� dp_table�� idx�ν� ���� �Ӽ��� �������� ���� �ľ��ϰ�, �׿� ���� ��ȭ�� �����ϱ� 


'''



def dp():

    num = int(input())

    mod = 1000000000

    dp_table = [[ 0 for _ in range(10) ] for _ in range(num+1)]

    # init value
    for idx in range(1,10):

        dp_table[1][idx] = 1


    # dp algorithm

    for idx in range(2, num+1):

        for j in range(10):

            if j == 0 :

                dp_table[idx][j] = dp_table[idx-1][1]

            elif j == 9 :

                dp_table[idx][j] = dp_table[idx-1][8]

            else:

                dp_table[idx][j] = dp_table[idx-1][j+1] + dp_table[idx-1][j-1]

    #print(dp_table)


    return sum(dp_table[num]) % mod 

print ( dp() )