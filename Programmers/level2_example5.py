'''

 Programmers _ exampels 5

  "주식가격"

 by Jinwoo Lee ( 2021/06/01 )


 # Problem

  - 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

  - [1,2,3,2,3] => [4,3,1,1,0]


 # Attention for Implementation

  - next greater element 

  - 대소비교에 스택을 이용하는 방법도 있는것 같은데 추후 생각해보기

'''



def solution(prices):

    result = [0 for _ in range(len(prices))]

    for idx, value in enumerate(prices):

        for cmp_idx in range(idx+1,len(prices)):

            if value <= prices[cmp_idx] :

                result[idx] +=1

            else:
                # break 변한 그순간까지는 값이 유지되기떄문에 1증가 시키고 break 해야함
                result[idx] +=1
                 
                break

    print(result)


solution([4,1,5,9,2,45,6,7,8])




