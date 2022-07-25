
'''

 Backjoon _ exampels 1417

  "국회의원 선거"   by Jinwoo Lee

  < algorithm >

  1. 입력의 첫번쨰가 다솜에 해당하는 기호 1번 임으로 , 이를 제외한 나머지 후보를 내림차순으로 정렬

  2. 내림차순 정렬 시 , sub_candidate[0]이 항상 큰값이 보존됨으로, 

     이 값과 기호1번에 해당하는 dasom 값을 비교해서 dasom이 가장 클떄까지 해당 행위를 반복 
 

'''


def solution():

    num = int(input())

    candidate = [ int(input()) for _ in range(num)]

    if num == 1 : print(0)


    else:


        answer = 0 

        sub_candidate = sorted(candidate[1:], reverse= True)

        dasom = candidate[0]

 

        while sub_candidate[0] >= dasom :

            dasom +=1

            sub_candidate[0] -=1

            answer +=1

 
            sub_candidate = sorted(sub_candidate, reverse = True)


        print(answer)



solution()