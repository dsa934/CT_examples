

'''

 Backjoon _ exampels 21966

  "�߷�"   by Jinwoo Lee

  < algorithm >


  1. ���ڿ� slicing
  
    1) �ڿ��� n���� : -n 

    2) �տ��� n���� :  n     =>  strng[n:-n] �� ���� ǥ��



  2. ���ǿ� ���� �ڸ� ���ڿ��� �� �������� �Ǵ��ϴ� ���

    1) sub_string�� '.'�� ���ԵǴ°�

    2) '.'�� ��ġ�� ������ ���� �������ΰ�


    * index('ã�����ϴ� ǥ��') ��� ��, ���ڿ� �ȿ� ã�����ϴ� ǥ�Ⱑ ���� ��� ������ �߻� 

      => '.'�� �ִ������� üũ


    3) �־��� ���ǵ鿡 �߰�������, �߰� sub_string�� ','�� ���� ��� �ѹ��忡 ���ϱ� ������ ...�� ��� ����


  * ������ �¶��� ���� ��ȸ���� ������ �ڵ�

 

'''




def solution():
    
    n = int(input())

    string = list(input())

    if n > 25 :
    
        sub_string = string[11:-11]
        

        if '.' in sub_string:
            
            if sub_string.index('.') == len(sub_string)-1:

                string[11:-11]='...'

            else:

                string[9:-10]='......'

        else :
            string[11:-11] ='...'

    print(''.join(string))

solution()