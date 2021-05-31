'''

 Programmers _ exampels #

  "문자열 내림차순 배치하기"

 by Jinwoo Lee ( 2021/05/26 )


 # Problem
 
 - 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
 - s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.
 - "Zbcdefg" -> "gfedcbZ"

 # Attention for Implementation

  - 이 코드는 어렵지 않으나, 문자열에 대한 정렬에서 소문자+대문자 형태의 문자열을 정렬할경우 
   
    대문자 < 소문자 정렬이 default임을 기억하자 ( 따라서 아래와 같이 upper alphabet point를 구할필요는 없었음)

    다만 아래코드와 같이 진행시 소문자/대문자를 분리하여 출력하는 다른문제에 적용이 가능함 

'''

def solution(s):
    
    
    # find Upper alphabet
    upper_idx = [idx for idx,value in enumerate(sorted(s,reverse=True)) if value.isupper()]
    
    result =[]
    sort_list = sorted(s,reverse=True)
    
    if len(upper_idx) !=0 :result = ''.join(sort_list[:upper_idx[0]] + sort_list[upper_idx[0]:] )
    else:
        result = ''.join(sort_list)

    
    return result
   