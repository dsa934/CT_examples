'''

 Programmers _ exampels 4

  "Develope Functions"

 by Jinwoo Lee ( 2021/06/01 )


 # Problem
 
  - 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
  - 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
  - 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 
    return 하도록 solution 함수를 완성하세요.


 # Attention for Implementation

  - 반올림(round) 내장함수 사용하는 경우 제외하고 올림/내림일 경우의 Tip

    임의의 수 N, divisor에 대해 N/divisor = X.12346 와 같이 나누어 떨어지지 않는 경우

    32 // 5  = 6  ,  -32 // 5 = -7

    올림 : N에 대하여 음수를 취하면 올림의 효과 

    내림 : N에 대하여 양수를 취하면 내림의 효과 



  - list에서 요소별 대소 비교 후 추출과 같은 과정이 있는 문제의 경우 만들어진 list에서 추출하는 방식으로 구성할 경우 pop or del 하는 순간 list 길이가 달라져서 구현이 어려울 수 있다

    => 비교하는 요소들을 list에 다 채운 후 비교가 아닌, 채워 넣으면서 비교를 하는 방식으로 구현해보기 




'''

def solution(progresses, speeds):

    # set init params
    result = []

    for p,s in zip(progresses, speeds):

        if len(result) == 0 or result[-1][0] < -((p-100)//s):
            
            result.append([-((p-100)//s),1])

        else:
            result[-1][1] += 1

    #print(result)
    return [value[1] for value in result]



solution([93, 30, 55], [1, 30, 5])