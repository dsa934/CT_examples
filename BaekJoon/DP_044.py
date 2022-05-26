
'''

 Backjoon _ exampels ####

  ""   by Jinwoo Lee

  < algorithm >


 1. dp array를 [0,1,2]로 시작 하였기 떄문에 
 
    0으로 시작하는 경우에 대한 추가 처리가 필요  ( 종료 조건과 다름 a,b 둘다 0이어야 함 ) 


    =>  0 10  (input data)

       dp = [ 0 ,1 ,2  3, 5, 8 , 13  ... ]

       0 <= dp <= 10 의 개수 =  6

       문제에서는 dp[0] 에 해당하는 0 값을 고려하지 않음 ( 필자의 코드에서는 indexing을 편하게 하기 위해서 0을 삽입)

       따라서 0을 제외하고 개수를 세야 하기 떄문에

       for value in dp[1:] 로 구현하는것이 정답


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

