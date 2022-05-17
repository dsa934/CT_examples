
'''

 Backjoon _ exampels 12865

  "����� �賶"   by Jinwoo Lee

  < algorithm >

  1. ���� �˰��� �̿�

    i)  if w_idx < info[idx][0] then  dp[idx][w_idx] = dp[idx-1][w_idx]

        => �Է¹��� idx���� ������ ����(info[idx][0])�� ������ ���� ����(w_idx) ���� Ŭ ��� ,

           idx ���� ������ �������� �ʱ� ������, w_idx �� ��ȭ�� ������, ������ ���� idx �� �ϳ� �پ�� �Ͱ� ����

           ��, ������ [idx-1][w_idx] �� ���� ��������.
           


    ii) if w_idx >= info[idx][0] then dp[idx][w_idx] = amx (dp[idx-1][w_idx] , dp[idx-1][w_idx - info[idx][0] ] + info[idx][1] )

        => ������ ���� ����(w_idx) ���� �Է¹��� idx ���� ������ ����(info[idx][0]) �� �۰ų� ���� ������, 2���� case�� ��� �ؾ��Ѵ�

           a) i-th ���� ������ : �������� ���� ��� i) �� ���� ��Ȳ������,  dp[idx-1][w_idx]

           b) i-th ���� ���� : ������ �����ϱ� ���ؼ� ������ ���� ���ѿ��� i-th ���� ������ ���Ը� ���� �ؾ� �ϰ�, i-th���� �������� ��ġ�� ������� �Ѵ�.

             -> dp[idx][w_idx] = dp[idx][w_idx - info[idx][0] ] + info[idx][1]  

             
    iii) dp[idx][w_idx] = max(dp[idx-1][w_idx] , dp[idx-1][w_idx - info[idx][0]] + info[idx][1])



  2. dp_table ���� 

    * ���� �˰��� ����, ���� ������ 2���ε� �ϸ�, �־��� ���� N, M�� ���Ͽ� 

     0 <= N <= max(N),   0<= M <= max(m) �� ������ dp_table�� �����Ͽ�, bottom_up ������� ä��������

     ������ ��� dp_table[N][M]�� return �ϸ� �ȴ�.



  3. ����

    * dp_table ���� ��, �� ����(N,M)�� ù���� ��Ҹ� ä��� ����, 0���� ��Ҹ� zero_padding ����� �Ѵ�.

     table �������� ������ ���µ�, (N,M)�� ���� �Է� �����͸� ������ 0������ ���� ������ ���� ������ 

     [0] + info_lst �� ���·� ������ �ʿ��ϴ�.

 

'''


def solution():


    n_item, n_weight = list(map(int, input().split()))

    info = [0] + [ list(map(int, input().split())) for _ in range(n_item)]

    dp = [[0 for _ in range(n_weight+1)] for _ in range(n_item+1)]


    for idx in range(1,n_item+1):

        for w_idx in range(1, n_weight+1):

            if w_idx < info[idx][0] :

                dp[idx][w_idx] = dp[idx-1][w_idx]

            else:

                dp[idx][w_idx] = max(dp[idx-1][w_idx] , dp[idx-1][w_idx - info[idx][0]] + info[idx][1])

        
    return dp[n_item][n_weight]
    

print( solution() )