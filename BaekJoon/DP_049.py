
'''

 Backjoon _ exampels 14607

  "피자 (Large)"   by Jinwoo Lee

  < algorithm >

  1. 점화식 : dp[idx] = dp[idx-1] + idx-1

  2. 1 <= N <= 1e9 

    => N의 범위가 크기 떄문에 1의 점화식을 dp array로 작성하면 memory 초과 발생

    => 이전 값, 이전 idx만 있으면 됨으로 변수 answer 하나만 필요 

    => dp array 대신 dp scalar 값 하나로만 처리하면 통과


  * 배열을 지워가며 dp.clear() 시도 한것은 메모리 초과 대신 TLE 판정 뜸 

    => 변수 하나로 하는 것이 정답 

'''


def solution():

    num = int(input())

    answer = 0 

    if num > 1:
        
        for idx in range(2, num+1):

            answer += (idx-1)

    return answer

print(solution())