
'''

 Backjoon _ exampels 11055

  "���� ū ���� �κ� ���� "   by Jinwoo Lee


  < algorithm >

  0. dp_table�� �ʱⰪ�� <����> ���� ��� �� ��ȭ�Ŀ�  ���� �پ��� ���� ����


     a) dp_table�� �ʱⰪ�� ��� 1�� ���� ���, LIS�� ���� ���� �ذ�
     
     b) dp_table�� �ʱⰪ�� �Է¹��� ���ҷ� �� ���, LIS�� ���� ��ҹ��� �ذ�


     ��ȭ�� : dp[idx] = max ( dp[idx] , dp[cmp_idx] + @  )

 
             @ =>   a)  + 1  : ���� ����

                    b)  + value : ���� ����� �� ���� 
   

    * �� ��ġ(idx) ���غ��� ���� ������ ���� ������ ���� �������ν� dp[idx]�� ��� update �Ǵ� ��





 
  1. ���� ������ ���� ���� ��ġ(idx) �� �� ���� �� (cmp_idx)�� ���ϸ� dp[idx] ���� ���� 
 
      idx  :      0  1  2 3  4  5 6... 

      info  :     1 100 2 50 60 3 5 6 7 8 

      dp    :     1 100 2 50 60 3 5 6 7 8 

                  1 101 3 53 ( 1 + 2 + 50 )

                            113 ( 1 + 2 + 50 + 60 )


            info[idx] = 2, 50�ϋ��� ���� ����, 

            for idx(2) in range(num):

                for cmp_idx(1) in range(idx):

                if info[idx] > info[cmp_idx] :

                 cmp_idx == 1 , �� info[cmp_idx] =1 �� ��,    dp[idx] (2) �� dp[cmp_dx]+ info[idx] (1 + 2) �� 

                 => dp[2] = 3


            for idx(3) in range(num):

                for cmp_idx(1, 100, 2) in range(idx):

                 if info[idx] > info[cmp_idx] :

                 cmp_idx == 1 , �� info[cmp_idx] =1 �� ��,    dp[idx] (50) �� dp[cmp_dx]+ info[idx] (1 + 50) �� 

                 cmp_idx == 2 , �� info[cmp_idx] =100 �� ��,    ���� �Ҹ��� continue

                 cmp_idx == 3 , �� info[cmp_idx] =2 �� ��,  dp[idx] (1+ 50) �� dp[cmp_dx]+ info[idx] ( 1+ 2 + 50) �� 



'''

def solution():

    num = int(input())

    info = list(map(int , input().split()))


    dp = [value for value in info]
    
    for idx in range(num):

        for cmp_idx in range(idx):

            if info[idx] > info[cmp_idx]:

                dp[idx] = max( dp[idx], dp[cmp_idx] + info[idx])

    return max(dp)

    

print( solution() )