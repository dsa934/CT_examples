'''

 Programmers _ exampels 4

  "정수 내림차순 배치"

 by Jinwoo Lee ( 2021/05/26 )


 # Problem

   - 함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
   - 예를들어 n이 118372면 873211을 리턴하면 됩니다.

 # Attention for implementation

   - 어렵지 않지만 join 함수를 통해 list 내의 요소들을 하나의 값으로 합칠 수 있음 
   - 이때 list 내 요소들은 str type이어야 함 
   - 하나의 예제로써 기록 

'''

def solution(n):
    
    list = sorted([value for value in str(n)], reverse=True)
    
    print("".join(list))
            
solution(118372)