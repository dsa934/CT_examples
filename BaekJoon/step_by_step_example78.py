'''

 Backjoon _ exampels #

  "Baek 1141 - Prefix (문자열)"   by Jinwoo Lee


 # Algorithm 

  0. 접두사 X집합의 최대 크기 출력 

  1. 2중 포문을 사용, 각 원소끼리 비교를해서 접두어가 되면 break, 안되면 끝까지 비교 

     h  hi  hello   run  rerun   running    =>   h, hi 비교  ( 접두어가능 break)
                                                 hi, hello 비교 (접두어 가능(break)
     h  hi  hello   run  rerun   running         hello, {run, rerun, running} 비교  접두어 불가 is_prefix = False


     => idx & cmp_idx 비교 , cmp_idx는 alphas[ idx+1 : ] 


  
  2. 접두어 관련 : index or startswith 함수 사용 가능 



 # Attention for Implementation

  1. index 함수는 찾고자하는 것이 없는 경우 오류가 발생 

    => try  ~ except 구문 

  2. 길이로 정렬시 key =len 으로 간략화 가능 

  3. temp.startswith(value) : temp 문자열이 value로 시작하면 True ,else : False


'''

num_alpha = int(input())

alphas = sorted([input() for _ in range(num_alpha)], key = len)

total =0 


for idx in range(len(alphas)):

    is_prefix = False

    for cmp_idx in range(idx+1, len(alphas)):

        if alphas[cmp_idx].startswith(alphas[idx]) : 

            is_prefix = True
            break

    if not is_prefix : total+=1

print(total)

