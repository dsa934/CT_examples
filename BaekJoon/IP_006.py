
'''

 Backjoon _ exampels 20546

  "������ �ŸŹ�"   by Jinwoo Lee

  < algorithm >

  1. BNP & Timing �Ÿ� ����� �·� ���ϱ� 

    1) BNP : �ش� ��¥�� �ֽ��� �� �� �ִٸ� ������ �缭 ������ �� ���ȱ� 


    2)  �������� 3�� �����ų�, �����ų��� �������� �Ÿ�/������ ����

       => �� �������� ���ϴ� ���� 3���� 

          �������� �������� idx-1, idx-2, idx-3�϶� �ְ��� ����ߴ°��� �ǹ� ��
          
          a)  3�� ���� ����ϸ�, ������ ������ �϶�

          b)  3�� ���� �϶��ϸ�, ������ ������ ��� ������ �Ʒ� ������ ����

          ...  98 15 6 4 1 1 1 ... �� ���� 4�� �϶��ϴ� ��찡 �־��� 


       �� ������ Ǫ�� �ۼ��ڴ� 2��ġ�� �ֽ� ������ �̸� �˰� ������, ���� �� ������ �ι� ����, ������ ���忡���� �̷��� �ֽ� ������ �� �� ���� ������,

          a), b) �� ���� '����'�� �ϴ� �������� 

          ���α׷��� ���� �ÿ��� ������ ��¥(idx)�� �������� 

          [idx, idx-1], [idx-1, idx-2], [idx-2,idx-3] ������ ���Ͽ� ��� ũ�ų�, ��� ���� ��쿡 a,b�� �´� �ŸŹ��� �ϵ��� �����ϸ� �ȴ�.







         

'''

def BNP(money, stock):
    

    cnt = 0 

    cur_money = money

    last_price = stock[-1]

    for value in stock:

        if cur_money >= value :

            cnt += cur_money // value

            cur_money %= value


    return cur_money + (cnt*last_price)




def Timing(money, stock):
    
    cur_money, cnt = money, 0
    
    last_price = stock[-1]
    

    for idx in range(3,len(stock)):
        
        # up 
        if stock[idx] > stock[idx-1] and stock[idx-1] > stock[idx-2] and stock[idx-2] > stock[idx-3] :

            cur_money += cnt * stock[idx]

            cnt = 0

        # down
        elif stock[idx] < stock[idx-1] and stock[idx-1] < stock[idx-2] and stock[idx-2] < stock[idx-3] :
            

            cnt += cur_money // stock[idx]

            cur_money %= stock[idx]

  
    return cur_money + last_price*cnt



def solution():
    
    money = int(input())

    stock = list(map(int, input().split()))
   

    BNP_val = BNP(money,stock)
    Timing_val = Timing(money,stock)
    
    if BNP_val == Timing_val : answer = 'SAMESAME'

    elif BNP_val > Timing_val : answer = 'BNP'
    else : answer='TIMING'


    return answer



print (  solution() )