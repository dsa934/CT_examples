
'''

 Backjoon _ exampels 24417

  "알고리즘 수업 - 피보나치 수2 "   by Jinwoo Lee

  < algorithm >

  1. pypy3 로 제출 -> TLE 통과, MLE 불통과

     => dp array로 작성하는 것이 아니라, 2개의 변수만 사용

        idx-2, idx-1에 해당하는 prev_1, prev_2 변수 값으로만 문제 해결시 MLE 해결 


  2. python 제출 통과 자들은 보통 sys library 사용

    => 코테 대비용임으로 해당 라이브러리 사용은 지양 


 * why difference between pypy3 and python 


   => pypy3 는 Just-in-time compiler 

      python 은 CPython인 인터프리터 형식을 사용 

      실행 시간 (faster) : pypy3 > python

      메모리 효율 (good) : pypy3 < python 


   why ?? ( important )

   고급 프로그래밍 언어 => 어셈블리 언어로 번역 해주는 작업 ( 컴파일러 & 인터프리터 )

   * 컴파일러 

     => 프로그램 전체를 스캔하여, 이를 모두 기계어 번역  

        전체 스캔하기 떄문에 초기 시간은 오래 걸리지만, 실행 파일을 만들어놓고 실행떄마다 만들어놓은 실행 파일을 사용하기 때문에 전체 실행 시간은 인터프리터보다 빠르다.

        but  고급언어로 작성된 소스 => 기계어 번역 과정에서 
        
             1. object code라는 파일을 만들기
             
             2. Linking : 1)에서 만든 object code를 하나로 묶어서 실행 파일로 만드는 작업

             을 거치기 떄문에 인터프리터 방식보다 메모리를 많이 잡아 먹는다 .

        프로그램 전체를 스캔함으로 실행전에 오류를 알 수 있다.



   * 인터프리터

     => 프로그램 실행시 한번에 한 문장만 번역 하기 때문에 실행시간 자체는 컴파일러보다 느리다.

        but 컴파일러처럼 object code, linking 과정을 거치지 않기 떄문에 메모리면에서 효율적이다 .

        한문장씩 번역하기 떄문에 오류가 생기면 프로그램 종료 


    


  

'''



def solution():

    num = int(input())

    prev_1, prev_2 = 1,1 

    if num > 2: 

        for idx in range(3, num+1):

            prev_1, prev_2 = prev_2, (prev_1 + prev_2 ) % 1000000007
            

    print(prev_2 ,num-2)

solution()