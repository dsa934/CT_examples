

'''

 Backjoon _ exampels 9625

  "BABBA"   by Jinwoo Lee

  < algorithm >

  1. A,B�� ���� DP_table�� �����غ���,  n-2, n-1 �� ���̶�� ����� �� �� ����

  * print() ������ list�� []�� , �� ���ָ鼭 ����ϴ� ����� print ( *list_name ) �ε�

    �̰� print()������ �۵��Ѵٴ°� �˾ƾ� ��
 

'''


def solution():


    num = int(input())

    dp_table = [ [1,0] , [0,1]]


    if num > 1 :

        for idx in range(2, num+1):

            
            dp_table[0].append( dp_table[0][idx-2] + dp_table[0][idx-1] )
            dp_table[1].append( dp_table[1][idx-2] + dp_table[1][idx-1] )



    answer = [ dp_table[0][num] , dp_table[1][num] ]

    return answer


print( *solution() )