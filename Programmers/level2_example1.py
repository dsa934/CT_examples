'''

 Programmers _ exampels 1

  "피보나치의 수 "

 by Jinwoo Lee ( 2021/05/31 )


 # Problem

  - F(2) = F(0) + F(1) = 0 + 1 = 1
  - F(3) = F(1) + F(2) = 1 + 1 = 2
  - F(4) = F(2) + F(3) = 1 + 2 = 3
  - F(5) = F(3) + F(4) = 2 + 3 = 5

  => 이전의 두 수의 합


 # Attention for Implementation 

  - 모듈러 연산 

   -> 임의의 숫자 A,B,C에 대하여 (A + B) % C ≡ ( ( A % C ) + ( B % C) ) % C 성립



  - 수학적 정의를 통해 구현하면 재귀함수로 가능하나, 시간초과 오류가 대부분의 coding test에서 생길 수 있음

   => 피보나치 수열의 규칙은 이전 두 수의 합으로 나타낼 수 있음 따라서 

   =>  [ F[0], F[1] ]  -> [ F[0], F[1], F[2] ] 와 같이 배열을 이용하여 값을 추가하고 마지막 값 return 하는 방향으로 구현해보기 

'''


def solution(n):
    
    result_list = [0,1]
    
    for idx in range(2, n+2):
        
        result_list.append( (result_list[idx-2] + result_list[idx-1] ) % 1234567 )
        
        
    return result_list[n]
