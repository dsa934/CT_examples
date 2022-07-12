

'''

 Backjoon _ exampels 4821

  "페이지 세기"   by Jinwoo Lee

  < algorithm >

  1. 특수 문자 '-' , ' ' 에 대하여 입력받은 문자열을 split()을 통해 두번 분리

  2. 페이지가 중복 되면 안되기 떄문에 set() 자료 구조를 사용하여  범위 내 페이지 추가

  3. 위반 조건 chk 

    1) start > num 

    2) end > num && start < num 이면, start ~ num 까지 

    3) end < start


  * 최초 시도 - AC 받지 못함

    => 분리한 문자열이 (start,end) 의 범위 형태가 아닌, (just_one_page) 1장인 경우에,

       just_one_page > num 인 경우 인쇄를 할 수 없는 것으로 간주 

       num : 문서의 총 페이지 수 라고 문제에서 정의 

       => num은 '인쇄해야 할 종이 뭉치 수의 상한' 이 아니라 '인쇄 가능한 페이지의 상한' 을 의미 함 

 

'''



def solution():

    while True:

        num = int(input())

        if num == 0 :break

        candidate = set()

        string = input().split(",")

        sub_string = [ value.split("-") for value in string ]


        for value in sub_string:

        
            if len(value) == 1: 
                
                if int(value[0]) > num : continue
                else:
                    candidate.add(int(value[0]))

            else:

                s, e = value
                s, e = int(s), int(e)

                if e < s : continue

                elif num < s : continue  

                else:

                    for value in range(s,e+1):

                        if value > num : break

                        else:
                            candidate.add(value)

                            
        print(len(candidate))

solution()