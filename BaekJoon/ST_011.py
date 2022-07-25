
'''

 Backjoon _ exampels 5534

  "간판"   by Jinwoo Lee

  < algorithm >

  1. 입력으로 주어지는 각 간판값에 대해서, 시작과 끝값이 만드려고 하는 간판의 시작/끝 값과 같은 idx를 찾는다.


  2. 1번 과정을 통해 주어진 간판의 시작~ 끝 범위가 설정되고, 

     해당 범위 내에서  [start_idx + avg_interval*cnt] 를 통해 범위 내 일정 간격에 있는 알파벳이, 

     만들려고 하는 간판의 구성과 같은지 체크

  
'''



def make_ganpan(name, candidate):

    length_name = len(name)

    for start_idx in range(len(candidate)):

        for end_idx in range(start_idx, len(candidate)):

            if candidate[start_idx] == name[0] and candidate[end_idx] == name[-1]:

                avg_interval = (end_idx - start_idx) // (length_name-1) 

                cnt = 0

                while cnt < length_name :

                    if candidate[start_idx + avg_interval * cnt ] == name[cnt]:

                        cnt +=1

                    else: 

                        break

                        
                if cnt == length_name : return 1

 

    return 0


def solution():

    

    num = int(input())

    name = input()

    candidates = [input() for _ in range(num)]

    answer = 0 

 
    for candidate in candidates:

        answer += make_ganpan(name, candidate)

    print(answer)

solution()