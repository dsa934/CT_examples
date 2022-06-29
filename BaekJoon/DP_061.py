
'''

 Backjoon _ exampels 1965

  "상자넣기"   by Jinwoo Lee

  < algorithm >

  1. 현재 위치(cur_idx) 기준으로, 0~cur_idx-1 까지의 dp table을 조사하여 가장 큰 값을 찾고

     해당 값에 +1 을 하여 dp[cur_idx]에 저장. +1을 하는 이유는 dp[idx]의 경우 idx에 포함되는 상자들이기 떄문에 자기 자신을 포함하지 않은 수치이다.


  2. 문제의 해석이 조금 이상한 것 같은데 

     (1,5,2,3,7) 구조에서  1,2,3,7을 선택하면 7에 4상자가 들어간다고 서술하고 있다. 문맥상 3상자가 답인 것 같지만 문제가 해석되는 과정에서 오류가 난 것 같다.



     
 

'''




def solution():

    num = int(input())

    score = list(map(int, input().split()))


    dp = [0]

    for cur_idx in range(1,num):

        value = 0

        for cmp_idx in range(0, cur_idx):

            if score[cur_idx] > score[cmp_idx] :

                if dp[cmp_idx] + 1 > value :

                    value = dp[cmp_idx]+1


        dp.append(value)

    print(max(dp)+1)


solution()