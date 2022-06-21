
'''

 Backjoon _ exampels 1788

  "�Ǻ���ġ ���� Ȯ�� "   by Jinwoo Lee

  < algorithm >

  1. �Ǻ���ġ�� ���� �������� Ȯ���� ��� 

     -10  -9  -8   -7   -6  -5   -4  -3  -2  -1  0  1  2  3  4  5  6   7   8   9   10

     -55  34  -21  13   -8   5   -3   2  -1   1  0  1  1  2  3  5  8   13  21  34   55 

     => ���� ���⿡���� ��ȣ�� ���������� ���ϴ� ���� Ȯ�� �� �� �ִ�

     
     1) ����� ��� 

        dp[idx] = dp[idx-1] + dp[idx-2]


     2) ������ ��� 

       => dp[idx], dp[idx-1] ���� �˰� dp[idx-2]�� �𸣴� ��Ȳ ������ 

       dp[idx-2] = dp[idx] - dp[idx-1] 


       ������ �����̱� ������ dp[idx-2]�� ������ �̷� ������ �Ǿ������. ( dp[idx-2]�� �𸣰� dp[idx], dp[idx-1]�� �ƴ� ��Ȳ�� ���� ���� )

       dp[idx-2] <=> dp[idx]�� ��ȯ�� �̷������ �Ѵ� 

       �� value = dp[idx-2] - dp[idx-1]


 
  * 1e10 : 10, 000, 000, 000 

    => e �ڿ��� 0�� ������ �ǹ��� ȥ������ ���� 

    => �������� 1,000,000,000 (10��)�� �䱸�ߴµ� 100������ �ؼ� Ʋ�� 



'''


def solution():

    num = int(input())

    mode = int(1e9)
    
    _type = 0 
    dp = [0, 1]

    if num != 0 and num > 1:
        
        for idx in range(2, num+1):

            value = (dp[idx-1] + dp[idx-2]) % mode 

            dp.append(value)


    elif num != 0 and num < -1 :
        
        for idx in range(2, abs(num)+1):

            value = dp[idx-2] - dp[idx-1]


            if value < 0 :
                
                value %= -mode


            elif value > 0 :

                value %= mode

            dp.append(value)
    
    

    if dp[abs(num)] > 0 :
        _type = 1

    elif dp[abs(num)] < 0 :
        _type = -1

    print(dp)
    print(_type)
    print(abs(dp[abs(num)]))

solution()