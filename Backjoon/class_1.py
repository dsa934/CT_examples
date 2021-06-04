'''

 Backjoon _ exampels #

  "10951 - A+B-4"

 by Jinwoo Lee ( 2021/06/xx )


 # Problem

  - 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.



 # Attention for Implementation

  - 종료조건 및 testcase 수가 정해져 있지 않는 경우

   => while try ~ except 구문 활용 


'''

while True:

    try :
        n, m = map(int, input().split())
        print(n+m)

    except:
        break



