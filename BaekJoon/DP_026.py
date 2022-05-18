
'''

 Backjoon _ exampels 1495

  "��Ÿ����Ʈ "   by Jinwoo Lee

  < algorithm >

  1. ���� �˰��� ��� ( i���� ���� ����, �����Կ� ���� �� �񱳰� �ʿ��� ��� )

      n / m   0  1  2  3  4  5  6  7  8  9  10 ... m 
      
      start                  1
       
       3      1                              1

       5                1          1  

       7      1                               1
       


  2.  ���ʿ� ������ ����������, dp_table ������ (raw: �뷡 ��, col :���� )�� ��Ȥ�ϰ� ã������, 

      dp_table[x][y] �� ���� ���� ��ġ������ ���ϰ� ���ٺ��� ������ �߻�, 

      ���� ��ȸ���� ���ϴ� ���� ���� �������� �̿��Ͽ� on / off( 1 or 0 )�� ���� �˰��� Ȱ���غ��� 




  * 0 ~ n-1 

    => i���� �� ������ ������ ���� ���� �� (+- volume[i] ), M�� �ѱ��� �����鼭, ������ ���� �����ҋ��� ���� ũ�⸦ ���ϴ� ��

    => m�� ���ϴ°��� �ƴ� (ȥ�� x)

    => ���� n����, ���� ������ n-1���� �ϱ� ������,  n-1 �� �ݺ��ؾ��Ұ� ������, ���ۺκп� �ش��ϴ� start�� �����ϱ� ������ n �� �����ؾ� �Ѵ� 

       ���� for idx in range(1, n+1) �� �ƴ�,  for idx in range(n) �� �Ǵ� �� 

 

'''

def solution():

    n, s, m = list(map(int, input().split()))

    volume = list(map(int, input().split()))

    dp_table = [ [0 for _ in range(m+1) ] for _ in range(n+1) ]


    dp_table[0][s]= 1


    for idx in range(n):

        for cmp_idx in range(m+1):

            if dp_table[idx][cmp_idx] == 1:

                if cmp_idx + volume[idx] <= m :

                    dp_table[idx+1][cmp_idx + volume[idx] ] = 1

                if cmp_idx - volume[idx] >= 0 :

                    dp_table[idx+1][cmp_idx - volume[idx] ] = 1

    result = -1 

    for idx in range(m,-1,-1):
        
        if dp_table[n][idx] == 1 :

            result = idx
            break


    print(result)

solution()