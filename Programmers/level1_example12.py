'''

 Programmers _ exampels 12

  "2019 KAKAO BLIND RECRUITMENT - 실패율"

 by Jinwoo Lee ( 2021/05/31 )



 # Condition

  - 실패율 계산시 해당 층을 N이라고 가정하면,

    실패율 =  n층에 도달했지만 클리어하지 못한 플레이어 수  / n층에 도달한 플레이어 수 



 # Attention for Implementation

  - 배열의 각 요소의 값을 비교하여 해당하는 idx로 정렬하는 법 

   => python dict 자료구조 사용 
   
   => result = sorted( target, reverse = , key = lambda x : x[ 정렬기준 ] )    # dict 구조라 (key, value) 쌍의 형태 임으로 [1]을 해야 value끼리 비교하여 정렬

   => result[0] : 정렬된 배열의 idx return (key, value) 쌍임으로

   => 정렬시 dict 사용하는 것에 익숙해지기 


'''

def solution(N, stages):

    # set init params
    result = dict()
    total_user = len(stages)
    current_user = 0

    for num_stage in range(N):

        if stages.count(num_stage+1) != 0 :

            # 실패율 계산
            result[num_stage+1] = stages.count(num_stage+1)/ (total_user-current_user)

            # 각층별 도전자 계산
            current_user += stages.count(num_stage+1)

        else :
            result[num_stage+1] = 0


    # sort
    final = sorted(result.items(), reverse=True, key = lambda x:x[1])
    
    return [value[0] for value in final]


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
solution(4, [4, 4, 4, 4, 4])
