'''

 Programmers _ exampels 6

  "행렬의 덧셈"

 by Jinwoo Lee ( 2021/05/27 )


 # Problem
   
  - 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
  - 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.


 # Attention for Implementation

  * 문제 자체는 어렵지 않으나, list comprehension을 활용한 풀이 사용 권장

    - 2개 이상의 for문에 대한 list 내포 사용시, 
    
      case 1 :  [ for x in range(1,10) for y in range(1,10) ]          => list 1개 사용

      case 2 :   [ [for _x, _y in range(x,y)] for x,y in range(X,Y) ]  => list 2개 사용 ( 각 for문별 변수가 이어지는 경우 for문 개수만큼 list 필요)
  


  * Zip(A,B) : 순회 가능한(iterable) 객체를 인자로 받아, aggregation

    - zip return 시 zip_object로 return 하기 떄문에 list화 필요

    - examples

            arr1 = [ [1,2] ,[2,3] ]   list(zip(arr1,arr2))   [ ( [1,2],[3,4] ), ([2,3] , [5,6]) ]        # shape : (2,2,2)
            arr2 = [ [3,4] ,[5,6] ]           ===>                                                        

                          
  * list 사칙연산

    - list로 묶여있는 객체끼리의 합연산은 extend와 같은 연산을 진행

    - 요소별 덧셈을 취하고 싶은 경우 차원을 1차원까지 내려야 한다.



'''

arr1 = [ [1,2] ,[2,3] ]
arr2 = [ [3,4] ,[5,6] ]


print([[_x + _y for _x, _y in zip(x,y)] for x,y in zip(arr1,arr2)])

