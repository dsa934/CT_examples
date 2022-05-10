
'''

 Backjoon _ exampels 2156

  "������ �ý� "   by Jinwoo Lee

  < algorithm >

  * ��� ������ ������ ��� ( �����ؼ� 3���� ���� �� ���ٴ� ���� )


  1. �ִ� ���뷮 (dp) , �� n��° ������ ���� ���뷮 (info )�� �־�����.


  2. dp[num] = max( dp[num-3] + info[num-1] + info[num] , dp[num-2] + info[num] )

    a) dp[num-3] + info[num-1] + info[num]     : num-3 ��°��, num-1�� ��ĭ�� �ٰ�, num ���� �����ֺ��� �����ϴ� ��� (1,3,4)
     
    b) dp[num-2] + info[num]                   : num-2������ num ��°�� �����ֺ��� ���� �ϴ� ���                     (2, 4)


    
    => 2���� ��� ���, �������� 3���� ���ô� ����� ���� ���ϱ� ���� ��� �Ǿ��� 

    * ��� ������ ������ ���, �̵� ����� = { 2ĭ, 1ĭ } �� 2���� ��� �ۿ� ������ ������ ��  2���� ���׸� ���������,

      �� ���������� �Ѱ��� ������ �� ����ؾ� �Ѵ�.

     �� dp[num-1]                               : num�� �ش��ϴ� ���� ������ �ʾ��� ���

    

    => a), b)�� ��� ��� num ĭ�� ���� �Ǿ������� ����� ���� ����Ѵ�.
     
       ���� ���,  bottom_up ������� memoization�� ����Ͽ� �����Ǿ�������, '���ӵǴ� 3���� ���� �� ����' ��� ��Ģ�� �ǰ��Ͽ� 
       
       dp_table�� �� ���� �� ���, dp[num-1]�� ���� �ǹ̴� 

       ' ���ӵ� 3���� ������ �����鼭 num-1��° ������ ���������� �ִ밪'�� �Ǹ� 

        �� ���� ����ϴ� ������ dp[num]�� a), b)�� ���� ����ϴ� ����� ������ num-1 ���� ������ ���õ��� ���� �� �ִµ�
        
        num-1 ���� ������ ���õ��� ���� ����� ���� num ���� ������ �����ϴ� ����� �� ���� Ŭ ���ɼ��� �ֱ� �����̴�.


       
       


 
'''

def solution():

    num_wine = int(input())

    info = [0]
    
    for _ in range(num_wine):

        info.append(int(input()))


    dp_table = [0]

    if num_wine >= 1:

        dp_table.append(info[1])

    if num_wine >= 2 :

        dp_table.append(info[2]+info[1])



    for idx in range(3,num_wine+1):

        target_before_one_step = dp_table[idx-3] + info[idx-1] + info[idx]

        target_before_two_step = dp_table[idx-2] + info[idx]

        dp_table.append(   max( target_before_one_step , target_before_two_step, dp_table[idx-1]) )

    #print(dp_table)
    return max(dp_table)


print( solution() )
