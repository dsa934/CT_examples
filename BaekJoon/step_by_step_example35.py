'''

 Backjoon _ exampels #

  "Baek 1475 - 방 번호"   by Jinwoo Lee


 # Algorithm 

  0. 입력을 문자로 받아서, 각 문자별 중복회수를 계산하여 가장 큰 횟수만큼 셋트가 필요함 

  1. 6,9가 스왑이 가능하기 떄문에 count_list에 6과 9중 한개만 없는 경우에 대하여 count를 줄일 수 있음  
  
  2. dict 자료형을 활용하여 6,9 에대한 중복회수를 체크하고, 중복횟수의 짝, 홀수에 따른 경우를 나누어 카운터 수를 조절한다


     1) if count('6') % 2  == 0  : count('6') //=2        2) count('6') % 2 != 0 : count('6') //= 2 +1
      
  3. 2번 과정 진행 후 max(count_list) 값이 최종값이된다.


  4. 1의반례 99699 등장 6과 9가 모두 있을떄도 처리가 필요함 => 99699 -> 3 

    ['9'] = 4   => '9', '6' 둘다 있는 경우, cnt = min(count['9'] , count['6']) + tmep 
    ['6'] = 1       
                    temp = >   if max(count['9'], count['6']) % 2 == 0 : temp //2
                               else : (temp //2) + 1




 # Attention for Implementation

  - input 받을떄 

    input().split() -> 이 경우 공백을 기준으로 단어를 나누며, 2개의 이상의 입력일 경우 string 형태로 저장

    list( input().split() ) -> 이와 같이 list를 취하면, '9999'와 같은 단어가 개별적으로 분리되어 str형태로 저장된다

'''

num_str = list(input())

unique_num = list(set(num_str))


count_list = {value: num_str.count(value) for value in unique_num }


if '6' in count_list.keys() and '9' not in count_list.keys(): 

    if count_list['6'] %2 == 0: count_list['6'] //=2

    else : 
        count_list['6'] = (count_list['6'] // 2 ) +1


elif '9' in count_list.keys() and '6' not in count_list.keys(): 

    if count_list['9'] %2 == 0: count_list['9'] //=2

    else : 
        count_list['9'] = (count_list['9'] // 2 ) +1

elif '9' in count_list.keys() and '6' in count_list.keys():


    temp = max(count_list['9'], count_list['6']) - min(count_list['9'], count_list['6'])

    if temp %2 == 0 : temp //= 2
    else : temp = (temp //2) + 1

    # 굳이 6,9에 안넣고 0으로 만든 후 새로 추가해도 무관함
    count_list['tmp'] = temp + min(count_list['9'], count_list['6'])
    count_list['6'], count_list['9'] = 0,0


print(max(count_list.values()))
 