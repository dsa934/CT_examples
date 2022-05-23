


'''

 Backjoon _ exampels 8394

  "악수"   by Jinwoo Lee

  < algorithm >

  1. 사람 수 별 악수 횟수를 써내려가면 피보나치 수열이 성립

  2. 출력에서 값이 매우 커질 수 있기 떄문에 1의 자리만 표기하라고 요구 

    => recursion 방식으로 dp를 푸는것은 recursion depth 초과를 발생시킬 확률이 높음으로 배제 

    => 자료형의 값이 클수록 dp array에 넣을수가 없어서 메모리 초과 오류가 발생하는 듯 함

    => 메모리 초과 문제는 보통 문제에 몇자리수까지 쓰라고 써있으니 참고할것 
 

'''



def solution():
    
    num = int(input())

    dp =  [1 for _ in range(num+1)]

    dp[1] = 1
    
    if num > 1 :

        for idx in range(2, num+1):

            dp[idx] = (dp[idx-1] + dp[idx-2])% 10


    return dp[num]

print( solution() )
