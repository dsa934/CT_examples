'''

 Backjoon _ exampels #

  "Baek - 13305 주유소"

 by Jinwoo Lee ( 2021/06/09 )

     case 1

     1    3        2        4

       2      3        1 

    case 2

    2    3        1      4

      2       3       1

    case 3

    1    1      1       1

      3     3       4


 # Attention for Implementation

  - 현재 위치의 주유소와 다음 위치에 있는 주유소간의 가격을 비교

  - greedy 문제가 나오는 경우, 전체 경우를 다 고려하지말고 부분적인(현 위치에서) 해를 구하여 iterative 하게 진행하도록 코딩하기 


'''

num_city = int(input())
load = list(map(int,input().split()))
city = list(map(int,input().split())) 

pos = 0 
total = 0 
current_oil = 0

length = 0

while num_city>1:

    for idx in range(len(city)):
        
        if pos == idx :
            continue

        # 현재 위치의 주유소가 다음 주유소보다 싼 경우
        elif city[pos] <= city[idx] :

            total += load[idx-1] * city[pos]
            num_city -=1

            if num_city == 1:
                break

        # 현재 위치 주유소가 다음 주유소가 비싼 경우
        elif city[pos] > city[idx] :

            # 일단 다음주유소까지 가야하기 때문에 그 길이만큼 주유하고 
            total +=load[idx-1] * city[pos]

            # 현 주유소를 다음 주유소로 옮겨줌
            pos = idx
            num_city -=1

            if num_city == 1:
                break


print(total)


            



