
'''

 Backjoon _ exampels 9711

  "피보나치"   by Jinwoo Lee

  < algorithm >

  1. python 제출시 TLE, pypy3 제출시 pass

    => python 풀이 중에서, P의 범위가 10000 까지임으로 미리 10000 까지 만들어서 가져오는 방식을 취하면 Pass 받을 수 있음

      그러나 효율적인지는 의문 


  2. 아래 코드가 갖는 의의 

    * 실행 속도가 빠름   pypy 3 > pyhon 3

       pypy3(컴파일러) > python3 (인터프리터 방식)


    * pypy3는 메모리면에서 손해

      => object code 생성, linking 과정( object code 묶기) 떄문에 메모리 효율은 인터프리터 방식에 비해 떨어짐


    * 공간 복잡도가 O(1)

      => dp array를 사용할 경우 공간 복잡도가 O(n) 이지만,

         bottom_Up & memoization 기법을 사용할 경우, 최종적으로 구해야하는 시점 t의 값을 구하기 위해  t-1 값만 있으면 되기 떄문에 공간복잡도 O(1) 구성 가능


    ∴ 결과적으로, 실행속도는 빠르나 메모리 효율이 별로인 pypy3 를 사용하면서, 공간복잡도를 O(1)로 줄여 메모리에서 얻는 손해를 어느정도 zero_sum 하고자 한 코드 

 

'''


def solution():

    p, q = map(int ,input().split())


    prev_1, prev_2 = 1,1

    if p > 2 :

        for _ in range(3, p+1):

            prev_2, prev_1 = (prev_1 + prev_2 ), prev_2

    return prev_2 % q



num = int(input())

for idx in range(1,num+1):


    ans = solution()


    print(f'Case #{idx}: {ans}')



