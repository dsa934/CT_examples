
'''

 Backjoon _ exampels 1205

  "등수 구하기"   by Jinwoo Lee

  < algorithm >

  1. N == 0 ,  N != 0 

     N == 0 이면 무조건 1등


  2. N == P 인데 score의 마지막값(제일 작은값) 보다 태수의 점수가 낮으면 랭킹에 들어갈 자리조차 없기 떄문에 -1 출력


  3. N != P 일 경우,  

    태수의 점수를 N+1 로 초기값 설정( 가장 랭킹이 낮다고 생각)

    이후 score 점수를 돌면서 태수 점수보다 낮은 구간이 있다면 그 index+1 이 답이 됨

    index가 0부터 시작함으로 index+1 해야함




    * 등수 구할떄 동점자가 있다고 해서 너무 어렵게 dict 같은거 써서 하지 말기 , 조건화 하기 

    * 범위 체크 .0 <= N <= P 

'''


def solution():

    n, score, p = map(int, input().split())

    if n == 0: answer = 1

    else:

        score_board = list(map(int, input().split()))

        if n == p and score_board[-1] >= score : answer = -1
            
        else:

            answer = n +1

            for i in range(n):

                if score_board[i] <= score :

                    # idx 가 0부터 시작이니 +1 해줘야 원래 등수가 나옴,  score보다 작은거 찾으면 그자리가 삽입될 자리임
                    answer = i +1 
                    break
        
    print(answer)
solution()