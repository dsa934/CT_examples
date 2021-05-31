'''

 Programmers _ exampels 10

  "문자열 내 마음대로 정렬하기 "

 by Jinwoo Lee ( 2021/05/28 )


 # Problem

  - 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
  - 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.


 # Condition

  - strings는 길이 1 이상, 50이하인 배열입니다.
  - strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
  - strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
  - 모든 strings의 원소의 길이는 n보다 큽니다.
  - 인덱스 n의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.
 

 # Attention for implementation

  * lambda functions(익명 함수)

     - 코드의 간결함 & 메모리 절약 
    

       =>    def 함수이름(args):         <====>   lambda args : result
                 return result 


       => def keyword : 코드와 이름을 담아 함수클래스를 통해 객채 생성, 그 객채를 함수 이름과 동일한 변수에 담는 과정을 행하는 역할

                        함수객체를 변수에 담은 시점에서, 함수 객체는 메모리에 올라가서 변수를 통해 자신이 호출되기를 기다리게 된다 -> 1번만 사용되는 경우 메모리 낭비 
    

'''

def solution(strings, n):

    # set init params
    result = []
    
    # condition 5
    strings = sorted(strings)
    
    result = sorted(strings, key = lambda x: x[n])

    return result
   