'''

 Backjoon _ exampels #

  "Baek 1744 - 수 묶기 "

 by Jinwoo Lee ( 2021/06/xx )


 # Attention for Implementation

  - 1과 조합되는 경우는 곱하는거보다 더하는게 더 크다 

  - 음수 양수 나뉘되 음수에 0을 포함시켜야함  ( -6, 0 이면 곱하면 0이라서 더 큰 수다)

  - 처음부터 입력리스트를 나눠서 하면 편했음  => simple한 아이디어 설계를 위해 알고리즘 뿐만 아니라 입력받는 방식까지 범위를 확장하여 고려하기 

    => 아이디어가 타당한데 코딩이 난잡해진다면 다른부분을 세분화하여 설계하기



  - heapq 사용

   1. 리스트 형성 -> 리스트를 max/min heap tree로 구성

   2. max : heapq._heappop_max(list_name)  / min : heapq.heappop(list_name)으로 꺼내서 사용 


'''

def pos_tied(list, result):

    while True:

        if len(list) == 0:
            break

        else:

            first = hq._heappop_max(list)

            if len(list) !=0:

                second = hq._heappop_max(list)

                if first == 1 or second == 1 : result.append(first+second)

                else : result.append(first*second)


            else:
                result.append(first)

    return result



def neg_tied(list,result):

    while True:

        if len(list) == 0:
            break

        else:

            first = hq.heappop(list)

            if len(list) !=0:

                second = hq.heappop(list)

                result.append(first*second)
                

            else:
                result.append(first)

    return result






import heapq as hq

num_digit = int(input())

positive_list = []
negative_list = []


for _ in range(num_digit):

    data = int(input())

    if data >0 : positive_list.append(data)
    elif data <= 0 : negative_list.append(data)

hq._heapify_max(positive_list)
hq.heapify(negative_list)

result = [] 
result = pos_tied(positive_list,result)
result = neg_tied(negative_list,result)

print(sum(result))

