'''

 Backjoon _ exampels #

  "Baek 9375 - 패션왕 신해빈" (String)   by Jinwoo Lee


 # Algorithm 

  0. 패션 종류가 주어졌을때 겹치지 않고 입었을떄의 총 패션 가지수 출력 

  1. a,b,c type의 옷이 있다면 1종류의 type만 입거나, 2종류, 3종류 ... len(type) 종류의 옷을 혼합하여 입을 수 있다. 

  2. 총 조합의 수를 구하기 위해서는 1,2,3 ... len(type) 종류의 옷을 입었을떄의 경우의 수를 모두 더해야 하는데 

     => 일일히 따지지 않고, "공백"을 추가함으로써 이를 간단하게 코딩할 수 있게 된다

     example ) 

     hat headgear                   headgear : [ hat, turban, empty ]
     turban headgear                eyewear : [sunglasses, empty ] 
     sunglasses eyewear        =>   face  : [ mask, empty ]              =>   조합 수 : (3 x 2 x 2 ) - 1  
     mask face                                                                 ( 전부다 empty의 가지수를 제외 하기 위해 -1 )


 # Attention for Implementation



'''

num_test = int(input())

result = []

for _ in range(num_test):

    num_item = int(input())

    closet = {}

    for _ in range(num_item):

        item, _type = input().split()

        if _type not in closet.keys() : 

            closet[_type] = 2  # 공백 포함 

        else:
            closet[_type] += 1

    total = 1

    for value in closet.values():
        total *= value
        
    result.append(total-1)

for value in result:
    print(value)
    