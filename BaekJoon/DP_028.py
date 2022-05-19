
'''

 Backjoon _ exampels 2839

  "���� ����"   by Jinwoo Lee

  < algorithm >

  1. �־��� ���� N kg �� ���Ͽ� ,   3kg, 5kg ������ ���� �ּҷ� ��� �ϱ� 

    => dp ������ ������, ���ؾ� �ϴ� ������ ������ dp array�� �����غ��� 

                                               0   1   2  3  4  5 
      dp = [ 0 for _ in range(num+1) ]   =>   [ 0 , 0 ,0 ,0 ,...  ]


    => 3, 5 kg �� ���� 1������ �̵� ��ų �� ����  =>   0   1   2  3  4  5 
                                                      [ 0 , 0 ,0 ,1 ,0, 1 ,  ...    ]  


  2. �� dp table�� ����, 6kg ���ʹ� [idx-3], [idx-5]�� ���� ǥ���� ����

     dp[idx] = min ( dp[idx-3] , dp[idx-5] ) +1

     => �� ���������� 3,5�� ���� �� ���� kg�� ���ؼ��� ������ ���� ������ ���� ó���� ������ ���� 

     6�� ��� 

     dp[6] = min(dp[3], dp[5]) + 1

     => 3kg �� ��� 1���� �̸�,  6kg �̸� 3kg�� ���� ������ �� �Ѻ����� �߰� => ��������� 2���� 

     dp[9] = min (dp[6], dp[4] ) + 1 

     =>  2 ���� + 1  => 3���� 





  3. dp array �ʱ� ����

     dp = [ (5000 +1) for _ in range(num+5) ]

     num = 0~ 4�� ���ð�� for���� out of idx ������ �߻��ϱ� ������ �̸� ���� ó�� 



      
  


  * dp Ǯ�� ���޾Ƽ� �⺻���� �ٽ� �����ϱ� 
 

'''



def solution():
    
    num = int(input())

    
    dp = [ (5000 +1 ) for _ in range(num+5) ]


    dp[3] = 1
    dp[5] = 1

    for idx in range(6, num+1):

        dp[idx] = min (dp[idx-3] , dp[idx-5]) + 1

        
    return dp[num] if dp[num] < 5001 else -1 


print( solution() )