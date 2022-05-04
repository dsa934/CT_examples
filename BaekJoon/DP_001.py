
'''

 Backjoon _ exampels 1003

  "피보나치 함수"   by Jinwoo Lee

  < algorithm >

  1. bottom up & memoization을 활용한 피보나치 수열 구현

  2. N := n번째 피보나치 수 ( N이 몇번쨰 피보나치 수 라는 의미로 혼동 하지 말것 )

  3. N에 도달하기 까지 1과 0이 몇번 나왔느냐 에 대한 문제이며,

     0,1 각각에 f(n) = f(n-2) + f(n-1)을 적용하면 N번 째 수에 대해 0,1이 각각 몇번 사용되었는지에 대한 '개수'를 알 수 있음 
  


'''




def fib_naive(n):

    zero = [0 for _ in range(41)]
    one = [0 for _ in range(41)]
    
    zero[0], one[0] = 1,0
    zero[1], one[1] = 0,1
    
    if n >= 2 :


        for idx in range(2, n+1):

            zero[idx] = zero[idx-2] + zero[idx-1] 
            one[idx] =  one[idx-2] + one[idx-1] 


    print(zero[n], one[n])

num_test = int(input())

for _ in range(num_test):
    
    fib_naive(int(input()))