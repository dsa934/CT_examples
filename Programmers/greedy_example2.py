'''

 Programmers _ exampels #

  "Greedy - 조이스틱"

   by Jinwoo Lee ( 2021/06/03 )


 # Problem

  - 조이스틱을 이용해 알바벳 이름 완성하기 

  - 제일 초기상태 : A * N (N :글자수)

  - directoin => UP : 다음 알파벳(Z 넘어가면 A), DOWN : 이전 알파벳, LEFT : 커서왼쪾이동(마지막이면 마지막문자), RIGHT : 오른쪽이동

  - 항상 한쪽으로 이동하는것이 최소이동을 보장하지 않는다.


 # Attention for Implementation

  - filter 함수

  - 알파벳 변경기능과 이동기능을 구별해서 생각하기

  - 이동 연산을 구현할시(중요)
  
    1. 현재 위치(cur)를 기준으로 바꿔야하는 알파벳이 있는 change_list의 값들과 거리 계산

    2. 1에서 계산된 거리 중 최소의 위치로 이동 (cur = min_idx)

    3. 새로운 위치에서 1,2를 반복


  - 기존 코드가 실패했던 이유 

    바꿔야하는 change_list를 구한 후에 curser와의 비교없이 change_list에 담겨 있는 순서대로 이동했기 떄문에 최소를 보장하지 못함 


'''

def cal_move(change_list, cur, name, pos_count):

    pos = dict()

    for value in change_list:

        pos[value] = min( value - cur, len(name) + cur - value)

    min_idx = min(pos)
    min_value = min(pos.values())

    cur = min_idx
    change_list.remove(min_idx)

    pos_count += min_value
    
    return change_list, cur, pos_count


def solution(name):

    change_list = list(filter(lambda i : name[i] !='A', range(len(name))))

    count = 0
    pos_count = 0
    cur = 0

    #변환 연산
    for value in change_list:

        count += min ( ord('Z')+1 - ord(name[value]) , ord(name[value]) - ord('A'))

    

    #이동 연산
    while len(change_list) >0:

        change_list, cur, pos_count = cal_move(change_list, cur, name, pos_count)

    
    print(count+pos_count)

solution("JAN")
solution("JEROEN")
solution("ABAAAAAAAAABB")
solution("ZZAAAZZ")

#거리를 가지고 change list 를 정렬하면 해결되는거같음
