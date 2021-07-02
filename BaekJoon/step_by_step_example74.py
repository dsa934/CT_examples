'''

 Backjoon _ exampels #

  "Baek 1058 - 친구 (BF)"   by Jinwoo Lee


 # Algorithm 

  0. 2-친구의 조건 : A-B가 서로 친구이거나 , A-C 친구, B-C 친구인 친구 C가 있을 경우 

  1. 서로 친구인 경우를 카운팅 하고(배열의 요소가  Y인 경우) 해당 idx를 yes_list에 저장 

  2. 2번쨰 조건인 건너건너 친구를 고려하기 위해, 

     Row 기준 조사결과, A-C가 친구가 아니라면  C에 대한 조사 (Col 기준)를 통하여 

     A의 yes_list 에 해당하는 위치의 값이 C에서도 'Y'인 부분이 있다면 추가로 카운팅 하는것을 고려 

    

 # Attention for Implementation

  1. A와 친구인 yes_list를 얻기 위해 2중 포문을 나눠서 해줘야 함




'''


person = int(input())


people = [input() for _ in range(person) ]

result = []

row_idx = 0

while row_idx < person:

    cnt = 0 
    yes_list = []

    for col_idx in range(person):

        if people[row_idx][col_idx] == 'Y': 

            yes_list.append(col_idx)
            cnt+=1

    
    for col_idx in range(person):

        if people[row_idx][col_idx] == 'N' and row_idx != col_idx :
      
            for chk_idx in yes_list:

                if people[chk_idx][col_idx] == 'Y' :

                    cnt+=1
                    break


    result.append(cnt)
    row_idx +=1


print(max(result))