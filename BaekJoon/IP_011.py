

'''

 Backjoon _ exampels 1817

  " 짐 챙기는 숌 "   by Jinwoo Lee

  < algorithm >

  1 . 책이 탑처럼 쌓여 있기 때문에 sort 사용 금지, 배열의 마지막부터 뺴내야 함 

  2. pop 한 책의 무게가 박스 허용치를 초과할 경우 

    a) 박스를 추가하고 ( answer +=1 )

    b) pop 한 value를 다시 넣어주고 info,append(value)

    c) 새로운 박스에 넣어야 함으로 total = 0 으로 초기화 


 

'''



def solution():

    num, weight = map(int, input().split())

    if num == 0 : print(0)

    else:
        info = list(map(int , input().split()))
        
        total, answer  = 0, 0

        while True:

            value = info.pop()
            
            total += value 

            if total == weight : 

                answer += 1

                total = 0

            # algorithm 2 
            elif total > weight :

                answer +=1 

                total = 0

                info.append(value)

            elif total < weight and len(info) == 0 :

                answer+=1

            if len(info) == 0 : break

        print(answer)




        
solution()