'''

 Programmers _ exampels 11

  "크레인 인형뽑기 게임 - 2019 카카오 개발자 겨울 인턴쉽"

 by Jinwoo Lee ( 2021/05/31 )


def delete_basket(basket,result):

    while True:

        # cmp basket's elements
        for idx in range(len(basket)-1):

            if basket[idx] == basket[idx+1]:

                result += 2
                basket[idx] =0
                basket[idx+1] =0

        new_basket = []
        nonzero_list = []

        for idx, value in enumerate(basket):

            if value != 0:

                nonzero_list.append(idx)

    
        for value in nonzero_list:

            new_basket.append(basket[value])

        
        if len(basket) == len(new_basket):
            break

        basket = new_basket

    return result

        
def solution(board, moves):

    # set init params
    basket = []
    init_basket = 0
    result = 0

    for curser in moves:

        for idx, row in enumerate(board):

            # is_empty 
            if row[curser-1] == 0:
                continue

            else :

                basket.append(row[curser-1])
                board[idx][curser-1] = 0
                break

    
    # doll pop    
    result = delete_basket(basket,result)

    

 # 위 코드는 너무 어렵게 구현하여 간단하게 다시 구현해보기 
 
 # Attention for implementation

  - claw function : 굳이 board를 전치행렬로 다루지 않고 moves 와 board의 row로 indexing 하여 인형을 뽑을 수 있음


  - delete function 

    -> 인형을 다 뽑아놓고, 뽑은 list에서 삭제하려고 하니 구현이 더 어렵게 되었음

    => 인형을 뽑는것과 동시에 basket의 길이가 1이상일 경우 비교하여 삭제하는 연산을 동시에 하면 위와 같은 고민을 해결 할 수 있음 

    => Stack을 활용하기 ( 앞으로 중복 삭제에 관련한 issue는 stack을 활용해보기)

    => break 위치 중요 : 인형을 뽑고 -> basket 비교 후 -> 집게 이동 이기 떄문에 ifrow[claw-1] != 0 과 맞물려야 함

'''

def solution(board, moves):

    # set init params
    basket = []
    result = 0

    # claw
    for claw in moves:

        for idx,row in enumerate(board):
            
            if row[claw-1]!= 0 :
                basket.append(row[claw-1])
                board[idx][claw-1] = 0
                
                if len(basket) > 1 :

                    if basket[-1] == basket[-2] :
                        basket.pop()
                        basket.pop()

                        result += 2

                # break 위치 중요 
                break
    
    return result

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4] )
