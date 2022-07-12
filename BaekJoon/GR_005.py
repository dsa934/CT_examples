

'''

 Backjoon _ exampels 14655

  "욱제는 도박쟁이야 !!"   by Jinwoo Lee

  < algorithm >

  1. 연속된 3개의 동전을 뒤집는데,  동전을 뒤집는 횟수에 제한이 없다

    => 동전을 무한히 뒤집을 수 있다면 

       a) first 의 요소가 모두 양수가 될때까지 계속 뒤집음

       b) second의 요소가 모두 음수가 될떄까지 계속 뒤집음

       ∴ 결과적으로 무한히 뒤집는 다는 조건을 이해했다면 , '3개의 연속된 동전을 뒤집는다' 는 무시가 가능해짐


  * map function

   => 보통 map 은  list(map(int , input().split() )) 의 형태로 사용했는데 

     int ->  lambda x : abs(int(x))  를 채용함으로써  

     int : cast 연산자

     abs() : 절대값 구하기 

     위 함수를 동시에 실행 가능 -> 코드가 좀 더 간결 해짐 

 

'''



def solution():
    
    num = int(input())

    first = sum( list(map(lambda x : abs(int(x)), input().split())) ) 

    second = sum( list(map(lambda x : abs(int(x)), input().split())) ) 

    print(first + second)

solution()