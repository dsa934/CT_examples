
'''

 Backjoon _ exampels 5635

  "생일"   by Jinwoo Lee

  < algorithm >


  1. 문자열 분해 후, 생년월일을 모두 일로 통일하여 대소 비교 -> lambda x : x[1] 을 이용 
 

'''



def solution():
    

    num = int(input())

    candidate = [] 

    for _ in range(num):

        info = list(input().split())

        date = int(info[3]) *365 + int(info[2]) * 30 + int(info[1]) 

        candidate.append([info[0], date])

    candidate = sorted(candidate, key = lambda x : x[1] , reverse=True)

    print(candidate[0][0])
    print(candidate[-1][0])





solution()