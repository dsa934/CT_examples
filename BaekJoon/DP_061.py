
'''

 Backjoon _ exampels 1965

  "���ڳֱ�"   by Jinwoo Lee

  < algorithm >

  1. ���� ��ġ(cur_idx) ��������, 0~cur_idx-1 ������ dp table�� �����Ͽ� ���� ū ���� ã��

     �ش� ���� +1 �� �Ͽ� dp[cur_idx]�� ����. +1�� �ϴ� ������ dp[idx]�� ��� idx�� ���ԵǴ� ���ڵ��̱� ������ �ڱ� �ڽ��� �������� ���� ��ġ�̴�.


  2. ������ �ؼ��� ���� �̻��� �� ������ 

     (1,5,2,3,7) ��������  1,2,3,7�� �����ϸ� 7�� 4���ڰ� ���ٰ� �����ϰ� �ִ�. ���ƻ� 3���ڰ� ���� �� ������ ������ �ؼ��Ǵ� �������� ������ �� �� ����.



     
 

'''




def solution():

    num = int(input())

    score = list(map(int, input().split()))


    dp = [0]

    for cur_idx in range(1,num):

        value = 0

        for cmp_idx in range(0, cur_idx):

            if score[cur_idx] > score[cmp_idx] :

                if dp[cmp_idx] + 1 > value :

                    value = dp[cmp_idx]+1


        dp.append(value)

    print(max(dp)+1)


solution()