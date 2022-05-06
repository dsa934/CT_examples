
'''

 Backjoon _ exampels 9461

  " �ĵ��� ����"   by Jinwoo Lee

  < algorithm >
 
   1. F(n) = F(n-2) + F(n-3)   < ����� ã�� >

   2. init value = [1,1,1]     < �ʱⰪ ���� >

   * �ᱹ dp ������ '����� ã��'�� ���� �Ʒ��� '3����'�� �����ϴ��� üũ�ϱ� 

     a) �ش� ������ sub_problem���� ���� �Ǵ���

     b) sub_problem�� �ذ� �� �θ� ������ Ǯ�� ��� �Ǵ���

     c) sub_problem�� �ذ� �ٸ� sub_problem���� ��� �Ǵ��� ( Momoization )


   * �ʱⰪ ���� (init value)�� ���� Top_down ����� �ƴ�, ' Bottom_up ' ����� ���� 



'''

def padoban():

    
    num = int(input())

    dp_table = [1,1,1]

    if num > len(dp_table):

        for idx in range(3,num+1):

            value = dp_table[idx-2] + dp_table[idx-3]

            dp_table.append(value)


    return dp_table[num-1]



num_test = int(input())

for _ in range(num_test):

    print( padoban() )