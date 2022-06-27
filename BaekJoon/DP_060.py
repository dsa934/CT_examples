


'''

 Backjoon _ exampels 2407

  "����"   by Jinwoo Lee

  < algorithm >

  1. ������ ���ϴ� ������ �Ľ�Į�� �ﰢ���� �����ϱ�

  2. �Ľ�Į�� �ﰢ�� init value =>   [0][0] , [1][0], [1][1] = 1 ,1 ,1  �� ���� 

  * but, n>= 1000 �̻��� ū ������ ���, �Ľ�Į�� �ﰢ������ ������ ���ϴ°� TLE�� �ɸ� 

    ������ �丣���� ������ , ��ī�� ���� ������ �� ������ ���� �� �ִµ�

    �̴� gold level�ε� ��  => ���� �̺κп� ���� �����ؾ� �� (2022-06-27)


 
    ref. https://rebro.kr/107

'''






def solution():

    n, m = map(int , input().split())
    

    dp_table = [ [0 for _ in range(n+1)] for _ in range(n+1) ]
    
    dp_table[0][0], dp_table[1][0] , dp_table[1][1] = 1, 1, 1
    

    for row_idx in range(2, n+1):
        
        for col_idx in range(0, row_idx+1):
            

            if col_idx == 0 : 
                
                dp_table[row_idx][col_idx] = dp_table[row_idx-1][col_idx]
                
            else:
                
                dp_table[row_idx][col_idx] = dp_table[row_idx-1][col_idx] + dp_table[row_idx-1][col_idx-1]
                

    print(dp_table[n][m])
    
solution()