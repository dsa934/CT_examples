
'''

 Backjoon _ exampels 21313

  "문어"   by Jinwoo Lee

  < algorithm >

  1. if even number then answer = [1,2] * (num//2)

  2. if odd number then answer = [1,2] * (num//2) + [3]


  ∴ answer = [1,2] * (num//2) + ( [3] if num%2 else [] )

    => if <조건문> 에서 조건문 부분이 0이면 False, 그 외 다른 숫자면 True

    => ( [3] if num%2 else []  ) 에서 () 을 생략하면 통과 판정을 받지 못함

       정확한 진단은 하지 못했지만, () 생략하면 [1,2] * (num//2) + [3] 이후에 if 조건을 판단할 수도 있을 것 같음




  * 그림을 통해서 1번과 N번의 연결이 무조건 2어야 한다고 잘못 생각해서 틀렸던 문제

    => 그림에 현혹 되지 말고 문제 조건을 조금 더 세심하게 읽기


 '''   
 



    
def solution():
    
    num = int(input())

    answer= [1, 2] * (num//2) +([3] if num %2  else [] )

    print(answer)
    
solution()
     
