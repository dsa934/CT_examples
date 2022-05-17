
'''

 Backjoon _ exampels 1535

  "�ȳ�"   by Jinwoo Lee

  < algorithm >

  1. ���� �˰��� �̿�

    * dp_table �� ���´� < raw, col > = < ��� ��, hp(1~99) >  �� ����

    * hp�� 100�� �Ǹ� �״´ٰ� �����ϱ� ������ ���� 



 


'''

def solution():

    n_person = int(input())

    hp = [0] + list(map(int, input().split()))

    thx = [0] + list(map(int, input().split()))


    dp_table = [[0 for _ in range(100)] for _ in range(n_person+1) ]

    
    for idx in range(1, n_person+1):

        for hp_idx in range(1, 100 ):
            
            if hp_idx < hp[idx] :

                dp_table[idx][hp_idx] = dp_table[idx-1][hp_idx]

            else:
                dp_table[idx][hp_idx] = max( dp_table[idx-1][hp_idx] , dp_table[idx-1][hp_idx - hp[idx] ] + thx[idx])

        

    return dp_table[n_person][-1]

      

print( solution() )