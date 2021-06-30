'''

 Backjoon _ exampels #

  "Baek 1041 - 주사위 (Greedy)"   by Jinwoo Lee


 # Algorithm 

  0. A~f로 구성된 주사위를 가지고 N으로 이루어진 정육면체를 만들때, 이 정육면체의 5면의 합이 최소가 되는 프로그램 

  1. ☆ 5면의 합이 최소가 되게 하려고 밑바닥을 6으로 깔아놓는다는 가정을 하면 문제를 풀 수 없음 

  2. 주사위를 가지고 정육면체를 만들때는 3면, 2면, 1면이 보이는 주사위가 있다.

     2-1. 3면이 보이는 경우, 정육면체의 꼭지점 : 4개 (원래 8개인데 밑면은 탁자위에 있어서 안보이기떄문에 4개 )

     2-2. 1면이 보이는 경우, 4옆면 +1윗면 : 4(n-2)(n-1) + 1*(n-2)(n-2)

     2-3. 2면이 보이는 경우, 전체 - (아예 안보이는 주사위 + 1면만 보이는 주사위 + 3면만 보이는 주사위) 

          => n^3 - ( (n-2)(n-2)(n-1) + 4(n-2)(n-1) + 1*(n-2)(n-2) + 4)

  3. 1,2,3면이 보이는 주사위 개수 * F값 ( F값은 마주보지 않는 주사위 면 합 중 최소가 되도록) 



 # Attention for Implementation

  1. 밑면을 6으로 두면 최소가 된다는 가정은 문제를 이해하는데 혼란을 야기한다.

  2. 주사위에 해당하는 number가 정렬되지 않은 상태로 들어온다면 순서에 신경써야 한다 .

     2-1. 주사위 : [3 2 1 1 3 3]으로 주어지는 경우 [3,3], [2,3], [1,1] 의 마주보는 조합 중에 작은값을 취해야 한다 .

     2-2. N=1인 경우 주사위 배열중 가장큰값 1개를 뺸 나머지의 합으로 처리 


'''

from collections import deque

num = int(input())

number = list(map(int,input().split()))

pair =  deque(sorted([ sorted([number[0], number[5]]) , sorted([number[1], number[4]]), sorted([number[2], number[3]]) ] ))


if num == 1 : 
    
    max = max(number)
    number.remove(max)
    print(sum(number))




else:

    side1 = 4 * (num-2) * (num-1) + (num-2) * (num-2)

    side3 = 4

    side2 = num**3 - ((num-2)*(num-2)*(num-1) + side1 + side3)


    val1 = pair.popleft()[0]

    val2 = val1 + pair.popleft()[0]

    val3 = val2 + pair.popleft()[0]

    print(val1* side1 + side2*val2 + val3*side3)

