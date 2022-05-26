
'''

 Backjoon _ exampels ####

  ""   by Jinwoo Lee

  < algorithm >


 1. dp array�� [0,1,2]�� ���� �Ͽ��� ������ 
 
    0���� �����ϴ� ��쿡 ���� �߰� ó���� �ʿ�  ( ���� ���ǰ� �ٸ� a,b �Ѵ� 0�̾�� �� ) 


    =>  0 10  (input data)

       dp = [ 0 ,1 ,2  3, 5, 8 , 13  ... ]

       0 <= dp <= 10 �� ���� =  6

       ���������� dp[0] �� �ش��ϴ� 0 ���� ������� ���� ( ������ �ڵ忡���� indexing�� ���ϰ� �ϱ� ���ؼ� 0�� ����)

       ���� 0�� �����ϰ� ������ ���� �ϱ� ������

       for value in dp[1:] �� �����ϴ°��� ����


'''



def fibo(lower_boundary, upper_boundary):

    dp = [0,1,2]
    

    if lower_boundary >=3 or upper_boundary >= 3:

        idx = 3

        while True:

            value = dp[idx-2] + dp[idx-1]

            dp.append(value)

            idx +=1

            if value >= upper_boundary :
                break

    
    cnt = 0 

    for value in dp[1:] :

        if value > upper_boundary :

            break


        if value >= lower_boundary :

            cnt +=1


    return cnt




def solution():

    while True:

        a, b = list(map(int, input().split()))

        if a ==0 and b == 0 : break

        ans = fibo(a,b)

        print(ans) 

solution()

