'''

 Backjoon _ exampels #

  "Baek - 1339 단어 수학 "

 by Jinwoo Lee ( 2021/06/15 )


 # Attention for Implementation

  - 2            각 알파벳의 자리수를 따져서, 내림차순 정렬 후 9~0 부여 후 합치면 가장 큰값이 나옴 
    AAAAA   =>    A : 11112    9
    BBBDD         B : 11100    8
    CCA           C : 110      7  
                  D : 11       6
 

  - 처음 풀이는 입력단어 자리수로 정렬하여 시도 => 반례 1 <-> 반례2  상충사례가 있어 해결 불가능

    반례 1)   AB                반례2)  AAAAA
              BA                        BBBDD 
                                        CCA
  

  - dict tyep -> value 로 정렬하기 

    => sorted( dict.values()  or dict.items() or dict.keys() , reverse=False ) 

   
'''
# set init params
num_word = int(input())
words = [input() for _ in range(num_word)]
result = {}

# 자리수 판별 
for word in words:
    
    # 10^0 = 1
    tmp_len = len(word)-1

    for char in word:

        if char in result.keys():

            result[char] += 10**tmp_len

        else:

            result[char] = 10 ** tmp_len

        tmp_len -=1


sorted_result = sorted(result.values(), reverse=True)

total = 0

for idx in range(len(sorted_result)):

    total += sorted_result[idx] * (9-idx)

print(total)




