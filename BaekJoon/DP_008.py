
'''

 Backjoon _ exampels 1463

  "1로 만들기"   by Jinwoo Lee

  < algorithm >

  1. 이전 숫자의 계산 결과를 활용 

     dp[idx] = dp[idx-1] + 1   => 숫자가 1증가 했기 때문에 최소한 -1 연산이 활용됨으로 횟수 1 증가


  2.  Greedy method 적용 불가 

     * /3 , /2 , -1 중에 어떤 방법이 최선인지 알 수 없음

       => greedy가 적용되려면, 최소비용을 구하는만큼 /3을 했을떄 해가 보장되어야 하는데 해당 문제는 그렇지 않음 

          이에 대한 예시로 '10 -> 9 -> 3 -> 1 ' 주어짐


  3.  dfs/bfs 적용 불가능

     * 시작점으로부터 도착점까지  /3 , /2 , -1 의 3가지 방법을 사용하여 가장 빨리 도착하는 (최단경로 문제) 라면 적용할 수 있지만,

       /3 , /2 , -1 이 떄에 따라 적용이 '불가능'한 경우가 있음 


  4.  /3, /2, -1 어느 것이 최선인지 모르기 때문에 모두 비교해서 최소값을 저장해야 한다.



'''

def make_one():

    num = int(input())

    dp_table = [0] * (num +1)
    

    for idx in range(2, num+1):

        dp_table[idx] = dp_table[idx-1] +1


        if idx % 2 == 0 :

            dp_table[idx] = min (dp_table[idx], dp_table[idx//2]+1 )

        if idx % 3 == 0:

            dp_table[idx] = min (dp_table[idx], dp_table[idx//3]+1 ) 

    return dp_table[num]

print (make_one())