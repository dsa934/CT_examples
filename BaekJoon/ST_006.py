

'''

 Backjoon _ exampels 4096

  "�Ӹ���ι���"   by Jinwoo Lee

  < algorithm >

  1. 0 �̸� �Է� ���� 

    => �Է����� 0000�� �־��� ���� �ֱ� ������ , int(''.join(num)) = 0 �̸鼭, ���̰� 1���� üũ �ʿ� ( �� ���� ������� 50% ���� Ʋ�� ����)


  2. ���ڿ� + ����

    1) ���ڿ� -> ���� ��ȯ 

       string = '00001234'  

       int( ''.join(string) )                    



    2) ���� -> ���ڿ�

       num = 1234

       list( str(num) )    # ���ڸ� ���ڿ� ȭ(str) �� list�� �����ؾ� int object not iterable ���� �߻����� ���� 


    3) ���ڿ� + ���� �縰��� ����������  ����, �縰��� ���θ� üũ���ָ� �ȴ�


      * ���� : ���� ���� ���� �� ,  ���ڿ��� ���ڷ� ��ȯ�ϴ� �������� �տ� 000�� ���������  ���� ���� ���̸�ŭ 0�� �����ش� 

      * raw �� reverse�� ������ �縰���         
      

'''




def chk_palindrome(num):

    cnt = 0

    length = len(num)
    
    while True :

        if ''.join(num) == ''.join(num[::-1]) and len(list(''.join(num))) == length: 
            
            break

        else:
            cnt +=1
            
            str2int = list(str(int(''.join(num)) + 1 ))

            differ = length - len(str2int)
            
            # algorithm - 3
            num = list(('0'*differ) + ''.join(str2int))        

    return cnt

    
   

def solution():

    while True:

        num = list(input())

        if len(num) == 1 and int(''.join(num)) == 0 :
            break

        else:

            print( chk_palindrome(num) )

    

solution()