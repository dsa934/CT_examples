
'''

 Backjoon _ exampels 2579

  "��� ������"   by Jinwoo Lee

  < algorithm >
 
  1. N > 3 ,  F(N) = max ( F_cost[N-3] + F_stairs[n-1] + F_Stairs[n] , F_cost[N-2] + F_stairs[n])

  2. ' �����ؼ� 3���� ����� ���� �� ����' �� ���ǿ� ���Ͽ�,  ���� ��ġ�� t��� �Ҷ�

      a)  t-2 + 2 step up                => 2ĭ �Ʒ����� �ѹ��� 2ĭ���� t ����

      b)  t-3 + 2 step up + 1 step up    => 3ĭ �Ʒ����� �ٷ� ��ĭ t-1���� ���� �� 1ĭ �̵��Ͽ� t ���� 


  3. �ʱⰪ ����

     a) 0��  : ��� ����, 0 

     b) 1��  : ��ĭ���θ� ����, info_stair[1]

     c) 2��  : 2ĭ �ѹ��� or 1ĭ�� �ι� , max( info_stairs[2], info_stairs[1] + info_stairs[2] )


     * ���� ��� table �� dp�� ����,  ��� ������ ����迭�ν� Ȱ�� ( �� ��ȭ x )
     
       a)  'RGB �Ÿ�' ������ �ٸ��� info_table�� ���� �������� ���ϴ� ����

           =>  ������ : ���翡�� ������ ������ Ȱ���Ͽ� ���� Ǯ�� ( T���� ������ t-1 ���� �� ���� Ȱ�� ) 

               ������ :  '�������� ������� ���� (3ĭ ���� ���� ���� )'

                          t���� �����ϱ� ���� Ȱ���ϴ� ������ �������� ����������,  ���ϴ� ���� ����( t-2, T-3 )�� �޶����� ������ �߰� TABLE �ʿ� 
               





  cf. DP ���� Ǯ�̽� ����� �������� �ʴ´ٸ�,

    * ������ �����ϴ� ' �̷� ' �� �������� ����, ������ '����'�� �����ϱ� 

      ����� � �ö󰡾� �ϴ°�?  =>  �� ��������� ��� �ߴ°� ?






'''

def climbing_stairs():

    num_stairs = int(input())

    info_stairs = [0]

    for _ in range(num_stairs):

        info_stairs.append(int(input()))
    
    if num_stairs == 1: 
        
        return info_stairs[-1]


    cost = [0, info_stairs[1] ,  max ( info_stairs[2], info_stairs[1] + info_stairs[2] ) ]  
    
    if num_stairs > 3:
        
        for idx in range(3, num_stairs+1):
            
            _cost = max ( cost[idx-3] + info_stairs[idx-1] + info_stairs[idx] , cost[idx-2] + info_stairs[idx] )

            cost.append(_cost)


    return cost[num_stairs]


print ( climbing_stairs() )

    


    
