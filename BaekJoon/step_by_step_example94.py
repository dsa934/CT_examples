'''

 Backjoon _ exampels #

  "Baek 1213 - 팰린드롬 만들기 "(String)   by Jinwoo Lee


 # Algorithm 

  0. 입력이 주어지면 해당 입력을 palindrome 으로 만들기 ( 여러개면 사전순으로 가장 앞에 있는것을 출력) 

  1. 입력을 list화 + 내림차순 정렬하여, 정렬된 list의 앞에서부터 원소를 뺸다. (value =list.pop(0) )

  2. value가 원소에 list에 있을 경우 pair_value를 또 뺴준다 ( 사전에 정렬했기 떄문에 또다시 pop을 하면됨 cmp_value = list.pop(0) )

  3. 각각 save, rev_save에 넣어주고, value가 list에 없는경우 chk_cnt +=1

  4. 펠린드롬은 앞뒤가 똑같은 문자열이 되어야 함으로 chk_cnt 가 2이상일 경우 팰린드롬이 성립이 안되기 떄문에 break 


 # Attention for Implementation

  1. itertools로 구현할 경우 메모리 제한 위배 

  2. AABBCCCDD -> ABCD C DCBA ( chk_cnt로 따로 예외 처리를 해줘야 하는 이유 ) 



'''

string = sorted(list(input()))


save = [] 
rev_save = []


chk_cnt = 0

while string:

    value = string.pop(0)

    if value in string :

        save.append(value)
        
        cmp_value = string.pop(0)

        rev_save.append(cmp_value)

    elif value not in string and not string :

        save.append(value)

    else:
        
        string.append(value)
        chk_cnt +=1

        if chk_cnt == 2 : break



if chk_cnt == 2 : print("I'm Sorry Hansoo")
else: print( ''.join(save) + ''.join(reversed(rev_save)))

