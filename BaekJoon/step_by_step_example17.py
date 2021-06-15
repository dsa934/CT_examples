'''

 Backjoon _ exampels #

  "Baek - 15649 N과 M ( Backtracking)"

 by Jinwoo Lee ( 2021/06/15 )


 # Attention for Implementation

  - itertools의 순열/조합 이용 ( 표준 라이브 러리라서 사용가능)

  - itertools 사용할 경우 데이터 형태가 (1,2)와 같은 tuple로 주어짐

    => .join function을 이용하여 문제에서 요구하는 출력형태를 맞춰줌



'''

from itertools import permutations

n, m = list(map(int,input().split()))


data = [ value for value in range(1,n+1) ]

p_data = list(permutations(data,m))


for value in p_data:

    print(' '.join(map(str,value)))