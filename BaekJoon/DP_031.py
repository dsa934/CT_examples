
'''

 Backjoon _ exampels 15489

  "�Ľ�Į �ﰢ��"   by Jinwoo Lee

  < algorithm >

  1. dp �� ���� �Ľ�Į �ﰢ�� �����

  2. Ư�� ���� �� �� ���ϱ� 

   * start = [raw][col] 

    raw : raw ~ raw + w 

    col : col ~ col + w 

    => ���� ���� ���� column �� �ո� ���ϸ� �Ǳ� ������ while , for�� ���

       raw�� ���� for�� ���� [raw+w_idx] �� �ϸ�� 

       while cnt < w+1 :  # w�� �����ؾ� �ϱ� ����

        for col_idx in rnage(col, col+cnt):
            
           ans += dp_table[ raw + cnt -1 ] [ col_idx ]
        
 
    * �ֽô��� 3�� �������� ������ �ʿ䰡 ����

     => n^3 �� �Ǹ� TLE�� �ɸ� �� ���� 

     => '3�� ���� �ؾ� �ϳ�?' ���� �Ǹ� �ϳ��� for���� indexing���� ���� �� �ִ��� ������ üũ 

'''


def solution():
    

    raw, col, w = list(map(int, input().split()))


    dp_table = [[0 for _ in range(30+1)] for _ in range(30+1) ]

    dp_table[1][1] = 1

    for i in range(2,31):

        for j in range(1, i+1):

            if j == 1 : 

                dp_table[i][j] = dp_table[i-1][j]

            else:
                dp_table[i][j] = dp_table[i-1][j] + dp_table[i-1][j-1]
        
    ans = 0 
    cnt = 1

    while cnt < w+1 :
        
        for col_idx in range(col, col+cnt):

            ans +=  dp_table[raw+ cnt -1 ][col_idx] 

        cnt +=1


    return ans


print( solution() )

