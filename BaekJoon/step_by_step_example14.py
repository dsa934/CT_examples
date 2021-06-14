'''

 Backjoon _ exampels #

  "Baek - 2217 Rope"

 by Jinwoo Lee ( 2021/06/14 )


 # Attention for Implementation

  - 첫 구현시(while ~ for) 시간초과  => brute force가 아님  => 로프 리스트 내에서 해결 

  - 로프리스트를 내림차순 정렬 후

    => max( 로프길이 * 로프순위+1 , max_value) 비교 

    => 예를들어 [5,4,3,2,1]일 경우, 
    
        길이가 5인 로프 선택시 로프1개 => 최대 5

        길이가 3인 로프 선택시 3번쨰 로프까지 채용하는것임으로 로프 3개 => 3 * (idx+1) = 9 


  - if while ~ for문과 같이 하나씩 증가시켜서 일일히 찾는 경우가 가능하다 -> brute force

    else : greedy 

'''

# ~ O(nlogn)
import sys

tc = int(sys.stdin.readline())
max_value = 0

data = sorted([int(sys.stdin.readline()) for _ in range(tc)], reverse=True)

result = [value *(idx+1) for idx,value in enumerate(data)]

print(max(result))


