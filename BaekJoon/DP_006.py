
'''

 Backjoon _ exampels 1932

  "���� �ﰢ��"   by Jinwoo Lee

  < algorithm >

  0. �ּ�/�ִ� ��� ���� Ǯ�� ������ �� 

    * Greedy�� ������ ���� X 

      => DP Ȱ��, How ?


         * ���� ������ ��������, �Ѵܰ� ���� ������ ���,  cost = current_cost + max or min ( prev_cost )

         => greedy�� �����ظ� �������� �ʴ� ������ �ذ� �� solution 


    * dfs/bfs���� ���� 

      => dfs/bfs�� ���, ����� ���� N������ ��� �������� ���� Ǯ�̰� �ȴ� ( �ִ� ��� okay,  �ּҺ�� ��� Not perfectly okay ) 

         ���ʷ� �����ߴٸ� ( not in visited,  value[_x][_y] == 0 , etc.. ) , �ش� ��ġ ���� �����Ͽ� ǥ�� �ϸ� ������ �ذ�Ǵ� ��찡 ���� ����

         [_x][_y] ��ġ�� ���� ���� �����߾ �� ����  weight ������ �ּҺ���� ���� �ƴ� �� ���� 




   1. ����� ã�� 
 
      first element :=  F[raw, 0] +=  F[raw-1, col]                       => a

      others :=  F[raw, n] += max ( F[raw-1, n] , F[raw-1, n-1] )         => b


      a) �ﰢ�� ���, ���� ���Ҵ� left/right diagonal element�� ��� ������ ���������� 

         [raw][first_column] �� [raw-1][first_column] �� ��� ����


      b) �ﰢ�� ����̱� ������, [raw][-1] �� ��� [raw][column-1] �� ��밡�� ������, 

         �Է°����� �̷���� field��  zero padding�� ���� ���簢�� ���·� ����� ����� ���� 



'''


def int_triangle():

    num_floor = int(input())
    
    field = [list(map(int , input().split())) for _ in range(num_floor)]


    for raw_idx in range(num_floor):

        if len(field[raw_idx]) != num_floor:

            for _ in range( num_floor -len(field[raw_idx]) ):
                
                field[raw_idx].append(0)


    
    for raw_idx in range(1,num_floor):

        for col_idx in range(num_floor):

            if col_idx == 0 :

                field[raw_idx][col_idx] += field[raw_idx-1][col_idx]

            else:

                field[raw_idx][col_idx] += max( field[raw_idx-1][col_idx] , field[raw_idx-1][col_idx-1])

    
    return max(field[-1])



print(int_triangle())

