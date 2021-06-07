'''

 Backjoon _ exampels #

  "Baek 1966 : Printer queue"

 by Jinwoo Lee ( 2021/06/07 )



'''


test_case = int(input())

num_page = []
info_list = []

answer = []
for _ in range(test_case):

    num_page.append(  list(map(int, input().split())) )
    info_list.append( list(map(int, input().split())) )

    
for idx in range(test_case):

    queue = [ (idx,value) for idx, value in enumerate(info_list[idx]) ]

    result = 0

    while True:

        page = queue.pop(0)

        if any ( page[1] < queue_value[1] for queue_value in queue ) :

            queue.append(page)


        else:

            result += 1

            if page[0] == num_page[idx][1]:

                answer.append(result)
                break

for value in answer:
    print(value)










