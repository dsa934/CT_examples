
'''

 Backjoon _ exampels 17202

  "핸드폰 번호 궁합"   by Jinwoo Lee

  < algorithm >

  1. dp style로 문제를 풀지는 못했음

     => 전화번호가 무한 한것이 아니기 떄문 ( 추후 방법을 찾을 필요성 있음 )
 

'''



def solution():

    number_1 = list(input())
    number_2 = list(input())


    candidate = [] 

    for idx in range(len(number_1)):


        candidate.extend(number_1[idx] + number_2[idx])

    while len(candidate) != 2 :

        ans = [] 
        
        for idx in range(len(candidate)-1):

             ans.extend( str((int(candidate[idx]) + int(candidate[idx+1]) ) % 10 ) )



        candidate = ans


    print("".join(candidate))


solution()