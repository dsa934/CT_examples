'''

 Backjoon _ exampels #

  " Baek 1032 - 명령 프롬포트 (문자열)"   by Jinwoo Lee


 # Algorithm 

  0. 검색결과를 보고 어떤 패턴을 입력해야 이런 결과가 나오는지 알아내기 위한 문제 

  1. N개의 입력에 대해 각 입력들의 글자가 같은지 비교 후 같다면 result에 추가 아니라면 ? 추가  

     => zip 사용 
      
     tmp = [ 'abc', 'cde', 'def' ] 라면 ,   아래와 같은 형태로 출력된다 

     for value in zip(*tmp):               ('a', 'c', 'd')
         print(value)            =>        ('b', 'd', 'e') 

 

 # Attention for Implementation

  - zip 내장함수는 iterative 한 객체의 각 요소를 묶거나 해제(unzip) 할떄 모두 사용된다 

   => 1의 예시에서 zip(*list_name)은 해제의 의미라고 생각할 수 있으며, 

      이 문제에 적용하면, 입력받은 각 문자열이 zip 되어있다고 판단, 각 글자별로 묶어주기 위해서 unzip 했다고 이해하면된다


   => zip 사용시 가장 짧은 인자를 기준으로 데이터가 엮이며, 나머지는 버려진다 

      이문제에서 ?의 개수를 가능하면 적게 쓰고 싶다라는 가정이 붙게되는 이유 

'''

num = int(input())

string = [input() for _ in range(num)]

result = []

for value in zip(*string):

    if value.count(value[0]) == num: result.append(value[0])

    else: result.append("?")

print(''.join(result))