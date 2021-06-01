'''

 Programmers _ exampels 3

  "Printer"

 by Jinwoo Lee ( 2021/06/01 )


 # Problem

  - 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
  - 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
  - 그렇지 않으면 J를 인쇄합니다.

  - 현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 
  - 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.


  # Attention for Implementation

  - 각 인쇄물에 대한 네이밍을 어떻게 유지할 것인지 ?

    -> index list와 value list를 따로 작성했는데 이 방식은 python 스럽지 않아서

       collection library가 코딩테스트에서 사용이 가능한것 같으니 이 부분을 이용해보기 


  * Copy function 

    - python은 기본적으로 포인터 이기 때문에  

     list1 = list2 이후  list.sort()와 같은 형태로 정렬하면 list2또한 변화하기 떄문에

     list1 = list2.copy()와 같이 값만 복사해온다는 의미로 사용 



def solution(priorities, location):

    # set init params
    result = []
    idx = 0 

    index_list = [idx for idx in range(len(priorities))] 
    value_list = priorities.copy()

    while value_list != sorted(value_list, reverse=True):

        if value_list[idx] < max(value_list[idx+1:]):

            index_list.append(index_list.pop(idx))
            value_list.append(value_list.pop(idx))

        else:
            # 실제 출력 구현을 위해 pop을 써버리면 매 iterate 마다 배열길이가 달라지기 떄문에 
            # 구현하지 않는 것이 더 효율적
            idx +=1

   
    return index_list.index(location) +1


  * 위 코드보다 더욱 python 스러운 코드를 완성해보자 



  # Attention for Implementation 2

  * 인쇄물 인덱스 유지에 대한 해답 = > any keyword

   - any를 list comprehension 처럼 사용 가능 

     ex ) if any(q_value < que for que in queue)



'''



def solution(priorities, location):
    
    # set init params
    result = 0

    # tied (idx, list_value)
    queue = [ (idx, value) for idx, value in enumerate(priorities) ]


    while True:

        # 페이지 출력
        page = queue.pop(0)

        if any(page[1] < queue_value[1] for queue_value in queue) :

            queue.append(page)

        # 이미 위에서 출력했으니 횟수만 증가
        else:

            result +=1

            if page[0] == location:

                return result

           

solution([2,1,3,2], 2)