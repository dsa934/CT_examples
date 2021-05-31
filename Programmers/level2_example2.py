'''

 Programmers _ exampels 2

  "가장 큰 수"

 by Jinwoo Lee ( 2021/06/01 )


 # Problem

  - 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

  - 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

  - 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.



 # Attention for Implementation

   * string algorithm 
   
    - 모든 조합을 고려하는 방법은 시간복잡도가 O(len(numbers)) 라서 고려되지 않는다.

    - 주어진 정수를 통해 n자리수를 만들어 비교하는 문제임으로 

      주어진 정수를 반복하여 n자리수를 만든 후 어떤 정수가 앞쪽에 위치할지 대소비교 

      주어진 정수 : {6,10,2} ->  6666, 1010, 2222 로 만든후 비교 



   * map functions

    - n개의 데이터를 한번에 다른 형태로 변환하기 위하여 사용 

    - map(변환함수, 순회 가능데이터)  =>  list(map(str, numbers) )  map 객체로 return 되기 때문에 list화 

    - for value in numbers 보다 간결한 표현 가능 ( list comprehension )

    - str로 바꾼것은 *n 연산 진행시 n번씩 반복되는 문자열로 만들기 위함



   * 마지막 str(int (''.join(sort_list)))

   - [0,0,0,0,0]을 넣을 경우 00000으로 나오기 떄문에 int 를 통해 중복제거 후 

     문제에서 요구하는 return 은 str 형태이기 떄문에 다시 str로 casting 연산 진행 


'''

def solution(numbers):

    str_list = list(map(str,numbers))

    sort_list = sorted( str_list, reverse= True, key = lambda x : x*3)

    print(str(int(''.join(sort_list))))
    return str(int(''.join(sort_list)))
    



solution([0,0,0,0,0])


